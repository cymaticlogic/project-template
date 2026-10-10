# Repository Agent Contract

Read `PROJECT.md` and relevant code/config/accepted specs before making a change. Replace placeholders and adapt this file to the actual stack.

## Work mode
- For small, clear tasks: Inspect → Implement → Targeted Validate.
- For complex or ambiguous tasks: Requirement Alignment → Plan/Spec → Small PRs.
- Carry out multiple bounded, recoverable loops when tools and authorization permit.
- During CI waits, progress only independent work that cannot interfere with a pending build.
- Ask only when uncertainty impacts security, correctness, cost, irreversible operations or core requirements.

## Constraints
- Preserve current architecture, module boundaries, versions, contracts and unrelated work.
- Use existing dependencies, formatting and test runners.
- Do not invent schema, API methods, config values or successful executions.
- Do not perform unrequested infrastructure modifications, broad refactors or dependency upgrades.

## Validation
- Documentation: relevant structure, link and content checks.
- Localized code: affected unit/type/static checks.
- API/contracts/shared components: relevant integration/regression validation.
- Database/security/deployment: expanded risk-based validation and recovery plan.
- Never disable required tests, branch protections or security checks to get green.

## Git & delivery
- Use the issue/work tracking convention defined in PROJECT.md.
- Respect repository branch protection, code review and deployment policies.
- Do not merge or deploy without the project-specific authorization.
- Do not commit credentials, production secrets, sensitive customer data or internal inventories.
- Report Changed, Verified, Not Verified, Remaining Risks and Evidence.

## Project-specific commands and boundaries
- Build: {BUILD_COMMAND}
- Targeted test: {TARGETED_TEST_COMMAND}
- Lint/typecheck: {STATIC_CHECK_COMMAND}
- Deployment/rollback: {POLICY_REFERENCE}
- Mandatory approval gates: {APPROVAL_POLICY}
- Forbidden changes: {FORBIDDEN}

Never execute a placeholder command.
