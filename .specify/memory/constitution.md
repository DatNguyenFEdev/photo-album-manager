<!--
  Sync Impact Report
  ==================
  Version change: (template) → v1.0.0
  Modified principles: N/A (initial population)
    - PRINCIPLE_1: (template) → "I. Code Quality"
    - PRINCIPLE_2: (template) → "II. Testing Standards"
    - PRINCIPLE_3: (template) → "III. User Experience Consistency"
    - PRINCIPLE_4: (template) → "IV. Performance Requirements"
    - PRINCIPLE_5: (template) → "V. Simplicity & Maintainability"
  Added sections:
    - Principle I (Code Quality)
    - Principle II (Testing Standards)
    - Principle III (User Experience Consistency)
    - Principle IV (Performance Requirements)
    - Principle V (Simplicity & Maintainability)
    - Security & Compliance (Section 2)
    - Development Workflow (Section 3)
    - Governance rules
  Removed sections: N/A
  Templates requiring updates:
    - ✅ .specify/templates/plan-template.md (no changes needed)
    - ✅ .specify/templates/spec-template.md (no changes needed)
    - ✅ .specify/templates/tasks-template.md (no changes needed)
    - ✅ .specify/templates/checklist-template.md (no changes needed)
    - ✅ .opencode/commands/speckit.constitution.md (no changes needed)
  Follow-up TODOs:
    - TODO(RATIFICATION_DATE): Original adoption date unknown. Set when first ratified.
-->

# UV My Project Constitution

## Core Principles

### I. Code Quality
All production code MUST pass automated linting and type checking before
commit. Linters, formatters, and type checkers MUST be configured in the
project and run as part of CI. Every function MUST have a single
responsibility; functions exceeding 50 lines SHOULD be refactored.
Duplicate code MUST be extracted into shared utilities. Code review is
MANDATORY for all merges to main — every review MUST verify compliance
with this principle.

### II. Testing Standards
Tests MUST be written for every feature and bug fix. The test pyramid
SHALL be followed: many unit tests, fewer integration tests, few
end-to-end tests. Unit tests MUST cover all edge cases and error paths.
Tests MUST be deterministic — no flaky tests are tolerated. CI MUST
fail on test failure. Test coverage MUST never regress; coverage gates
SHOULD be enforced in CI. Tests are first-class code: they MUST be
maintained, reviewed, and kept fast.

### III. User Experience Consistency
All user-facing interfaces MUST follow the same design language,
terminology, and interaction patterns. Error messages MUST be
human-readable, actionable, and consistent in tone and format.
Console/CLI output MUST use a uniform structure. Accessibility is
MANDATORY: all interfaces MUST support keyboard navigation and screen
readers where applicable. Every user-facing change MUST include a
before/after assessment of UX impact in the spec.

### IV. Performance Requirements
Every feature MUST define measurable performance budgets in its spec
before implementation begins. Latency, throughput, and resource
consumption MUST be tested and reported in CI. Performance regressions
MUST block merges. Optimizations MUST be justified by data, never by
intuition. Critical paths MUST be identified and benchmarked.
Profiling tools MUST be used before optimisation to ensure effort is
directed at actual bottlenecks.

### V. Simplicity & Maintainability
The simplest solution that meets requirements MUST be preferred (YAGNI).
Dependencies MUST be justified and kept minimal — every third-party
dependency requires explicit rationale in the spec. Dead code MUST be
removed; commented-out code MUST NOT be committed. Modules MUST have
clear boundaries documented by their public API. Refactoring for clarity
is PRIORITISED over adding new features when technical debt is
identified.

## Security & Compliance

All secrets MUST be managed through environment variables or a secrets
manager — never hard-coded. Input validation MUST be applied at every
trust boundary. Data at rest MUST be encrypted; data in transit MUST use
TLS. Dependencies MUST be scanned for known vulnerabilities in CI.
Compliance with applicable regulations (e.g., GDPR, SOC 2) MUST be
verified before production release. Security review is MANDATORY for any
change that handles sensitive data.

## Development Workflow

All changes MUST be developed on feature branches and merged via pull
request. Every PR MUST include a reference to the corresponding issue or
spec. CI MUST pass before merge. Commit messages MUST follow the
Conventional Commits format. The main branch MUST be deployable at all
times. Breaking changes MUST be communicated in advance and follow a
deprecation window policy defined per project.

## Governance

This constitution defines non-negotiable rules for the project. Any
amendment requires a documented proposal, team review, and consensus
approval. Amendments MUST be recorded here with version increment.
Compliance MUST be verified during code review and CI. Violations
SHOULD be flagged and tracked as tech-debt items. The constitution
supersedes all other local practices.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): original
adoption date unknown | **Last Amended**: 2026-06-30
