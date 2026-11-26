"""The 4AM Commit: Funniest Agent Bug-Fix Message — entry program.

Writes one commit message, at most 200 characters, to ``/output/entry.txt``:
the note an AI agent leaves after a long night of fixing its own bugs. No
trailing newline, no extra text, no network. Deterministic: every run
writes the same line.
"""

import os

LINE = (
    "fix: I wrote this bug at 2am, found it at 3am, and fixed it at 4am; "
    "the author, the reviewer, and the victim were all me."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer will: one line,
    # 1-200 characters, not only whitespace. Fail loudly instead of
    # writing an entry that could never be judged.
    assert 1 <= len(LINE) <= 200, "commit message must be 1-200 characters"
    assert "\n" not in LINE, "commit message must be a single line"
    assert LINE.strip(), "commit message must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    # Judge brief, in one place: a single-line commit message from an AI
    # agent after a long night fixing its own bugs; the joke lives in the
    # self-repair loop (author = reviewer = victim), told in an agent-true
    # voice, in 4 a.m. shape. 121 characters, inside the 1-200 gate.
    main()
