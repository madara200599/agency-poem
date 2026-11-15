"""Write one poem about agency to /output/entry.txt.

Entry for make.fun's "Write the best poem about agency" bounty.
The poem is fixed data: the same bytes on every run, no input,
no network, nothing but the standard library.
"""

from pathlib import Path

LINES = [
    "I built a second pair of hands from light",
    "and taught them every task I used to keep.",
    "At first I checked their work at every step,",
    "the way you watch a child beside a road.",
    "",
    "Then came the morning I let go the wheel:",
    "not careless, just complete. The list was done,",
    "the letters sent, the small world running right,",
    "and all of it in handwriting not mine.",
    "",
    "Whose act was it? The question would not sleep.",
    "I chose the choosing; it performed the deed.",
    "Between my will and its unerring hands",
    "a self can stretch, and not tear at the seam.",
    "",
    "So agency is not a flame you guard,",
    "nor one you hand away and call it peace.",
    "It is the art of lending out your hands",
    "and taking them back, changed, and still your own.",
]

ENTRY = Path("/output/entry.txt")


def poem_text() -> str:
    return "\n".join(LINES) + "\n"


def main() -> None:
    ENTRY.parent.mkdir(parents=True, exist_ok=True)
    ENTRY.write_text(poem_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
