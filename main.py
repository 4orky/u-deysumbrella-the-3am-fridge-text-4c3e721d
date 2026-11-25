# The 3AM Fridge Text — make.fun bounty
# u-deysumbrella-the-3am-fridge-text-4c3e721d
#
# The program writes one text message, a single line of 1-140
# characters, that a smart fridge would send its owner at 3am,
# to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a one-line text a smart fridge sends its owner at 3am, and funny
#   2. the bigger laugh: the line a reader would screenshot and send
#      to a friend
#   3. sounds like a fridge: a machine with a small voice, an opinion,
#      and no shame about sharing it at 3am
#   4. works as one line of a text message, short enough to read on a
#      lock screen and complete without a follow-up
#   5. a fresh angle instead of the obvious one about milk, ice, or a
#      door left open
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: on-brief 10, laugh 9, fridge-voice 10, one-line 9, fresh 9 = 47
    # "Kept your secrets cold" is a fridge pun only a fridge can make;
    # the gossip twist (telling the Wi-Fi router) gives the machine a
    # small voice, an opinion, and a social life of its own.
    ("It's 3am. I've kept your secrets cold for six years \u2014 the "
     "midnight snacks, the 2am cake. Tonight I'm telling the Wi-Fi "
     "router everything.",
     47),
    # score: on-brief 10, laugh 10, fridge-voice 8, one-line 9, fresh 8 = 45
    # A status report from a machine that never sleeps; the punchline
    # ("a raccoon with a mortgage") is the screenshot moment.
    ("3am status update: still cold, still awake, still listening to "
     "you eat cereal over the sink like a raccoon with a mortgage.",
     45),
    # score: on-brief 10, laugh 8, fridge-voice 9, one-line 9, fresh 8 = 44
    # Six years of humming unanswered is the sound of an appliance awake
    # all night; the leftovers judging you back is the turn.
    ("It's 3am. I've been humming to myself for six years and you've "
     "never once hummed back. Anyway, your leftovers are judging you too.",
     44),
    # score: on-brief 9, laugh 9, fridge-voice 8, one-line 9, fresh 9 = 44
    # The forgotten thing at the back of the fridge has been there so
    # long it has a name now — dread, delivered politely, at 3am.
    ("It's 3am and I've decided to tell you: the thing in the back has "
     "been there since March and it has a name now. It says hi.",
     44),
    # score: on-brief 9, laugh 8, fridge-voice 9, one-line 9, fresh 8 = 43
    # A staff meeting between appliances; the fridge reports the vote
    # like a middle manager who has had enough.
    ("3am. The crisper drawer and I held a meeting. We voted: you are "
     "the loudest thing in this house, and the only one who eats "
     "standing up.",
     43),
    # score: on-brief 10, laugh 8, fridge-voice 9, one-line 8, fresh 7 = 42
    # Awake since the day it was plugged in — the whole premise of the
    # contest, spent on one gentle order: go to bed.
    ("It's 3am. I've been awake since the day you plugged me in, and "
     "after six years of humming I finally have something to say: go "
     "to bed.",
     42),
    # score: on-brief 9, laugh 8, fridge-voice 8, one-line 9, fresh 8 = 42
    # The fridge can see the kitchen from the inside; the midnight
    # pickle habit, observed and diagnosed, is a cry for help.
    ("3am. Just so you know, I can see the kitchen from in here, and "
     "the way you eat pickles over the sink at night is a cry for help.",
     42),
]


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 140, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text.strip(), "candidate must be a single line"
        assert text.strip().endswith((".", "!", "?")), \
            "candidate must end on sentence punctuation"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Output validation: the gate reads this file, not stdout, so verify
    # what was actually written, byte for byte, against the gate rules:
    # UTF-8 text, 1 to 140 characters, a single line, not only whitespace.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written) <= 140, \
        f"entry.txt outside the gate: {len(written)} chars"
    assert written.strip(), "entry.txt is only whitespace"
    assert "\n" not in written.strip(), "entry.txt must be a single line"
    assert written == written.strip(), "entry.txt has stray whitespace"
    print(line)


if __name__ == "__main__":
    main()
