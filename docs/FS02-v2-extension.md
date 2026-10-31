# Bullshit Compass v2: three additional qualitative dimensions

Version 1.0 · 31 October 2026  
Framework: Rob Tyrie / Ironstone Advisory / Finger Spider Project  
Research synthesis and drafting: Rob Tyrie with OpenAI Codex

For the original project contributions and the Frankfurt, Pennycook and Graeber
influences, see [Background and provenance](BACKGROUND-AND-PROVENANCE.md).
The [development ledger](../history/provenance/2026-10-31-conversation-reconstruction.md)
separates author accounts, recovered conversations and repository artifacts.
The [evaluation plan](EVALUATION-AND-TRACEABILITY.md) connects future tests and
software versions to design rules and observed results.

## Decision and scope

Extend the nine-indicator RFC FS02 profile with **Evidence Alignment (EA)**,
**Decision Completeness (DC)** and **Response Relevance (RR)**. The profile now
contains twelve dimensions. Language Game Contextualization (LGC) remains a
contextual interpretation layer, not a thirteenth scored dimension.

This document is a v2 extension to the inherited `spec-original`, not a rewrite
of the historical RFCs. It governs the three additions and their boundaries with
the earlier nine. The executable review instructions are in
[the master prompt](../prompts/bullshit-compass-master-prompt.txt), version 1.1.

These are qualitative judgments supported by passages, source locations and
explicit reasons. A finding describes a limitation of the reviewed material; it
does not establish the author's intent or character. In the profile, **concern**
means a gap in alignment, completeness or relevance. A higher concern level does
not mean greater alignment, completeness or relevance.

## Why we synthesized these three

The existing nine examine circularity, hidden premises, drift, ambiguity, jargon,
scientific rhetoric, emotional appeals, obfuscation and data presentation. They
can identify ways language conceals or weakens meaning. They do not give equal
prominence to three relationships that a reader needs to inspect:

| Relationship | Review question | Addition |
|---|---|---|
| Claim to supporting material | Does this evidence justify this claim? | EA |
| Recommendation to decision | Is the relevant information present to evaluate this choice? | DC |
| Answer to question or stated purpose | Does this response address what was asked or promised? | RR |

A sentence can be precise yet cite irrelevant evidence. A proposal can be clear
yet omit the cost that determines whether it is viable. An answer can be eloquent
yet leave the question unresolved. These are distinct defects even when the prose
has little jargon or ambiguity.

We selected three broad relationships rather than promoting every adjacent
research phenomenon into another dimension. Causal overreach, certainty
inflation, misleading implication and citation amplification can be diagnosed
within these relationships. This keeps the framework usable and limits duplicate
counting. It does not claim that the dimensions are statistically independent.

## How the synthesis was made

1. **Identify an observable pattern.** Use research on citation distortion,
   reporting spin, decision-information quality and question evasion.
2. **Separate observation from inferred intent.** Translate descriptions of
   misleading behavior into checks on text and available context. Do not diagnose
   a writer's motives or cognitive state.
3. **Define the comparison required.** EA needs a claim and its available support;
   DC needs a stated or clearly identified decision; RR needs a question or a
   documented communicative purpose. Record uncertainty when these are missing.
4. **Specify the evidence for a finding.** Cite both sides of the comparison, or
   identify a specific absent item, the reviewed scope, and why it matters.
5. **Apply LGC and counterexamples.** Adjust for genre, audience and purpose;
   distinguish legitimate scope limits from material omissions or evasions.
6. **Retain the research boundary.** Empirical support for a phenomenon, or testing
   of an instrument in one domain, does not validate this new twelve-dimension
   synthesis or its implementation by an LLM.

The names EA, DC and RR, their grouping, the review procedures below and their
integration into the Compass are our synthesis. They are not scales published
under those names by the cited researchers, and no endorsement is implied.

## 10. Evidence Alignment (EA)

**Definition:** The fit between the strength, scope and wording of a claim and
the support actually available in the reviewed material.

**Attribution.** Greenberg [1] traced how a particular scientific claim acquired
authority through selective citation, amplification and changes in what citations
were taken to establish. Boutron and colleagues [2] experimentally examined how
reporting spin affected clinicians' interpretation of trial abstracts. We
synthesize these into a general comparison between a claim and its support,
including changes in confidence as a claim moves into a summary.

**Procedure**

- Identify the exact claim, including population, period, outcome, conditions and
  strength of language. Separate observation, causal explanation and recommendation.
- Locate the evidence or reasoning offered for it. Inspect accessible cited
  material before declaring it irrelevant or misrepresented.
- Compare what the source establishes with what the text concludes. Check for
  broadened populations, changed outcomes, association described as causation,
  uncertainty removed, or preliminary evidence described as settled.
- Where multiple sources are offered, examine whether they provide independent
  support or merely repeat one origin. Do not infer dependence without tracing it.
- Record the discrepancy and what narrower claim the support would justify.

**Common flags:** citation mismatch; unsupported scope expansion; causal
overreach; certainty inflation; repeated assertion presented as corroboration;
and misleading implication contradicted by accessible supporting context.

**Boundaries and counterexamples:** A well-supported claim is not thereby proven
true. Observational research can support causal inference under appropriate
designs and assumptions; lack of randomization is not an automatic failure.
Transparent opinion, a stated hypothesis, a definition or an ordinary instruction
need not carry research citations. An inaccessible reference means its alignment
is not assessable, not that it fails. A clearly asserted empirical claim without
support can be flagged as unsupported *in the reviewed material*, not as false.

**Illustrative positive finding:** A page claims all companies will double
productivity, but its linked study concerns time saved on one task in one team.
Cite the claim and study limits; flag unsupported generalization.

**Illustrative non-finding:** A page accurately describes a small pilot, labels
the result preliminary and states that broader effects are unknown.

**Relationship to the nine:** DPO owns defects in how numbers or charts are
presented. EA owns the inferential step from evidence to conclusion. ISI owns an
unstated contestable premise. PRM owns inappropriate scientific rhetoric. One
finding can carry secondary tags without becoming several independent defects.

## 11. Decision Completeness (DC)

**Definition:** Whether the reviewed recommendation supplies the material context
needed by its intended audience to evaluate the stated decision.

**Attribution.** DISCERN, developed by Charnock, Shepperd, Needham and Gann [3],
was tested as a qualitative instrument for written consumer information about
treatment choices. Its questionnaire [4] addresses matters including sources,
uncertainty, benefits, risks and alternative choices. We adapt the principle of
decision-relevant completeness to business and other documents. We do not copy
its questionnaire or scoring system, and its validation does not transfer to this
adaptation. Reviewer agreement in the original research varied with experience.

**Procedure**

- Name the decision, audience and declared scope. If a decision is inferred,
  label the inference and lower confidence where appropriate.
- Identify only context material to that decision: benefits, costs, risks,
  alternatives, prerequisites, implementation burden, time horizon, uncertainty,
  failure conditions and, when relevant, maintaining the status quo.
- Check the reviewed sections and clearly signposted supporting pages for that
  context. Do not assume every detail belongs in the executive summary.
- For each omission, explain the consequence: what comparison, estimate or choice
  becomes unreliable or impossible without it?
- State the missing information as a clarification request. Do not invent it.

**Common flags:** benefits without relevant costs; recommendations without material
alternatives; savings without implementation assumptions; omitted dependencies;
and confident recommendations that conceal known limitations in the supplied text.

**Boundaries and counterexamples:** Completeness is relative to purpose, not an
exhaustive checklist. A short teaser, poem or descriptive page is not a full
investment case. Use Not assessable, with reason “not applicable to this purpose,”
when no decision is in scope. If access to a clearly linked appendix is blocked,
record an access limit rather than asserting that the author omitted its contents.
Do not label an omission intentional or claim knowledge of hidden facts.

**Illustrative positive finding:** A proposal supplies annual savings and asks for
purchase approval, but gives no implementation cost or effort. Explain that the
reader cannot assess payback from the reviewed material.

**Illustrative non-finding:** The summary links to a reviewed cost-and-risk appendix
that supplies the information needed for the stated decision.

**Relationship to the nine:** AAR concerns what an assertion means; DC concerns
whether enough relevant assertions are present. OOI can describe language hiding
a cost; DC records a missing cost only when material to the decision. If both
describe the same underlying defect, retain one finding with both tags.

## 12. Response Relevance (RR)

**Definition:** Whether the response addresses the explicit question, requirement
or communicative purpose established for it.

**Attribution.** Rogers and Norton [5] studied how listeners can miss answers to
similar but different questions, and how directing attention to the original
question can improve detection. We adapt this into an explicit comparison of the
question and answer. Its relationship to Gricean relevance is conceptual; the
experiment did not validate an automated document or chatbot classifier.

**Procedure**

- Preserve the actual question, brief, requirement or stated purpose and locate it.
  Keep it visible alongside the proposed answer. Do not invent a convenient
  question and then penalize the text for not answering it.
- Identify what a responsive answer would need to address at the requested level.
- Classify the response as direct, partial, explicitly deferred/declined, or
  substituted. Explain which requested element remains unanswered.
- Look for changes of subject, metric, time period or scope that leave the original
  request unresolved despite a plausible-sounding response.
- Credit a legitimate correction to a false premise, an appropriate refusal, or
  an explicit statement that the answer is unknown. Responsiveness does not
  require answering an unsafe, impossible or ill-posed question on its own terms.

**Common flags:** answering a nearby question; substituting process for a requested
outcome; reporting activity instead of a requested result; and changing the time
period to avoid addressing the period asked about.

**Illustrative positive finding:** “When will the service launch?” receives only
“Quality remains our highest priority.” The date or status of the date is absent.

**Illustrative non-finding:** “We cannot commit to a launch date until testing ends;
we will provide an update on Friday.” The uncertainty is explicit and relevant.

**Relationship to the nine:** SDS evaluates coherence within the text. RR compares
the text with an external question or its own stated purpose. A coherent answer
can still address the wrong question. Without a sufficiently clear reference
question or purpose, mark RR Not assessable.

## Shared reporting and overlap rules

Use the existing concern labels: None observed, Low, Moderate, High or Not
assessable. Report confidence separately and explain it. Do not average the
labels. Record an applicability reason when a dimension cannot be assessed.

Every finding needs a stable ID, a primary dimension, any secondary tags,
source location(s), the comparison or missing item, practical consequence,
strongest plausible alternative interpretation, and a repair or clarification.
This is concise supporting reasoning, not a request for hidden model deliberation.

| If the defect primarily concerns... | Primary dimension |
|---|---|
| What a sentence commits to | AAR |
| What its evidence justifies | EA |
| What a stated decision requires but the reviewed material lacks | DC |
| Whether the question was addressed | RR |
| How quantitative information is represented | DPO |
| An unexplained shift within the text | SDS |

Count each underlying defect once in the finding ledger. Secondary tags preserve
the links between dimensions without inflating the overall concern assessment.
Misleading implication is a description of the reading supported by context,
not a conclusion that the author deliberately paltered. Mechanism gaps may belong
under AAR, PRM or EA according to the actual defect; they are not an extra axis.

EA is available with external verification Off: compare the claim with supplied
evidence and accessible directly cited sources within scope. Independent searches
to establish real-world truth belong to the optional verification section. State
exactly which sources were checked. DC and RR similarly operate within declared
coverage and must not treat inaccessible content as absent content.

## Human and AI-created material

The twelve dimensions apply to human, AI-assisted, AI-generated and unknown-origin
articles, speeches/transcripts, documents, research, proposals and conversations.
Review the text on its merits regardless of provenance. Authorship is not an
input requirement or a review output and must not change the assessment. The
framework identifies text problems; it does not infer how the text was produced.

For any summary or derivative draft, compare against supplied originals or the brief:
identify unsupported additions, lost caveats, changed quantities, inconsistent
definitions and missed requirements. Attribute a source-fidelity finding to EA,
DPO, SDS or RR as appropriate. Without originals, source fidelity is not assessable.
For speeches, a transcript supports textual review but not conclusions about
delivery or audience impact.

Reference and quotation verification require accessible evidence. A broken link or
unsuccessful search does not prove a citation was fabricated. State what could and
could not be verified. Research-data fabrication and the validity of experiments
cannot be inferred from rhetorical patterns; reviewing those requires underlying
data, methods and appropriate expertise. The optional verification workflow must
remain distinct from qualitative concern ratings.

## Implementation status

The master prompt supports qualitative review across all twelve dimensions.
This means the instructions are present, not that reviewer accuracy has been
established. The Python lexical baseline reports EA, DC and RR as `not_assessed`
with null scores; its lexical score is unchanged. The illustrations above are
authored review examples, not an independent validation dataset.

Future evaluation should include independent reviewers, agreement and disagreement
analysis, examples from several genres, and deliberate non-findings. Preserve
both revised judgments and the evidence that prompted the revision.

## Sources and attribution

1. **Greenberg, S. A. (2009).** How citation distortions create unfounded authority:
   analysis of a citation network. *BMJ*, 339, b2680.
   https://doi.org/10.1136/bmj.b2680  
   Scope: an empirical analysis of a specific biomedical claim's citation network.
   It motivates tracing support and provenance; it is not a general text-quality scale.
2. **Boutron, I., Altman, D. G., Hopewell, S., Vera-Badillo, F., Tannock, I., &
   Ravaud, P. (2014).** Impact of spin …: the SPIIN randomized controlled trial [title shortened]. *Journal of Clinical Oncology*, 32(36), 4120–4126.
   https://doi.org/10.1200/JCO.2014.56.7503  
   Scope: an experiment on interpretation of clinical-trial abstracts; transfer to
   business summaries is our proposed application.
3. **Charnock, D., Shepperd, S., Needham, G., & Gann, R. (1999).** DISCERN: an
   instrument for judging the quality of written consumer health information on
   treatment choices. *Journal of Epidemiology & Community Health*, 53(2), 105–111.
   https://doi.org/10.1136/jech.53.2.105  
   Scope: development and testing of a domain-specific qualitative instrument.
4. **University of Oxford, Nuffield Department of Population Health.** The DISCERN
   Questionnaire.
   https://www.ndph.ox.ac.uk/research/research-groups/applied-health-research-unit-ahru/discern/the-discern-questionnaire
   Original instrument and guidance; credited as an influence, not reproduced here.
5. **Rogers, T., & Norton, M. I. (2011).** The artful dodger: answering the wrong
   question the right way. *Journal of Experimental Psychology: Applied*, 17(2),
   139–147. https://doi.org/10.1037/a0023439  
   Scope: four studies of question evasion and listener attention, not a validated
   document-analysis algorithm.

Bibliographic records and available abstracts informed this synthesis. The Oxford
questionnaire's indexed guidance was available; direct page retrieval was blocked
during this update. No claim of a systematic literature review or comprehensive
replication audit is made. The original papers and instrument retain their own
rights and terms. No endorsement by their authors or institutions is implied.

© 2026 Ironstone Advisory. Original synthesis: CC BY 4.0.
Underlying repository code remains subject to its existing MIT license.

