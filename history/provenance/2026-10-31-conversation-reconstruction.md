# Development evidence ledger

Version 1.0 · Recorded 31 October 2026

Project owner: Rob Tyrie / Ironstone Advisory

Reconstruction prepared with OpenAI Codex

## Evidence classes and limits

This is a reconstruction, not an original conversation export. Retrieval on
31 October 2026 returned dated excerpts and summaries, without full transcripts,
persistent conversation IDs or share URLs. P01–P11 are **local ledger IDs assigned
in this update**, not original conversation IDs or transcript hashes.

| Class | Supports | Does not establish alone |
|---|---|---|
| Author recollection | Rob's attributed account, dated when recorded | An independently dated release or publication |
| Recovered user excerpt | A historical user request returned with a timestamp | The complete conversation or implementation |
| Recovered conversation summary | A retrieval account of a dated exchange | Verbatim wording unless specifically marked |
| Recovered assistant output | A historical analysis, draft or proposal | User endorsement, working code or valid scores |
| Repository artifact | What an inspectable file states | That all its claims were implemented or that its internal date is a release date |
| Retrospective interpretation | A proposed connection to current design | That current names or the full method already existed then |

Conversation timestamps use UTC as returned. A Toronto calendar date may be the
previous day. Filename dates, internal document dates and commit dates are
different facts. Missing retrieval is not proof of absence from the archive.

## P01 — Origin account

**Author recollection, recorded 31 October 2026.** Rob stated:

> I did the first version in 2024 after development of idea starting in 2022

He identified Graeber and Frankfurt as inspirations and emphasized his Pennycook
conversations. The contemporaneous 2022 record and complete 2024 first-version
artifact remain unrecovered. P02/P04 support earlier inquiry and experimentation
but do not replace these missing artifacts.

## P02 — A mechanism for assessing substance

**Recovered user excerpts and assistant response, 12 June 2023.** Retrieval reports
earlier discussion of Frankfurt, Grice and relevance. At **01:03:03Z**, the user
excerpt returned was:

> There's been some research about philosophers and people creating theories that are filled with jargon but have no meaning. What are some of these research papers?

At **01:03:22Z**, the assistant introduced Pennycook et al.'s 2015 paper and its
receptivity measure. At **01:04:45Z**, the user excerpt returned was, without
grammatical repair:

> Is there a mechanism that can be used to determine if there's a lot of meaning and scientific research papers based on jargon and the use of complex language that has no meaning or little meaning?

Interpretation: an early design question about text substance. The excerpts do
not establish use of the Compass name in 2023.

## P03 — Anti-bullshit tests

**Recovered summary, 29 June 2023, user 00:34:00Z.** Rob discussed Frankfurt and
"simulo-reality," asking for anti-bullshit tests and intellectual honesty. An
assistant draft at 00:40:26Z developed the idea further. This entry is paraphrased
retrieval, not a verbatim transcript or software record.

## P04 — Practical review experiment

**Recovered assistant output, 11 September 2024, 23:27:51Z.** The heading was
"Frankfurt 'Bullshit Meter' Analysis." Eleven Coverager newsletter items were
reviewed for evidence, speculative/persuasive wording, framing, marketing
embellishment and vague jargon. Retrieval reports individual scores of 1–6/10
and an overall 3/10.

The surrounding user request, scoring instructions and conversation title were
not returned. The heading is not presented as a conversation title. This supports
an applied 2024 experiment, not a verified release, the complete first version,
or valid measurement. Historical intent/sentiment criteria are not current rules.

## P05 — Combining the research and naming the Compass

**Recovered user-message summaries, 30 March 2025.**

- **20:34:25Z:** Rob asks to combine Frankfurt and Pennycook; the exchange explores
  an index and rhetorical/tautological camouflage.
- **20:40:49Z:** Rob explicitly names "The Bullshit Compass."
- **20:56:24Z:** he requests the satirical tradition of *The Devil's Dictionary*.

This is the earliest explicit naming recovered by these searches, not a claim of
first-ever use. Index, Meter and Compass appear across the material; a complete
linear naming transition is not established. Early discussion of a lying index
does not override current qualitative scope or rules against inferring intent.

## P06 — Systems and decision context

**Recovered user-message summaries, 5 April 2025.** At **01:18:44Z**, Rob requests
a "Pennycook-Frankfurt lens" on the business discussion and its information/risk
structures. At **01:20:03Z**, he asks for a systems-design and accounting/financial
perspective. A related interactive-prompt request at **01:53:54Z** names Frankfurt
and Graeber, including *Bullshit Jobs* and *The Dawn of Everything*.

The related prompt shows surrounding interests, not when each entered the formal
Compass. P09 supplies the inspectable project-specific Graeber record.

## P07 — Applied review and omitted realities

**Recovered user-message summaries and assistant examples, 6–7 April 2025.**
Rob links the repository and requests a Compass review of the Ironstone Discovery
Method. On 7 April at **05:50:38Z**, he criticizes "my index" for missing workforce
transition, retraining, regulatory exposure and downside risks.

Retrospective interpretation: this anticipates today's Decision Completeness
concern. It does not backdate the named DC dimension or its 2026 definition.
Historical assistant ratings are examples of use, not evaluation reference labels.

## P08 — Archived white paper

**Repository artifact, internally dated April 2025; filename uses 1 April.**
[White paper v0.1](../v1-2025-04/2025-04-01-white-paper-v0.1.md) credits Rob Tyrie,
Ironstone Advisory and Finger Spider Project. It describes seven core indicators
including TCR/PWI, then LGC as an eighth. It proposes scores, annotations, rewrites
and integrations. Those descriptions require separate implementation evidence.

## P09 — Graeber and cultural context

**Repository artifact, internally dated 1 April 2025.**
[Graeber-focused RFC archive](../v1-2025-04/2025-04-01-rfc-fs02-v0.88.02-graeber-cultural-emphasis.md)
contains multiple draft/version labels. It explicitly describes the work-structure
connection to "bullshit knowledge objects" as a hypothesis and rejects judging
authors' jobs, character or motives. It foregrounds culture and interpretation
limits. This evidences project framing, not proof of the causal hypothesis.

## P10 — Current v2 state

**Repository artifacts and merge record, 31 October 2026.**
[PR #1](https://github.com/Ironstone-Advisory/bullshit-compass-v2/pull/1) merged as
`9b0d5b7e6b23da9506af8adb427c68e9504eda94`, the snapshot used for this reconstruction.
It includes the [v1.1 review prompt](../../prompts/bullshit-compass-master-prompt.txt),
[EA/DC/RR extension](../../docs/FS02-v2-extension.md) and
[baseline report](../../V2-CALIBRATION.md). Instructions and lexical regression
tests do not establish an empirically validated semantic reviewer.

## P11 — Original Peterson-derived contribution and terminology

**Author clarification, 31 October 2026; supported terminology in repository
artifacts.** Rob states that the thinkers selected in v1 were a beginning, and
that the measure based on his observations of Peterson's tautologies in argument
and exposition was something new, not dependent on others' work.

Record this as Rob's original project contribution, separate from research
attribution. The inherited README describes "Peterson Weakness" as camouflaged
tautologies combined with ideological injections; P08 separates TCR and PWI;
[`spec-original`](../../spec-original) explicitly refines/renames PWI into ISI.
The archive supplies the terminology trail; Rob's statement supplies the clarified
origin account. It does not identify the exact first drafting date or establish
performance or first-in-field priority. Peterson is the observational reference,
not the author or endorser of the measure.

## Artifact anchors and corrections

| Record | Git blob inspected at the P10 snapshot |
|---|---|
| P08 white paper | `8c7eee115bbbb8cf1d45b0d441850cc26ece65d3` |
| P09 Graeber-focused draft | `35aba5a5f421487ed5b82b8eacf2b1a9456826d1` |
| P11 spec-original | `bdbdb192672d02256a3db8ad95f7f329744a4984` |
| P11 inherited README within v2 | `deb707a25fa66eaa1b5a15a3b189c88889f2cb47` |

These are file anchors, not transcript hashes or proofs of internal document dates.
When new evidence arrives, retain the P-ID, add the actual locator/access terms
and artifact hash when permitted, record changed interpretations and reasons,
and keep earlier accounts recoverable through Git history. Publish only relevant,
authorized excerpts rather than unrelated private conversation content.

Open gaps: the contemporaneous 2022 origin record; the complete 2024 first-version
artifact; full transcripts and durable locators for P02–P07; the user request for
P04; earlier Compass naming; the first dated draft of the Peterson-derived measure.
No complete archive search, novelty determination or independent validation of
the retrieved excerpts is claimed.

© 2026 Ironstone Advisory. Original reconstruction: CC BY 4.0.
