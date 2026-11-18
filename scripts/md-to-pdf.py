#!/usr/bin/env python3
"""Convert Markdown files to dark, landscape PDFs.  Facilitator tool, not part of the app.

    ./scripts/md-to-pdf.py slidev/hackathon.md hackathon/facilitator/*.md
    ./scripts/md-to-pdf.py -d out/ --mode doc notes.md

Needs: python3 (stdlib only), pandoc, and a Chromium-based browser (Chrome, Chromium, Edge).
Optional: mmdc (mermaid-cli) to draw ```mermaid blocks; without it they stay as code.

Two modes (--mode, default auto):
  doc     plain Markdown: flowing A4 landscape pages.
  slidev  Slidev deck: one page per slide (16:9), no incremental builds. v-click / v-clicks /
          v-after are removed so everything is visible, speaker notes (<!-- -->) and
          per-slide frontmatter are dropped (layout and class are kept as styling hints).
          `auto` picks slidev when the leading frontmatter has `theme:` or `layout:`.

Style lives in scripts/md-to-pdf.css (override with --css).
"""
import argparse, html, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_CSS = HERE / "md-to-pdf.css"
DEFAULT_OUT = HERE.parent / "pdf"

PANDOC_FORMAT = ("markdown-tex_math_dollars-smart-raw_tex-citations-yaml_metadata_block"
                 "-implicit_figures-auto_identifiers+task_lists+fenced_divs")


def die(msg):
    sys.exit(f"md-to-pdf: {msg}")


def find_chrome():
    env = os.environ.get("CHROME")
    if env:
        return env
    for p in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Chromium.app/Contents/MacOS/Chromium",
              "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
              "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"):
        if os.path.exists(p):
            return p
    for n in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        w = shutil.which(n)
        if w:
            return w
    die("no Chrome/Chromium/Edge found; install one or set CHROME=/path/to/browser")


# --------------------------------------------------------------------------- shared

FENCE = re.compile(r"^\s*(```+|~~~+)")


def split_fenced(text):
    """Yield (is_code, line) so callers can leave fenced blocks alone."""
    fence = None
    for line in text.split("\n"):
        m = FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)[0] * 3
            yield True, line
        elif fence is not None:
            yield True, line
            if m and m.group(1).startswith(fence):
                fence = None
        else:
            yield False, line


class Mermaid:
    """Replaces ```mermaid blocks by placeholders; renders them with mmdc if available."""

    def __init__(self, tmp):
        self.tmp, self.mmdc, self.svgs = tmp, shutil.which("mmdc"), []
        self.warned = False

    def extract(self, text):
        out, buf = [], None
        for line in text.split("\n"):
            if buf is None and re.match(r"^\s*```+\s*mermaid\b", line):
                buf = []
                continue
            if buf is not None:
                if re.match(r"^\s*```+\s*$", line):
                    svg = self.render("\n".join(buf))
                    if svg is None:
                        out += ["```text"] + buf + ["```"]
                    else:
                        out.append(f"MERMAIDFIG{len(self.svgs)}X")
                        self.svgs.append(svg)
                    buf = None
                else:
                    buf.append(line)
                continue
            out.append(line)
        return "\n".join(out)

    def render(self, code):
        if not self.mmdc:
            if not self.warned:
                print("  note: mmdc not found, mermaid diagrams are left as code", file=sys.stderr)
                self.warned = True
            return None
        n = len(self.svgs)
        src, dst = Path(self.tmp, f"m{n}.mmd"), Path(self.tmp, f"m{n}.svg")
        src.write_text(code, encoding="utf-8")
        cfg = Path(self.tmp, "mmdc.json")
        cfg.write_text('{"args": ["--no-sandbox"]}')
        r = subprocess.run([self.mmdc, "-i", str(src), "-o", str(dst), "-t", "dark", "-b", "transparent",
                            "--svgId", f"mmd{n}", "-p", str(cfg), "-q"], capture_output=True, text=True)
        if r.returncode or not dst.exists():
            print(f"  note: mermaid diagram {n + 1} failed ({r.stderr.strip()[:200]}); left as code", file=sys.stderr)
            return None
        svg = dst.read_text(encoding="utf-8")
        return svg[svg.index("<svg"):]

    def inject(self, body):
        for i, svg in enumerate(self.svgs):
            body = body.replace(f"<p>MERMAIDFIG{i}X</p>", f'<div class="mermaid-fig">{svg}</div>')
        return body


# --------------------------------------------------------------------------- slidev

YAMLISH = re.compile(r"^(?:[A-Za-z_][\w-]*\s*:(?:\s|$)|\s+\S|\s*-\s|\s*#)")


def is_yaml(chunk):
    lines = [l for l in chunk if l.strip()]
    return bool(lines) and all(YAMLISH.match(l) for l in lines) and YAMLISH.match(lines[0]) \
        and re.match(r"^[A-Za-z_][\w-]*\s*:", lines[0])


def parse_slidev(text):
    """-> list of (frontmatter dict, markdown body). Handles headmatter and per-slide frontmatter."""
    chunks, cur = [], []
    for code, line in split_fenced(text):
        if not code and line.rstrip() == "---":
            chunks.append(cur)
            cur = []
        else:
            cur.append(line)
    chunks.append(cur)

    slides, i = [], 0
    if chunks and not any(l.strip() for l in chunks[0]):  # file starts with ---
        i = 1
    pending_fm = None
    first = True
    while i < len(chunks):
        c = chunks[i]
        # a yaml-looking chunk followed by another chunk is frontmatter for that next chunk
        if i + 1 < len(chunks) and is_yaml(c) and (first or pending_fm is None):
            pending_fm = parse_fm(c)
            first = False
            i += 1
            continue
        first = False
        body = "\n".join(c).strip("\n")
        slides.append((pending_fm or {}, body))
        pending_fm = None
        i += 1
    return slides


def parse_fm(lines):
    d = {}
    for l in lines:
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", l)
        if m:
            d[m.group(1)] = m.group(2).strip().strip("'\"")
    return d


def clean_slide(body):
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)                       # speaker notes
    body = re.sub(r"<style\b.*?</style>", "", body, flags=re.S | re.I)       # per-slide CSS: not portable
    body = re.sub(r"</?v-(?:clicks?|after|switch|click-gap)\b[^>]*>", "", body)  # wrapper components
    body = re.sub(r"\s(?:v-click(?:-hide)?|v-after|v-clicks|v-motion)(?:\.[\w.]+)?(?:=\"[^\"]*\")?(?=[\s>/])", "", body)
    body = re.sub(r"(?m)^(\s*[-*+]\s)\[\](\s)", r"\1[ ]\2", body)            # `- []` -> task item
    out = []
    for code, line in split_fenced(body):                                    # ```json {all|2|3-4} -> ```json
        if code:
            line = re.sub(r"^(\s*(?:```+|~~~+))\s*([\w+#.-]*)\s*(?:\{[^}]*\}\s*)*(?:\[[^\]]*\]\s*)?$", r"\1\2", line)
        out.append(line)
    return "\n".join(out).strip("\n")


def slidev_markdown(text, mermaid):
    parts = []
    for fm, body in parse_slidev(text):
        body = mermaid.extract(clean_slide(body))
        if not body.strip() and not fm.get("layout"):
            continue
        classes = ["slide", "layout-" + re.sub(r"\W", "", fm.get("layout", "default") or "default")]
        classes += (fm.get("class") or "").split()
        cls = " ".join(f".{c}" for c in classes if re.fullmatch(r"[\w:/.-]+", c) and c != "slide") or ""
        parts.append(f"::::: {{.slide {cls}}}\n::: slide-body\n{body}\n:::\n:::::\n")
    return "\n".join(parts)


# --------------------------------------------------------------------------- build

FIT_JS = """
document.querySelectorAll('.slide').forEach(function (s) {
  var b = s.querySelector('.slide-body'); if (!b) return;
  var cs = getComputedStyle(s), avail = s.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  var centered = /layout-(cover|center|section)/.test(s.className), k = 1;
  for (var i = 0; i < 40; i++) {
    b.style.width = (100 / k) + '%'; b.style.transform = 'scale(' + k + ')'; b.style.marginBottom = '0';
    if (b.scrollHeight * k <= avail || k <= 0.35) break;
    k -= 0.025;
  }
  if (centered) b.style.marginTop = Math.max(0, (avail - b.scrollHeight * k) / 2) + 'px';
  b.style.marginBottom = (-(b.scrollHeight * (1 - k))) + 'px';
});
"""


def build(src, out, mode, css, chrome, keep_html):
    text = src.read_text(encoding="utf-8")
    if mode == "auto":
        head = re.match(r"\A---\n(.*?)\n---\s*\n", text, flags=re.S)
        mode = "slidev" if head and re.search(r"(?m)^(theme|layout)\s*:", head.group(1)) else "doc"
    with tempfile.TemporaryDirectory(prefix="md2pdf-") as tmp:
        mermaid = Mermaid(tmp)
        if mode == "slidev":
            md = slidev_markdown(text, mermaid)
            n = md.count("::::: {.slide")
        else:
            md = "::: doc\n" + mermaid.extract(text) + "\n:::\n"
            n = None
        title = re.search(r"(?m)^#\s+(.+)$", text)
        cmd = ["pandoc", "-f", PANDOC_FORMAT, "-t", "html5", "-s", "--embed-resources",
               "--css", str(css), "-V", "document-css=false", "--syntax-highlighting=breezedark",
               "--metadata", f"pagetitle={title.group(1) if title else src.stem}",
               "--resource-path", str(src.parent)]
        r = subprocess.run(cmd, input=md, capture_output=True, text=True)
        if r.returncode:
            die(f"pandoc failed on {src}: {r.stderr.strip()}")
        page = mermaid.inject(r.stdout)
        if mode == "slidev":
            page = page.replace("</body>", f"<script>{FIT_JS}</script></body>")
        page = page.replace("<body>", f'<body class="{mode}">', 1)
        htm = Path(tmp, "page.html")
        htm.write_text(page, encoding="utf-8")
        out.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                            f"--user-data-dir={tmp}/profile", "--allow-file-access-from-files",
                            "--virtual-time-budget=5000", f"--print-to-pdf={out}", htm.as_uri()],
                           capture_output=True, text=True, timeout=180)
        if not out.exists() or out.stat().st_size == 0:
            die(f"browser produced no PDF for {src}:\n{r.stderr[-800:]}")
        if keep_html:
            shutil.copy(htm, out.with_suffix(".html"))
    print(f"  {src} -> {out}  [{mode}{f', {n} slides' if n else ''}]")


def main():
    ap = argparse.ArgumentParser(description="Markdown (plain or Slidev) to dark landscape PDF.")
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("-d", "--out-dir", type=Path, default=DEFAULT_OUT, help=f"output directory (default {DEFAULT_OUT.name}/)")
    ap.add_argument("-o", "--output", type=Path, help="output file (single input only)")
    ap.add_argument("--mode", choices=["auto", "doc", "slidev"], default="auto")
    ap.add_argument("--css", type=Path, default=DEFAULT_CSS)
    ap.add_argument("--keep-html", action="store_true", help="also write the intermediate .html next to the PDF")
    a = ap.parse_args()
    if a.output and len(a.files) != 1:
        die("-o needs exactly one input file")
    if not shutil.which("pandoc"):
        die("pandoc not found (brew install pandoc)")
    if not a.css.exists():
        die(f"stylesheet not found: {a.css}")
    chrome = find_chrome()
    for f in a.files:
        if not f.is_file():
            die(f"no such file: {f}")
        build(f, a.output or a.out_dir / (f.stem + ".pdf"), a.mode, a.css.resolve(), chrome, a.keep_html)


if __name__ == "__main__":
    main()
