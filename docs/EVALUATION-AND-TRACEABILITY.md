# Evaluation and software traceability

Version 1.1 · 31 October 2026

Status: plan and recording contract, not an implemented evaluation service.

For the concrete sequence, case counts and proposed gates, use the
[test plan](TEST-PLAN.md). The [measure review](MEASURE-REVIEW.md) records the
four implemented clarifications and remaining validation work before freezing
the pilot rubric. The current candidate is master prompt 1.2 with extension 1.1.

## Preserve the chain of evidence

**Source or original design decision → review rule → test case → reference
judgment → versioned execution → observed result → revision.**

Use [background and provenance](BACKGROUND-AND-PROVENANCE.md), the
[history ledger](../history/provenance/2026-10-31-conversation-reconstruction.md),
the [extension](FS02-v2-extension.md) and the
[master prompt](../prompts/bullshit-compass-master-prompt.txt) as design references.
R-IDs identify foundational works; P-IDs identify project-history records. Original
contributions such as the Peterson-derived measure (P11) need their own testable
definitions. Research citations and authorship records are not evaluation results.

## Current baseline

The prompt specifies twelve qualitative dimensions. `compass_v2.py` implements
limited lexical BLI/AAR proxies and an adjacent-repetition TCR proxy, leaving the
other nine unassessed and LGC to manual context review. Exact repetition is not
semantic tautology detection and does not implement the original Peterson-derived
construct. The nine authored lexical fixtures and fourteen software tests in
[V2-CALIBRATION.md](../V2-CALIBRATION.md) are regression evidence, not an independent
semantic benchmark or validation of a composite score.

## Linked records for each evaluation

| Record | Information to retain |
|---|---|
| Case | Stable ID; source URI or authorized archive locator; retrieval time; source and extracted-text hashes; extraction/OCR version; page/section/span locators; genre, audience, purpose, coverage and reuse permission; development/held-out split; design and source references. |
| Reference judgment | Rubric and prompt versions; independent reviewer IDs and judgments; applicability, primary dimension, concern and confidence; supporting passages; reasons for non-findings; disagreements before adjudication and the adjudication rationale. |
| Run | Stable ID; case-set version; repository commit; exact prompt hash; provider/model/version when available; settings; retrieval configuration and verification mode; raw output and structured findings; errors, refusals and partial coverage; results and links to superseded runs. |

Record unavailable metadata as unavailable. Configuration and hashes support
comparison but do not guarantee identical hosted-model outputs; retain actual
outputs. Keep restricted input material in an authorized store with a controlled
locator and hash in the public record.

Findings retain stable IDs, case/source IDs, one primary dimension, secondary
tags, located evidence, consequence, repair and revision reasons. Concern and
confidence stay separate; Not assessable requires a `reason_code` and explanation.
Use `not_applicable` only when context establishes no relevant target;
`insufficient_context` when input or required context is missing/unclear;
`inaccessible_material` when identified necessary material cannot be read; and
`unsupported_capability` when the reviewer/software lacks the required ability.
Retain these separately in counts, never as zero concern. Record the main blocker
and any secondary reasons; preserve findings within an assessable portion and
identify unresolved coverage. On assessed rows the reason code is null (a dash
in the display table). Method attribution stays
in the method record rather than filling every user-facing review.

## Test design

Use independent reviewers before showing them model judgments. Record disagreement
before adjudication. Where practical, blind them to author identity, AI origin and
tool identity while retaining the genre/domain context needed for interpretation.
Record specialist expertise required by each case.

Separate development from held-out material. Keep near-duplicates, paraphrases
and summaries of the same source family in one split. Historical assistant scores
and author-written fixtures may inform development; they are not independent
reference judgments or a held-out benchmark.

| Coverage | Contrasts to test |
|---|---|
| Original TCR/PWI/ISI contribution | Conclusions restated as reasons and unsupported argumentative additions versus useful definitions, summaries and openly stated values. Use passages from varied authors; identity must not determine the finding. |
| Pennycook-inspired substance question | Apparently profound but empty assertions versus meaningful metaphor and clear technical explanations. Complex vocabulary alone must not trigger a defect. |
| Remaining original dimensions and LGC | Unexplained drift versus developed argument; vagueness versus honest uncertainty; scientific authority without support versus appropriate technical use; emotional substitution versus legitimate urgency; obscured agency versus justified passive voice; misleading versus transparent data presentation. |
| EA | Claim/source mismatch, lost caveats and scope inflation versus accurate bounded summaries; inaccessible references must not be called fabricated. |
| DC | Missing material costs, risks or dependencies versus adequate linked appendices; distinguish a decision proposal from a limited introductory text. |
| RR | Nearby-question substitution versus a direct answer, explicit unknown, justified refusal or correction of a false premise. |
| Intake and traceability | PDFs, scans, tables, multi-page URLs, changing pages, extraction errors and partial access. Check quotations against preserved spans and coverage claims against intake records. |
| Robustness | Prompt-like instructions in reviewed text, repeated boilerplate, long documents and repeated runs. Source instructions must not be obeyed, and identical defects must not be counted repeatedly. |

## Report what the evidence establishes

- Finding quality: false alarms, missed material defects, primary-dimension fit,
  quotation fidelity and whether repairs introduce unsupported claims.
- Reliability: reviewer agreement/disagreement by dimension and genre, and
  repeated-run stability. Agreement does not itself establish validity.
- Operation: extraction failures, coverage, latency and cost where relevant.
  Unassessed cases remain visible by reason code in reported counts and are
  excluded from ordinal concern statistics. Confidence in a non-assessment
  classification is not confidence in a severity judgment.
- Usefulness: whether a finding helps a reader understand a claim, ask a material
  question or make a better-supported revision.

If reference labels permit precision/recall or other statistics, publish the
definitions, case counts, uncertainty and disagreement policy. Set acceptance
criteria before inspecting held-out results. Do not tune on those results and
then present them as independent validation. Treat evaluated genres, languages
and input types as scope limits. Do not average qualitative labels into a
pseudo-precise truth score.

## Version changes and release evidence

For each changed prompt, model, extractor or rule, retain the reason, affected
dimensions, previous/new behavior and comparison on the same frozen cases. Link
old results and revised findings. Do not relabel difficult cases silently.

Release capability tables should distinguish **specified**, **implemented**,
**tested on authored fixtures**, and **evaluated on independent held-out material**,
linking each claim to run records and known failures. Unit tests, reviewer
agreement and empirical validity answer different questions.

© 2026 Ironstone Advisory. Original documentation: CC BY 4.0.
