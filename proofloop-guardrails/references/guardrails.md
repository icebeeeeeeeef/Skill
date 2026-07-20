# Portable guardrails

### PLG-001 — Verify APIs against the repository's dependency version

- Trigger: A task, implementation, test, example, or review uses a dependency API, and the repository pins or otherwise constrains that dependency's version.
- Failure: The agent copies current or latest documentation, relies on memory, or selects an API without establishing that it exists with the repository's actual version and configuration.
- Required action: Resolve the effective version from the repository's manifest, lockfile, vendored source, or build environment; then verify the used API against primary documentation or source for that version. Prefer an existing repository usage pattern when it represents the same contract.
- Evidence: Cite the repository version source and the version-matched API definition, documentation, existing compiled usage, or a focused probe executed in the repository environment.
- Exceptions: Skip external verification when the API is defined in repository-owned source already inspected, or when a deterministic build/type-check/test directly proves availability for the pinned environment. Do not require adopting a newer version.
