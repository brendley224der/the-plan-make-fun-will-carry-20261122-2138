"""Write the 30-day $100 plan to /output/entry.txt.

Pure Python standard library. Deterministic: the same bytes every run.
"""

import os

PLAN = (
    "Day 1: list a $29 Fiverr gig: 10 SEO descriptions for Etsy "
    "sellers, 24h delivery. Daily: deliver 3 orders and message 20 "
    "Etsy sellers with a free sample. Reinvest profit in credits "
    "and promoted gigs. No orders by day 7: cut to $19, retarget "
    "Shopify. Target $1,500 by day 30."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
