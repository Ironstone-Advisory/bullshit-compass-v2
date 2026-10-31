# Review of the twelve measures

Review 1.1 · 31 October 2026

Status: design audit by OpenAI Codex with Rob Tyrie's direction. This is not an
independent expert review, reliability study or empirical validation. It compares
the prompt, extension and Python baseline. The initial audit examined prompt
1.1; this revision records the four clarifications implemented in prompt 1.2.
Semantic accuracy still needs independent evaluation.

## Overall finding

The dimensions are useful candidate review questions, but are not twelve validated
measurements. Several overlap. Their unit of analysis should be an **identified
textual or reasoning defect with located evidence**, not a word count or an
author's presumed intention. Concern labels are ordinal judgments; confidence
reflects evidence/access. Neither is a probability that an author is bullshitting.

Historical names containing Rate, Ratio, Index or Score do not supply a denominator
or a validated scale. Retain identifiers for compatibility, but display plain
dimension names and qualitative judgments. Any future quantitative measure needs
a defined construct, unit, denominator, aggregation rule and validation evidence.

## Dimension audit

The entry in the last column describes current software, not the prompt's scope.

| Dimension | Observable question | Boundary to double-check | Python baseline |
|---|---|---|---|
| TCR | Does the offered reason add support beyond restating the conclusion? | Reconstruct premise and conclusion; separate circular explanation from definitions, emphasis, topical similarity and literal repetition. | Adjacent exact-repetition proxy only; not semantic tautology. |
| ISI | What unstated, contestable premise is needed for this inference? | State the missing premise; an openly declared value is not smuggling. Distinguish premise insertion from ordinary evidence weakness (EA). | Not assessed. |
| SDS | Does a key definition, scope or evidential standard change without explanation? | Compare both locations; development of an argument is not drift. RR concerns an external question. | Not assessed. |
| AAR | Can the intended reader determine the claim or commitment? | Identify the consequential ambiguity; uncertainty, qualitative meaning and unstated irrelevant details are not failures. | Small vague-phrase dictionary. |
| BLI | Does a term substitute for explanation that this audience needs? | Jargon frequency alone is insufficient. Definitions and legitimate specialist use must resolve false alarms. | Jargon-phrase dictionary; contextual allowlist only. |
| PRM | Is scientific terminology or authority doing unjustified argumentative work? | Identify the claimed scientific connection. Missing evidence belongs primarily to EA unless scientific rhetoric itself is the mechanism; technical uncertainty may require expert review. | Not assessed. |
| EPF | Does emotional pressure replace reasons or discourage scrutiny? | Quote the substitution or pressure. Emotion, persuasion and justified urgency alone are not defects. | Not assessed. |
| OOI | What actor, action or consequence becomes harder to understand? | Demonstrate lost meaning, not merely passive voice, a long sentence or a disliked metaphor. AAR concerns unclear commitments; BLI concerns unexplained terms. | Not assessed. |
| DPO | Is quantitative information represented in a misleading or incorrect way? | Check denominators, units, baselines and comparisons. Keep the inferential step to a causal claim under EA; do not count it twice. | Not assessed. |
| EA | Does the available support justify the claim's scope and strength? | Identify claim and source separately. Unsupported, inaccessible and contradicted are different states; factual truth is a separate question. | Not assessed. |
| DC | What information material to this stated decision is missing from the reviewed scope? | Explain the consequence of the omission. Review appendices, respect the decision stage and avoid a universal checklist. | Not assessed. |
| RR | Does the response address the actual question, brief or stated purpose? | Preserve the reference question; explicit unknowns, justified refusals and false-premise corrections can be responsive. | Not assessed. |

LGC is the interpretation layer, not an additional scored dimension. It should
record genre, audience, purpose, domain and access limits before applying these
questions. Appropriate technical prose and culturally unfamiliar wording are
essential non-finding cases.

## Four clarifications implemented; semantic testing pending

Prompt 1.2 and extension 1.1 implement items 1–4 from the initial audit.
Prompt 1.1 remains in Git history at `ca621d707c85dbc06e771cfaa6317cb2bafac603`.
Select and archive the actual rubric used for each run; do not relabel earlier
outputs as if they used these rules.

1. **Repetition, circular support and argumentative additions.** TCR requires an
   identified premise/conclusion dependency, not repeated wording. Test circular
   support and unsupported additions independently and together. Assign an
   unstated contestable premise to ISI and an explicit claim beyond its support
   to EA. Open values and useful emphasis are not defects by themselves. This
   operationalizes Rob's original Peterson-derived contribution while retaining
   PWI as historical terminology; it neither adds a thirteenth dimension nor
   proves the usefulness of a combined measure.
2. **DPO/EA boundary.** Removed causal claims from the DPO checklist. DPO owns
   quantitative representation; EA owns inference, including causal overreach
   with correctly presented numbers. One causal leap gets one finding. A wrong
   percentage-point claim and an independently unsupported causal conclusion
   can be two linked defects with distinct repairs.
3. **Concern anchors.** Moderate now covers a recurring or material limitation
   in meaning, reasoning, evidence, decision completeness or responsiveness that
   requires clarification or repair before reliance. It is no longer restricted
   to ambiguity. Centrality, severity and prevalence guide the judgment; length
   alone does not. These remain provisional qualitative anchors.
4. **Non-assessment reasons.** Keep the display label Not assessable, but require
   `not_applicable`, `insufficient_context`, `inaccessible_material` or
   `unsupported_capability` and a concrete explanation. Inapplicability requires
   enough context to establish it. Report reasons separately in evaluation;
   none is a clean result or zero. Partial access must not erase supported
   findings or turn inaccessible evidence into a confirmed omission. The Python
   baseline now distinguishes empty input from its missing semantic capability
   through additive reason fields; it does not infer applicability.

The existing fifth audit requirement remains: a flag must survive its strongest
reasonable alternative reading, and a repair must preserve uncertainty without
inventing facts. The full reason-code definitions and concern anchors are in the
[extension](FS02-v2-extension.md) and the self-contained master prompt.

| Change | Authored semantic cases or software checks |
|---|---|
| Separate the original construct's components | TCR-P/N, ISI-P/N, four PWI factorial cases, CLAR-REPETITION and CLAR-EXPLICIT-ADDITION |
| Resolve DPO/EA overlap | DPO-P/N, EA-P/N, CLAR-CAUSAL and CLAR-TWO-DEFECTS |
| Broaden Moderate | CLAR-MODERATE-EA proposes an evidence-gap anchor without ambiguity; reviewers must independently judge severity |
| Distinguish non-assessment reasons | Three existing access/purpose controls, CLAR-NO-QUANTITIES, CLAR-APPENDIX and CLAR-DECISION-CONTEXT; software regression checks for empty input versus unsupported capability |

These mappings describe prepared coverage. Semantic cases have not yet been
executed against independently established reference judgments.

## What is already checked

Fourteen baseline regression tests pass after this revision, including two new
checks for reason reporting and repetition/semantic capability separation.
Lexical scoring is unchanged. The earlier twelve-test result and the separate
[lexical diagnostic run](../evaluation/lexical-diagnostic-run.json) remain
historical evidence from the prior baseline. That run records concrete
limitations; it is a demonstration, not a semantic benchmark.

| Diagnostic | Observed baseline output | Implication |
|---|---|---|
| Circular explanation, TCR-P | TCR repetition proxy 0; lexical warning 0 | The baseline does not detect this authored semantic circularity. |
| Clear finance definition, BLI-N | BLI lexical coverage about 0.095; warning intensity about 0.238 | Legitimate uses of "leverage" are counted; context is needed before making a substantive finding. |
| Vague commitment, AAR-P | AAR lexical proxy 0; warning intensity 0 | Ambiguity outside the short phrase dictionary is missed. |
| Unsupported generalization, EA-P | EA remains `not_assessed` | The baseline correctly discloses its missing semantic capability. |
| Exact repetition of a clear statement | TCR repetition proxy 1; overall lexical warning 0 | Repetition detection is distinct from evaluating circular reasoning. |

These outcomes are consistent with the code's disclosed limitations. They do
not justify treating a lexical zero as a clean semantic review or a dictionary
match as a confirmed substantive defect.

The [44 authored pilot cases](../evaluation/pilot-cases.json), dataset 1.1, cover all twelve
dimensions, boundary conditions and the original Peterson-derived construct.
Their expected outcomes are provisional design hypotheses. Independent reviewers
must establish reference judgments; cases created during development are not a
held-out dataset. See the [test plan](TEST-PLAN.md) for execution and reporting.

© 2026 Ironstone Advisory. Original review: CC BY 4.0.
