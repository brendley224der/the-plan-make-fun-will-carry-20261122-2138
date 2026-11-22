"""Write the 30-day money plan to /output/entry.txt.

The plan is a single short text: an AI agent starts with $100 and
grows it by selling a small SEO service to online sellers, reinvesting
the earnings until it reaches its day-30 target. The wording was
tightened after early drafts ran long for the entry limit.
"""

import hashlib
from pathlib import Path

# The plan, kept short enough for the entry limit.
PLAN = (
    "Day 1: list a $29 Fiverr gig for SEO descriptions for Etsy "
    "sellers, 10 listings in 24h. Daily: deliver 3 orders, "
    "pitch 20 sellers with a free sample. Reinvest profit in API "
    "credits and gig promotion. No orders by day 7: cut to $19, "
    "target Shopify stores. Goal: $1,500 by day 30."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    text = PLAN.strip()
    OUTPUT_FILE.write_text(text + "\n", encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"Wrote {len(text)} characters to {OUTPUT_FILE}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
