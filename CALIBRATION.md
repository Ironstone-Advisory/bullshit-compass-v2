# Calibration finding: v1 code, October 17, 2026

*By Rob Tyrie, Ironstone Advisory.*

The v1 reference code (`code`) was run unmodified on October 17, 2026, as the gate instrument for the NeoLibrary repos ([RFC-0004](https://github.com/Ironstone-Advisory/neolibrary/blob/main/rfcs/RFC-0004-how-we-build.md)). NLTK stopwords were supplied from spaCy's English list because the NLTK data download was blocked in that environment; `textstat` was pinned to 0.7.3 because newer versions need the CMU dictionary.

## Result: the instrument doesn't separate fog from plain text

| Sample | Expected | Score |
|---|---|---|
| "We are leveraging synergistic paradigms to actualize next-generation value-added solutions." | high | **0.04** ("clear and substantive") |
| "The project deadline is May 15th. We need to deliver the database migration and API endpoints by then." | low | 0.00 |

On real documents (15 Markdown files, 2 to 30 KB) every score landed between 0.20 and 0.43, whatever the quality of the prose.

## Why

1. **Tautology saturates.** It compares every sentence pair with spaCy vector similarity. In any document longer than a few paragraphs, many pairs exceed the threshold, so the component hits 1.0.
2. **Semantic emptiness sits near 0.95 everywhere.** The TF-IDF and readability blend isn't normalized for document length.
3. **Jargon density barely moves.** The 24-term built-in dictionary catches "synergistic" and "value-added" but scores them against all tokens, so even a sentence made of jargon reads 0.17.

## First v2 requirements

- A calibration set checked into the repo: graded samples from plain to pure fog, each with an expected band.
- A test that fails the build if fog doesn't outscore plain text.
- Length normalization for every component.
- Sentence similarity with a contextual model and a much higher threshold, or tautology detection restricted to adjacent sentences.
- Indicators aligned with RFC FS02 v0.88 (TCR, ISI, SDS, AAR, BLI, PRM, EPF, OOI, DPO plus LGC). The v1 code implements five of its own.
