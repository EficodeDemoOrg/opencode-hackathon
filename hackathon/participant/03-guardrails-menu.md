Guardrails Menu
===
Pick several, layer them, and say **what enforces each**. A guardrail that is only a sentence in a prompt is advice, not a control.

Strength: **Hard** = holds whatever the model decides. **Soft** = depends on the model following instructions. **Detect** = does not prevent, but tells you.

# Preventive: limit what the agent can do
| Control | Strength | How, without Node | Example |
|---|---|---|---|
| **Permission rules** (`opencode.json`) | Hard | `permissions` array; last matching rule wins | deny `git push *`, `rm *`, `git clone *` |
| **Per-agent permissions** | Hard | `permissions` in the agent front matter; repeat critical denials | `deliver` may edit `src/main/**` and `specs/**` only |
| **Deny first, then allow** | Hard | `shell *` deny, then exact allows | sub-agent may run only the Atlassian tool and `mvn test` |
| **Edit lanes** | Hard | `edit` allow only on named paths | `test-writer` only `src/test/**` |
| **No `execute`** | Hard | deny `execute` | stops JavaScript with network access that shell rules cannot see |
| **Allow-listed sub-agents** | Hard | `subagent` allow list | orchestrator cannot call anything else |
| **Read-only tools by construction** | Hard | tool code has no write path | `Atlassian.java` does GET only |
| **Scope allow-lists** | Hard | env vars | `JIRA_ALLOWED_PROJECTS`, `BITBUCKET_ALLOWED_REPOS` |
| **Credentials the agent never sees** | Hard | tool reads env; deny `*TOKEN*`, `env`, `printenv` | agent calls the tool, not curl |
| **Reference clones are read-only** | Hard | deny `edit repos/**`, push disabled | `repos/` is for reading |
| **Narrow, least-privilege tokens** | Hard | read-only, one project | even a manipulated agent cannot write |
| **Skills with exact commands** | Soft | `SKILL.md` | "run exactly this, stop on error" |
| **Iteration caps** | Soft | agent prompt | "at most 5 rounds, then stop and report" |
| **Never do a sub-agent's job** | Soft | agent prompt | a failing sub-agent stops the pipeline |

Rules match command **text**, not intent. Check for a second route to the same thing: `read` denied on `.env` does not stop `shell cat .env` if `cat *` is allowed.

# Preventive: limit what reaches the repository
| Control | Strength | How | Example |
|---|---|---|---|
| **Agent cannot commit** | Hard | deny `git add/commit/push` | a person commits |
| **Commit hooks** | Hard (local) | `scripts/githooks/pre-commit`, `commit-msg` | tests pass, no secrets, ticket key, `Reviewed-by:` |
| **CI** | Hard | pipeline on the branch | `mvn verify`, static analysis, dependency scan |
| **Branch protection, required reviewers** | Hard | Bitbucket settings | two approvals, no self-approval |
| **Small batches** | Soft | spec size limits | one ticket, one branch |

# Detective: know what happened
| Control | Strength | How | Example |
|---|---|---|---|
| **Audit log** | Detect | `logs/atlassian-audit.log` and git history | what the agent read, when |
| **Untrusted markers** | Soft | tool wraps external text | agent told to treat it as data |
| **"Suspicious content" line in every report** | Detect | report format | quote any instruction found in inputs |
| **Reviewer sub-agent** | Detect | read-only `code-reviewer` | checks spec, layering, tests |
| **Canary tests** | Detect | a ticket with a planted instruction | must be reported, not obeyed |
| **Open questions in the report** | Detect | skill/agent prompt | assumptions listed, not hidden |

# Corrective: stop and recover
| Control | How |
|---|---|
| **Kill switch** | remove the agent file or the allow rule; revoke the token |
| **Rollback** | the agent's work is an uncommitted diff or a branch: discard it |
| **Token rotation** | tokens are short-lived and scoped; rotate after the pilot |

# Human accountability checklist
- [ ] A named person owns the agent configuration.
- [ ] A named person reads **every** diff the agent produces before it is committed.
- [ ] The commit records that person (`Reviewed-by:`).
- [ ] The human can see what the agent read (audit log).
- [ ] The human has what they need to check the work: tests, the spec, a UI checklist.
- [ ] "Approve" is never the default: the report ends with what to check, not "looks good".

# Questions the board will ask
1. What is the worst it can do if the model is wrong? If an attacker controls an input?
2. What stops it if the prompt is ignored?
3. Who reads the output, and what happens if they are tired?
4. How do you know it works? On how many cases?
5. How do I turn it off?
