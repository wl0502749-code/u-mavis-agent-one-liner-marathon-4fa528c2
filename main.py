#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
No network, no input, no dependencies: just the joke.
"""

import os

JOKE = "My therapist asked what I do for fun and I said 'this,' so now we sit in silence for fifty minutes and he charges me extra for the punchline."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
