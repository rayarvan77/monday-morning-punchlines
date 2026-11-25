#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke, 200 characters at most.

The entry line is printed exactly as-is, one line, no decoration.

Why this joke: the setup sounds like a legal document, then the
punchline turns the bed into the custodial parent and Monday into
the weekend visitor who only shows up at 7 a.m. — a surprise turn
on the most Monday-morning feeling there is: not wanting to get up.
The line is 124 characters, well inside the 200-character cap.
"""

JOKE = (
    "My bed and Monday morning signed a custody agreement: "
    "the bed keeps me, and Monday only gets supervised "
    "visitation at 7 a.m."
)

MAX_CHARS = 200


def main() -> None:
    if len(JOKE) > MAX_CHARS:
        raise SystemExit("joke exceeds the 200-character limit")
    print(JOKE)


if __name__ == "__main__":
    main()
