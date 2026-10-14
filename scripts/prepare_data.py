"""Validate and convert the Olist tables used by the workshop to Parquet."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


TABLES: dict[str, tuple[set[str], tuple[str, ...]]] = {
    "olist_orders_dataset": (
        {
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
        },
        (
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ),
    ),
    "olist_customers_dataset": (
        {"customer_id", "customer_unique_id"},
        (),
    ),
    "olist_order_items_dataset": (
        {"order_id", "order_item_id", "product_id", "price"},
        ("shipping_limit_date",),
    ),
    "olist_products_dataset": (
        {"product_id", "product_category_name"},
        (),
    ),
    "product_category_name_translation": (
        {"product_category_name", "product_category_name_english"},
        (),
    ),
}


def convert_tables(raw_dir: Path, processed_dir: Path) -> list[Path]:
    """Convert required source CSVs, rejecting missing or unexpected schemas."""
    missing_files = [
        raw_dir / f"{table}.csv"
        for table in TABLES
        if not (raw_dir / f"{table}.csv").is_file()
    ]
    if missing_files:
        missing_list = "\n".join(f"- {path}" for path in missing_files)
        raise FileNotFoundError(
            "Faltan CSV del dataset de Olist:\n"
            f"{missing_list}\n"
            "Descargue el dataset de Kaggle, descomprima sus CSV en "
            f"{raw_dir} y vuelva a ejecutar scripts/prepare_data.py."
        )

    processed_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for table, (required_columns, date_columns) in TABLES.items():
        source = raw_dir / f"{table}.csv"
        headers = set(pd.read_csv(source, nrows=0).columns)
        missing_columns = required_columns - headers
        if missing_columns:
            missing_names = ", ".join(sorted(missing_columns))
            raise ValueError(
                f"El archivo {source.name} no tiene las columnas esperadas: "
                f"{missing_names}. Compare sus encabezados con "
                "docs/diccionario_datos.md y confirme la versión del dataset."
            )

        frame = pd.read_csv(
            source,
            parse_dates=[column for column in date_columns if column in headers],
        )
        destination = processed_dir / f"{table}.parquet"
        frame.to_parquet(destination, index=False)
        outputs.append(destination)
        print(f"{source.name} -> {destination} ({len(frame):,} filas)")

    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "raw",
        help="Carpeta con los CSV descargados (por defecto: data/raw).",
    )
    parser.add_argument(
        "--processed-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "processed",
        help="Destino de los Parquet (por defecto: data/processed).",
    )
    args = parser.parse_args()
    convert_tables(args.raw_dir, args.processed_dir)


if __name__ == "__main__":
    main()
