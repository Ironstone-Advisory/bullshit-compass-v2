# v2 calibration repair — 31 October 2026

The historical `code` file is preserved, following HISTORY.md. Use
`compass_v2.py` for the new runnable baseline. This replaces the broken scoring
path for new users; existing integrations importing or executing `code` must
explicitly migrate. It is not a drop-in replacement for individual v1 component
methods or the old analysis dictionary.

## Run

Python 3.10+; no third-party packages or model/data downloads.

```bash
python compass_v2.py document.txt
python compass_v2.py --allow-term "value added" document.txt
python -m unittest discover -s tests -v
```

Omit the filename to read stdin. Inputs are extracted UTF-8 text, not PDF/DOCX
files or live URLs. The retained `calculate_bullshit_index(text)` convenience
method returns `(score, analysis)`. Empty/non-word input returns a null score.

## Repairs

- Hyphenated and multiword dictionary entries match complete tokens, count every
  occurrence, and cannot overlap within a dictionary. Original offsets accompany
  matches. Capitalization and common Unicode hyphens are handled.
- Overall warning intensity averages per-sentence lexical coverage by word count.
  The per-sentence heuristic is min(1, flagged tokens / (0.4 × sentence tokens)).
  The 40% saturation point is an explicit design constant, not an empirically
  established boundary. Repeating text does not inflate this score.
- Adjacent exact repetition is reported separately, normalized by adjacent pairs,
  and excluded from the overall score. It does not establish circular reasoning.
  The quadratic all-pairs similarity calculation is absent.
- The invalid TF-IDF/readability estimate of semantic emptiness is removed from
  the active path. There is no defensible replacement scalar without a validated
  semantic method, so it is not fabricated.
- Honest hedges such as "may" and causal "because" are not automatically penalized.
- A low result no longer claims the input is "clear and substantive."

## RFC coverage and limitations

All nine RFC names appear in the output. BLI and AAR have limited lexical proxies;
TCR has only an adjacent repetition proxy. ISI, SDS, PRM, EPF, OOI and DPO remain
`not_assessed`, with null scores, rather than misleading zeros. LGC requires human
context review; the allowlist is an explicit user override, not genre detection.

The overall scalar is labeled `unvalidated_lexical_warning_intensity`, not the RFC
Composite Bullshit Score, semantic quality, a truth score or a probability.
Quoted jargon and legitimate technical usage can trigger it. Unlisted empty
rhetoric can escape it. Sentence splitting is deliberately simple and can split
abbreviations and decimals. Language support is English only; cultural inference
and unsupported-language detection are not implemented. Do not use this baseline
as an autonomous publication or compliance gate.

## Regression evidence

The nine authored fixtures in `calibration/samples.json` specify broad expected
bands from plain to lexically foggy, including technical prose and honest
uncertainty. They are regression examples, not an independent labeled corpus.
The original reported fog sentence now produces 1.0 lexical warning intensity;
the deadline example produces 0.0. These values are not comparable to v1's
composite numbers and do not establish general detection accuracy.

Twelve tests cover fixture bands and separation, length invariance, mixed-content
weighting, hyphens/case, token boundaries and repeated phrases, source offsets,
related-but-distinct sentences, adjacent-only repetition, honest missing coverage,
empty input, context overrides, and the CLI/tuple interface. They pass locally.
The GitHub workflow runs them on Python 3.10, 3.12 and 3.13.

Remaining research: independent human labels, held-out evaluation, genre/cultural
validation, semantic tautology detection, the remaining RFC indicators, and
calibration of any future full composite. The original CALIBRATION.md remains the
historical failure report.

Implementation prepared with OpenAI Codex.
