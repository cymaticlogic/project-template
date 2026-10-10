# Project Operating Contract

## Identity
- Project name: {PROJECT_NAME}
- Purpose: {PROBLEM_AND_VALUE}
- Users: {USERS}
- Phase: {CURRENT_PHASE}
- Acceptance / success criteria: {VERIFIABLE_CRITERIA}
- Non-goals: {EXCLUDED_SCOPE}

## Architecture
- Stack and versions: {VERIFY_FROM_SOURCE}
- Major modules and dependencies: {MODULES_AND_EXTERNAL_CONTRACTS}
- DB / API / event contracts: {LINKS}
- Development commands: {REAL_COMMANDS}
- Deployment environments: {REAL_ENVIRONMENTS}

## Sources of truth
Specify ownership (do not assume every project uses one tracker):
- Product and domain decisions: {ACCEPTED_SPECS_LOCATION}
- Current implementation: {REPO_CODE_AND_SCHEMA}
- Active work and approvals: {ISSUES_OR_LOCAL_TRACKER}
- CI and release status: {WORKFLOWS_AND_DEPLOY_RECORDS}
- Architecture decisions: {ADR_OR_SPEC_LOCATION}

## Constraints / risks
- Technical and product constraints: {CONSTRAINTS}
- Current known risks: {RISKS}
- Rollback / backup assumptions: {VERIFIED_RECOVERY}

## Authorization
- Autonomous changes: {ALLOWED_LOW_RISK_SCOPE}
- Explicit approval required: {PRODUCTION_DELETION_SECRETS_IRREVERSIBLE_ACTIONS}
- Forbidden operations: {PROHIBITED_ACTIONS}

## Collaboration and handoff
- Work in bounded steps: inspect, change, validate, review, record.
- Keep actual commit, PR, CI and accepted decisions as the durable record.
- Use `docs/handoff.md` as an optional session handoff format; never mistake a stale handoff for live state.
