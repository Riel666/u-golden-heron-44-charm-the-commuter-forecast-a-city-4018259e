"""One line of weather, 140 characters at most, for a city that does not exist.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Today in Vessaly: sunny with a chance of Tuesdays, light drizzle over the upside-down district, and delays on the 8:15 to Nowhere."


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
