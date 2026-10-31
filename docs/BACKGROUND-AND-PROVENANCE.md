# Background, contributions and provenance

Version 1.0 · 31 October 2026

Framework and original design contributions: Rob Tyrie / Ironstone Advisory

Historical reconstruction and documentation prepared with OpenAI Codex

## Purpose and authorship

The Bullshit Compass examines the substance, reasoning and usefulness of text.
Its development includes philosophical inquiry, research discussion, original
design hypotheses, applied reviews and software experiments. The thinkers chosen
in v1 were starting points; they did not supply all the project's measures.

Rob reports beginning the idea in 2022 and making a first version in 2024.
Recovered conversations support related inquiry in 2023 and an applied review
experiment in 2024. Explicit Compass naming was recovered in March 2025, followed
by the April specifications. [HISTORY.md](../HISTORY.md) and the
[evidence ledger](../history/provenance/2026-10-31-conversation-reconstruction.md)
identify what is recollected, retrieved, directly inspectable or still missing.

## An original contribution: the Peterson-derived measure

Rob identifies the measure arising from his observations of Jordan Peterson's
use of tautology in arguments and exposition as his own original design
contribution. It was not taken from Frankfurt's, Pennycook's or Graeber's measures.
This author attribution was clarified on 31 October 2026 (P11).

The inherited README calls the combined pattern "Peterson Weakness": camouflaged
tautologies combined with ideological injections. The archived white paper
separately describes **Tautological Camouflage Rate (TCR)** and **Peterson Weakness
Injector (PWI)**. The inherited `spec-original` explicitly refines/renames PWI as
**Ideological Smuggling Index (ISI)**. These artifacts document the terminology;
they do not establish that every historical formulation is the same construct.

| Element | Current interpretation | Attribution boundary |
|---|---|---|
| TCR | Circular reasoning, empty affirmations or conclusions restated as reasons | The project-specific measure and its role are design contributions; this is not a claim to have invented the general concept of tautology. |
| Historical PWI / "Peterson Weakness" | Rob's proposed pattern connecting apparent self-evidence or tautological camouflage with unsupported argumentative additions | Peterson's discourse was an observational stimulus, not an authored detection method or endorsement. |
| ISI | Contestable premises or unsupported claims embedded in apparently self-evident statements | The later generalization applies to the argument presented, irrespective of speaker identity. |

The observation that motivated a measure, its proposed operational definition,
and evidence that it detects a useful pattern are separate records. Credit the
original contribution while testing its performance. Specific passages, context
and counterexamples must support findings; the historical name is not a verdict
on a person's entire body of work. A common topic, useful definition, summary or
deliberate emphasis is not automatically circular reasoning.

## Three foundational influences

### Harry Frankfurt: language and truth

Frankfurt's *On Bullshit* distinguishes bullshit from lying through a lack of
concern for truth [R1]. It motivates examining how persuasive language relates
to evidence. **Our adaptation** examines identifiable claims and what supports
them. Textual shortcomings do not establish an author's mental state; the current
review avoids diagnosing dishonesty, motives or indifference to truth.

### Gordon Pennycook and colleagues: apparent profundity and discernment

Pennycook, Cheyne, Barr, Koehler and Fugelsang's 2015 study examined judgments of
pseudo-profound statements, including syntactically structured combinations of
buzzwords without discernible meaning, alongside meaningful comparison material
[R2]. It is empirical research on readers' reception and discernment.

Pennycook is foundational in this project's history. In the recovered June 2023
exchange (P02), Rob asks about jargon-filled theories without meaning. After the
assistant introduces this research, Rob asks for a mechanism to assess substance
in complex scientific writing. March–April 2025 requests explicitly combine a
Pennycook-Frankfurt lens (P05–P06).

**Our adaptation** asks what a passage explains or supports and tests whether
clear technical prose and meaningful metaphor survive review. Its links to
Compass dimensions are our design interpretation, not a taxonomy supplied by
the researchers. The study's receptivity measures are not a validated automated
document-quality scale, and do not justify profiling an author or reader.

**Name distinction:** an inherited draft also mentions **Alistair Pennycook** in
connection with critical discourse analysis. That is a different scholar. The
2015 pseudo-profound-bullshit study is by **Gordon Pennycook and the coauthors
listed in R2**; the two attributions must not be merged.

### David Graeber: work and organizational context

Graeber's *Bullshit Jobs* develops an account of work experienced as pointless and
its social consequences [R3]. The April 2025 project draft (P09) proposes that
certain work structures might encourage "bullshit knowledge objects": documents
that signal activity or justify roles without supplying useful substance.

This is a **project hypothesis building on Graeber**, not a demonstrated causal
result or a Graeber text-quality metric. It motivates asking what a document
communicates and enables. Job title, industry or presumed incentives are not
automatic penalties. The archived draft explicitly evaluates texts and rejects
judgments about whether their authors have "bullshit jobs."

## Further influences and the evolving synthesis

Archived drafts also draw on Wittgenstein's language games, Grice's cooperative
principles, Orwell's criticism of obscuring language, and Bierce's satirical
tradition. They contain additional intellectual references. This update records
those as historical influences, not a comprehensive audit of all their works.

Rob's framework was developed through AI-assisted discussion, drafting and
implementation. The grouping of dimensions, project-specific terminology and
review procedures are design choices. Source attribution does not imply that
the cited researchers designed, endorsed or validated the Compass.

| Relationship | Current design | History or research boundary |
|---|---|---|
| Language to supportable meaning | Original nine dimensions interpreted through LGC | Original contributions and cited influences coexist; the complete instrument requires its own evaluation. |
| Claim to support | Evidence Alignment (EA) | The 2026 extension adapts citation-distortion and reporting-spin research. |
| Recommendation to decision needs | Decision Completeness (DC) | Rob's April 2025 critique anticipates this concern; the 2026 formalization also adapts DISCERN. The historical connection is retrospective. |
| Answer to question or purpose | Response Relevance (RR) | The 2026 extension adapts question-evasion research; this named dimension is not backdated to earlier conversations. |

See [FS02-v2-extension.md](FS02-v2-extension.md) for EA/DC/RR definitions,
attribution and boundaries. Historical drafts experimented with different numbers
of indicators and numerical scores. Current guidance uses twelve qualitative
dimensions, LGC as a context layer, and concern separate from confidence. Inherited
words such as "index," "rate" and "score" do not establish statistical validity.

The same textual criteria apply to human, AI-assisted and AI-generated material.
Framework attribution belongs here; reviews should focus on evidence and repair.

## From design to software

The prompt specifies the full review. The Python baseline implements only limited
lexical and repetition proxies. Neither a specification nor passing unit tests
establishes semantic judgment quality. The [evaluation plan](EVALUATION-AND-TRACEABILITY.md)
connects sources and design decisions to cases, reference judgments, versioned
implementations and results, retaining disagreements and revisions.

The [measure review](MEASURE-REVIEW.md) audits all twelve dimensions. The
[test plan](TEST-PLAN.md) includes 36 authored cases and a separate test of the
proposed components of Rob's Peterson-derived construct.

## Primary references

- **R1 — Frankfurt, H. G.** (1986). "On Bullshit." *Raritan*, 6(2), 81–100;
  republished as *On Bullshit*, Princeton University Press (2005).
  [University-hosted text](https://www2.csudh.edu/ccauthen/576f12/frankfurt__harry_-_on_bullshit.pdf).
  [Princeton interview and publication history](https://www.princeton.edu/~paw/archive_new/PAW04-05/13-0420/notebook.html).
- **R2 — Pennycook, G., Cheyne, J. A., Barr, N., Koehler, D. J., & Fugelsang, J. A.**
  (2015). "On the reception and detection of pseudo-profound bullshit."
  *Judgment and Decision Making*, 10(6), 549–563.
  [Original journal text](https://sjdm.org/~baron/journal/15/15923a/jdm15923a.html).
  [DOI](https://doi.org/10.1017/S1930297500006999).
  The issue is November 2015; Cambridge's later online posting date is not the
  original study date.
- **R3 — Graeber, D.** (2018). *Bullshit Jobs: A Theory*. Simon & Schuster.
  [Publisher description and 2018 edition](https://www.simonandschuster.ca/books/Bullshit-Jobs/David-Graeber/9781501143342).
  The publisher also identifies the preceding 2013 essay, "On the Phenomenon of
  Bullshit Jobs." P09 documents the project's specific interpretation.

References and available primary material checked on 31 October 2026. This is an
attributed design history, not a systematic review, replication audit or claim of
historical priority over other projects. Original works retain their own rights.

© 2026 Ironstone Advisory. Original documentation: CC BY 4.0.
