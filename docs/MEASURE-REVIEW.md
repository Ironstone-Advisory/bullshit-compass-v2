# Review of the twelve measures

Review 1.0 · 31 October 2026

Status: design audit by OpenAI Codex with Rob Tyrie's direction. This is not an
independent expert review, reliability study or empirical validation. It compares
the current prompt (1.1), extension and Python baseline and identifies what to
test or clarify before treating the software as a semantic reviewer.

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

## Priority clarifications before a frozen semantic pilot

These are proposed clarifications, not silent edits to prompt 1.1. An executor
must select and archive the actual rubric used for a run. Keep 1.1 as a baseline
if testing a revised prompt against it.

1. **TCR versus the original Peterson-derived construct.** Test circular support
   and unsupported argumentative additions separately before testing their joint
   occurrence. PWI is not just exact repetition; ISI is a later generalization.
   The four PWI cases in the pilot vary the two proposed components independently.
   Assess whether their interaction adds a useful diagnosis without inventing a
   thirteenth dimension. Distinct defects can have linked findings; one defect
   should not become multiple independent counts through secondary tags.
2. **DPO/EA wording.** The current DPO checklist includes causal claims drawn from
   correlation, while the overlap rule assigns unsupported inference to EA.
   Proposed clarification: DPO owns representation of data; EA owns what is
   inferred from it. Apply one primary tag per underlying defect.
3. **Concern anchors across all dimensions.** Prompt 1.1's Moderate anchor says
   "recurring or material ambiguity," which is narrower than EA/DC/RR and several
   other dimensions. Proposed wording: a recurring or material limitation that
   requires clarification or repair before reliance. Keep centrality, severity
   and prevalence distinct; do not penalize length alone.
4. **Applicability versus inability to assess.** The current display label Not
   assessable covers both. Preserve an explicit reason such as not applicable,
   missing context, inaccessible material or unsupported capability. Report these
   separately in evaluation counts; none is a clean result.
5. **Evidence and rewrite requirements.** A flag must identify the problem and
   survive its strongest reasonable alternative reading. A repair must preserve
   uncertainty and must not invent facts to make a passage appear concrete.

## What is already checked

The existing twelve baseline regression tests pass on the unchanged code used
for this update. A separate [lexical diagnostic run](../evaluation/lexical-diagnostic-run.json)
records concrete limitations. It is a demonstration, not a semantic benchmark.

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

The [36 authored pilot cases](../evaluation/pilot-cases.json) cover all twelve
dimensions, boundary conditions and the original Peterson-derived construct.
Their expected outcomes are provisional design hypotheses. Independent reviewers
must establish reference judgments; cases created during development are not a
held-out dataset. See the [test plan](TEST-PLAN.md) for execution and reporting.

© 2026 Ironstone Advisory. Original review: CC BY 4.0.
