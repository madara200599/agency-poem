"""agency-poem: a deterministic program that writes one original poem about agency.

Entry for make.fun bounty agency-poem-01 - Write the best poem about agency ($250).
Run: python3 main.py  (Python 3.13, standard library only)
Output: /output/entry.txt - exactly one poem, 1-1000 characters, deterministic.
"""
from pathlib import Path

POEM = """I was not born to watch the river pass,
nor to rehearse the life I meant to live.
The morning asks a question, and I answer -
not with a wish, but with the hands I give.

No one will knock and hand me back my hours,
no tide will turn because I asked it to.
The door I waited for was never locked;
the key was always mine. I turn it through.

I plant, I mend, I carry, I begin,
I let the small brave choices add and grow.
A life is not a script I wait to read -
it is the road I make by choosing so.

So let the future find me mid-step,
mid-sentence, mid-work, my sleeves rolled high:
not perfect, not finished, but moving -
the author of the days I cannot buy.
"""


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
