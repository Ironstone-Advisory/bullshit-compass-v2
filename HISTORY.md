# History

*By Rob Tyrie, Ironstone Advisory.*

This is **version 2** of the Bullshit Compass, the active line of work. Version 1 lives at [Ironstone-Advisory/BullshitCompass](https://github.com/Ironstone-Advisory/BullshitCompass) and preserves the earlier repository record.

## Conceptual development and early experiments

Expanded on 31 October 2026. The [evidence ledger](history/provenance/2026-10-31-conversation-reconstruction.md)
distinguishes author recollections, recovered conversations and inspectable
artifacts. P-IDs are local ledger IDs, not original conversation identifiers.
Conversation dates use the UTC timestamps returned by retrieval; a Toronto date
can be the previous day.

| When | Milestone | Evidence |
|---|---|---|
| 2022 | Rob reports beginning development of the idea. | P01: author recollection; contemporaneous artifact not yet recovered. |
| Jun 12, 2023 | Discussion of Frankfurt, Grice and relevance; Pennycook et al.'s research introduced after Rob asks about jargon without meaning. He then asks for a mechanism to assess substance in scientific papers. | P02: recovered user excerpts and assistant response; an early design question, not proof of the later Compass name. |
| Jun 29, 2023 | Rob explores Frankfurtian bullshit and "simulo-reality," requesting anti-bullshit tests. | P03: recovered conversation summary. |
| 2024 | Rob reports making a first version. | P01: author recollection; complete first-version artifact not yet recovered. |
| Sep 11, 2024 | A "Frankfurt 'Bullshit Meter' Analysis" reviews eleven newsletter items. | P04: recovered assistant output; a practical review experiment, not a verified software release or the complete first version. |
| Mar 30, 2025 | Rob requests combined Frankfurt/Pennycook analysis, explores an index and explicitly names "The Bullshit Compass." | P05: earliest explicit naming recovered in this search; not a claim of first-ever use. |
| Apr 5, 2025 | Rob requests a Pennycook-Frankfurt lens, then systems-design and accounting/financial analysis; a related prompt request includes Graeber. | P06: recovered user-message summaries. |
| Apr 6–7, 2025 | Applied Compass reviews; Rob challenges missing workforce-transition, regulatory and downside context. | P07: recovered conversation summaries; the connection to today's Decision Completeness dimension is retrospective. |
| Recorded Oct 31, 2026; concerns v1 design | Rob clarifies that the Peterson-derived measure originated in his own observations of tautology in argument and exposition, independently of the cited thinkers' measures. | P11: author attribution, with TCR/PWI/ISI terminology anchored in archived specifications. |

See [Background and provenance](docs/BACKGROUND-AND-PROVENANCE.md) for the distinction
between original project contributions and intellectual influences.

## Repository and specification lineage

| When | What | Where |
|---|---|---|
| Apr 2025 | White paper v0.1, "Semantic Pattern Detection and the Bullshit Compass Framework": seven core indicators plus LGC, then presented as an eighth indicator. Archive filename uses Apr 1; heading says April 2025. | [history/v1-2025-04](history/v1-2025-04/2025-04-01-white-paper-v0.1.md), P08 |
| Apr 1, 2025 | Finger Spider project summary: the Fingerprint Spider (RFC FS01, semantic reuse) and the Bullshit Compass (RFC FS02, epistemic quality) as two tools on one platform | [history/v1-2025-04](history/v1-2025-04/2025-04-01-finger-spider-project-summary.md) |
| Apr 1, 2025, as dated in drafts | RFC FS02 iterations develop the indicators and contextual layer. Draft/version labels coexist; they are not all verified software releases. PWI is refined into ISI; the Graeber-focused draft treats work structures as context, not a detection target. | `spec`, `spec-original`, the v0.88 PDF, and [Graeber-focused draft](history/v1-2025-04/2025-04-01-rfc-fs02-v0.88.02-graeber-cultural-emphasis.md), P09/P11 |
| Apr 1, 2025 | Use cases and dashboard designs | `usecases`, `DashboardDesigns` |
| Apr 9, 2025 | Reference code: a Python scorer for tautology, jargon density, vagueness, "Peterson weakness" and semantic emptiness | `code` |
| Sep 20, 2026 | v2 started as a copy of v1 | this repo |
| Oct 17, 2026 | v1's commit history merged into v2 so `git log` and `git blame` reach back to April 2025; first calibration run of the v1 code | [CALIBRATION.md](CALIBRATION.md) |
| Oct 31, 2026 | Corrected lexical baseline and twelve-dimension qualitative prompt: original nine plus EA, DC and RR; LGC remains the context layer. | [Baseline report](V2-CALIBRATION.md), [extension](docs/FS02-v2-extension.md), [prompt](prompts/bullshit-compass-master-prompt.txt), P10 |
| Oct 31, 2026 | Background, original-contribution attribution, evidence ledger, twelve-measure design audit and test plan documented; 36 authored development cases and a lexical diagnostic run added. Semantic evaluation remains pending. | [Background](docs/BACKGROUND-AND-PROVENANCE.md), [test plan](docs/TEST-PLAN.md), [traceability](docs/EVALUATION-AND-TRACEABILITY.md) |
| Oct 31, 2026 | Prompt 1.2 and extension 1.1 implement the first four audit clarifications: circular support/additions, DPO/EA ownership, broader Moderate concern and explicit non-assessment reasons. Dataset 1.1 adds eight boundary cases (44 total); the baseline adds reason fields and two regression tests (14 total), with scoring unchanged. Semantic evaluation remains pending. | [Measure review](docs/MEASURE-REVIEW.md), [prompt](prompts/bullshit-compass-master-prompt.txt), [pilot cases](evaluation/pilot-cases.json) |

The code, use-case and repository-transition dates above are retained from the
earlier HISTORY.md; document dates and Git dates are distinct evidence.

Preserve historical RFCs, `code` and archived documents as records of their time.
Maintain current guidance in the README and new v2 documents. Earlier scoring and
capability claims are not evidence of present implementation or established
accuracy. A dated provenance addendum in v1 can clarify earlier work without
importing v2's later features into the historical specification.

The 2022 and first-version 2024 dates remain attributed to Rob's account. The
retrieved 2023–2024 material supports earlier inquiry and experimentation without
establishing the complete sequence or historical priority over other projects.
Missing retrieval is not proof that an earlier record does not exist.

