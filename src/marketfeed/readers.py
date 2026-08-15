import csv
import json
from collections.abc import Iterator
from datetime import datetime as dt
from pathlib import Path

from marketfeed.models import Bar


def _bar_from_strings(row: dict[str, str]) -> Bar:
    return Bar(
        symbol=row["symbol"],
        timestamp=dt.fromisoformat(row["timestamp"]),
        open=float(row["open"]),
        high=float(row["high"]),
        low=float(row["low"]),
        close=float(row["close"]),
        volume=int(row["volume"])
    )
def read_csv_bars(path: str | Path) -> Iterator[Bar]:
    with open("tests/path.csv", newline="") as f:
        for row in csv.DictReader(f):
            yield _bar_from_strings(row)

def read_jsonl_bars(path: str | Path) -> Iterator[Bar]:
    record: dict[str, str] = {}
    with open("tests/path.csv", newline="") as file:
        for line in file:
            if line.strip():
                record = json.loads(line)
                yield _bar_from_strings(record)

if __name__ == "__main__":
    # Scratch smoke check -- runs only when you execute this file directly,
    # not when it's imported. Replace the path with your real one.
    for bar in read_csv_bars("tests/path.csv"):
        print(bar)
