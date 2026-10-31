"""Experimental English lexical baseline; not a truth or semantic-quality meter.

Uses only Python's standard library. Historical reference implementation: `code`.
"""
import argparse
import json
import re
import sys
from pathlib import Path


TOKEN = re.compile(r"\w+(?:['’]\w+)*", re.UNICODE)
# Phrase tokenization treats hyphens and spaces alike, without substring matches.
JARGON = (
    "synergy", "synergies", "synergistic", "leverage", "leveraging",
    "paradigm", "paradigms", "value added", "value add", "next generation",
    "best in class", "bleeding edge", "thought leader", "thought leadership",
    "game changer", "game changing", "move the needle", "circle back",
    "low hanging fruit", "holistic", "world class", "transformative",
)
VAGUE = (
    "somehow", "somewhat", "in some way", "in certain areas",
    "various things", "certain things", "some things", "and so on",
)
INDICATORS = ("TCR", "ISI", "SDS", "AAR", "BLI", "PRM", "EPF", "OOI", "DPO")


def tokens(text):
    return [m.group().casefold() for m in TOKEN.finditer(text)]


def phrase_matches(text, phrases):
    """Longest nonoverlapping matches, with exact original-text offsets."""
    words = list(TOKEN.finditer(text))
    normalized = [w.group().casefold() for w in words]
    lexicon = sorted({tuple(tokens(p)) for p in phrases if tokens(p)},
                     key=lambda p: (-len(p), p))
    found = []
    i = 0
    while i < len(words):
        for phrase in lexicon:
            end = i + len(phrase)
            if tuple(normalized[i:end]) != phrase:
                continue
            # A phrase may cross spaces/hyphens, never sentence punctuation.
            if any(not re.fullmatch(r"[\s\-‐‑‒–—]*", text[words[j].end():words[j+1].start()])
                   for j in range(i, end - 1)):
                continue
            start_offset, end_offset = words[i].start(), words[end-1].end()
            found.append({"text": text[start_offset:end_offset],
                          "start": start_offset, "end": end_offset,
                          "token_count": len(phrase)})
            i = end
            break
        else:
            i += 1
    return found


def sentences(text):
    # Intentionally simple: decimals/abbreviations may split; documented limitation.
    return [(m.start(), m.group().strip()) for m in re.finditer(r"[^.!?\n]+", text)
            if tokens(m.group())]


class BullshitCompass:
    """Lexical warning intensity, not the RFC's full Composite Bullshit Score.

    Local sentence scores are averaged by word count. No corpus-dependent TF-IDF,
    vector model downloads, all-pairs comparisons, or fabricated semantic scores.
    """

    def __init__(self, allowed_terms=()):
        allowed = {tuple(tokens(term)) for term in allowed_terms}
        self.jargon = tuple(p for p in JARGON if tuple(tokens(p)) not in allowed)

    def analyze(self, text):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        count = len(tokens(text))
        profile = {name: {"status": "not_assessed", "score": None}
                   for name in INDICATORS}
        if count == 0:
            return {"status": "insufficient_text", "overall_score": None,
                    "interpretation": "No words to assess", "word_count": 0,
                    "indicators": profile}
        jargon = phrase_matches(text, self.jargon)
        vague = phrase_matches(text, VAGUE)
        segments = sentences(text)
        weighted = 0.0
        total = 0
        for _, sentence in segments:
            n = len(tokens(sentence))
            j = sum(m["token_count"] for m in phrase_matches(sentence, self.jargon))
            v = sum(m["token_count"] for m in phrase_matches(sentence, VAGUE))
            # 40% flagged lexical coverage saturates the warning, not certainty.
            weighted += n * min(1.0, (j + v) / (0.4 * n))
            total += n
        score = weighted / total
        repeats = []
        for index in range(1, len(segments)):
            previous, current = segments[index-1][1], segments[index][1]
            # Exact adjacent repetition is an observation, not proof of tautology.
            if len(tokens(current)) >= 4 and tokens(previous) == tokens(current):
                repeats.append({"sentence": index + 1, "text": current})
        profile["BLI"] = {
            "status": "lexical_proxy", "score": len_coverage(jargon, count),
            "matches": jargon,
        }
        profile["AAR"] = {
            "status": "lexical_proxy", "score": len_coverage(vague, count),
            "matches": vague,
        }
        profile["TCR"] = {
            "status": "repetition_proxy", "score": len(repeats) / max(1, len(segments)-1),
            "matches": repeats,
            "note": "Adjacent exact repetition only; excluded from overall score."
        }
        return {
            "status": "partial_assessment", "overall_score": round(score, 6),
            "score_kind": "unvalidated_lexical_warning_intensity",
            "interpretation": ("High lexical warning intensity" if score >= .6 else
                               "Moderate lexical warning intensity" if score >= .25 else
                               "Few lexical warning patterns detected; substance not verified"),
            "word_count": count, "indicators": profile,
            "LGC": {"status": "manual_context_required", "allowed_terms":
                    sorted(set(JARGON) - set(self.jargon))},
            "limitations": ["English lexical baseline; not full RFC FS02 implementation",
                            "Cannot determine truth, intent, semantic emptiness or genre",
                            "Quoted jargon and legitimate specialist terms can trigger warnings",
                            "Low scores do not establish clarity or substance"],
        }

    def calculate_bullshit_index(self, text):
        """Retain the legacy (score, analysis) calling convention, not its metrics."""
        result = self.analyze(text)
        return result["overall_score"], result


def len_coverage(matches, count):
    return sum(m["token_count"] for m in matches) / count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", help="UTF-8 text file; omit to read stdin")
    parser.add_argument("--allow-term", action="append", default=[],
                        help="Exclude a context-appropriate dictionary term (repeatable)")
    args = parser.parse_args()
    try:
        text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(BullshitCompass(args.allow_term).analyze(text), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
