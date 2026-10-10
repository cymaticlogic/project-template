# {PROJECT_NAME}

{ONE_SENTENCE_PURPOSE}

> Replace bracketed placeholders before inviting contributors or shipping a release.

## Project profile

- Stage: {DISCOVERY | MVP | DEVELOPMENT | STAGING | PRODUCTION}
- Users: {PRIMARY_USERS}
- Success criteria: {MEASURABLE_OUTCOME}
- Architecture: see [PROJECT.md](PROJECT.md)
- Agent working rules: see [AGENTS.md](AGENTS.md)

## Quick start

```sh
# Set up your actual dependencies and commands here.
# Never leave invented install, test, or deployment commands in published documentation.
```

## Working agreements

- Source-of-truth ownership and approval boundaries live in `PROJECT.md`.
- Repository-specific agent instructions live in `AGENTS.md`.
- PRs must report what changed, what was verified, what was not checked, and risks.
- Test selection should match risk and affected behavior. Avoid both unnecessary full suites and unsafe omissions.
- When resuming across sessions, start from Git/Issues/PRs/CI/Specs; chat memory is not the release log.

## Template setup

1. Replace all example placeholders in README, PROJECT.md and AGENTS.md.
2. Record the real code/toolchain, build commands, data contracts and deployment environments.
3. Choose a tracker (GitHub Issues, local tracked specs, etc.) and record which artifacts it owns.
4. Add stack-specific CI only when your runtime/toolchain is known. Do not assume .NET, Go or frontend defaults.
5. Configure review requirements, required checks, and secret management through repository settings.
6. Mark the repository as a GitHub Template using **Settings → General → Template repository** (requires administration privileges).
7. Remove template-only instructions as the project becomes operational.

This starter has **no product build or deployment jobs**. Its lightweight workflow checks only baseline file structure.
