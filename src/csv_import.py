import logging
import sys
from pathlib import Path

import polars as pl


def main():
    try:
        csv_path = Path(sys.argv[1])
        if not csv_path.exists():
            raise FileNotFoundError

    except Exception:
        logging.error("Please pass a valid path to an input csv file.")
        raise

    schema = pl.Schema(
        {
            "Title": pl.String(),
            "Content": pl.String(),
            "Status": pl.String(),
            "Requirement": pl.String(),
            "Spec": pl.String(),
            "Test": pl.String(),
        }
    )
    csv_data = pl.read_csv(csv_path, quote_char=None)

    for row in csv_data.iter_rows(named=True):
        if not row["Title"]:
            # skip empty lines
            continue
        logging.info(row)


if __name__ == "__main__":
    main()
