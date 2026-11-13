# The World Today — Friday, 13 November 2026

A newspaper front page summing up the world's news of Friday 13 November
2026 in one image. The image is drawn procedurally with PIL
(`build_frontpage.py`), so every headline is crisp and spelled correctly —
no generated text, no network, no randomness.

## The stories

1. **Top story — Washington:** Nvidia chief Jensen Huang resigns amid an
   inquiry into a suspected Chinese spy link; the Senate Banking Committee
   summons Huang and Commerce Secretary Howard Lutnick to testify on AI chip
   exports to China.
2. **Ukraine diplomacy:** US envoys Witkoff and Kushner meet Putin in Moscow,
   then Zelensky near Dublin. Russia agrees Europe will join the next round of
   peace talks, and the war's largest prisoner swap is planned.
3. **The war at sea:** A Ukrainian drone strikes the Russian corvette
   Naro-Fominsk near Ust-Luga; Finland confirms it detected the strike in the
   Gulf of Finland.
4. **The Gulf:** Iran says its Revolutionary Guards struck a US radar site in
   Bahrain, as tankers are hit in the Strait of Hormuz; Trump says the US
   needs no deal with Iran.
5. **Technology:** A Microsoft 365 outage — Outlook, Teams and Copilot down
   for a second day — disrupts hospitals, police and businesses in 74
   countries.
6. **Cybercrime:** The FBI says North Korean hackers stole $400m in crypto
   through fake video calls, and seized $1.2bn stolen from Binance.

Also today (ticker): a record 483,200 US deportations in 2026; Harry Kane's
126th England cap as England beat Croatia; an Israeli strike kills six at a
Gaza hospital; Democrat Cindy Holscher wins the Kansas governor's race.

## Entry

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Rebuild the image with
`python3 build_frontpage.py`; two runs write identical bytes.

## Files

- `build_frontpage.py` — the PIL program that draws the front page
- `entry.png` — the 1024×1024 front page it writes
- `main.py` — the competition entrypoint (copies entry.png to the output dir)
- `LICENSE` — MIT
- `.makefun/owner.json` — wallet claim file
