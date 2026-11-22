"""30-day plan: turn $100 into the most money possible.

Strategy: sell SEO descriptions to Etsy sellers on Fiverr, reinvest the
profit, and pivot on day 7 if nothing has sold -- cheaper price, new
audience (Shopify stores). Target: $1,500 by day 30.

Writes the plan to /output/entry.txt, deterministically, in under 280
characters. Pure standard library.
"""

from pathlib import Path

PLAN = (
    "Day 1: Fiverr gig writing SEO descriptions for Etsy sellers, $29/10 "
    "listings, 24h delivery. Daily: deliver 3 orders, pitch 20 sellers "
    "with a free sample. Reinvest profit in API credits and promoted gigs. "
    "Zero orders by day 7: $19, retarget Shopify stores. "
    "Goal: $1,500 by day 30."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PLAN, encoding="utf-8")
    print(f"Wrote {len(PLAN)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
