"""The joke about the demo — make.fun entry.

Writes one original one-line joke about working beside AI coding agents
to /output/entry.txt. No network, no randomness, no input: the same text
every run.
"""

import os

JOKE = (
    "My coding agent passed every test I wrote, then failed the live demo "
    "by confidently fixing a bug that never existed."
)

# The gate allows 1 to 280 Unicode code points; refuse to write anything
# outside it rather than submit an invalid entry.
assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
assert JOKE.strip(), "joke must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
