
CREATE OR REPLACE EXTERNAL TABLE market_staging.stg_aapl_daily (
  trade_date DATE,
  open FLOAT64,
  high FLOAT64,
  low FLOAT64,
  close FLOAT64,
  volume INT64
)
OPTIONS (
  format = 'CSV',
  uris = ['gs://apple-data-raw/raw/date=2026-02-02/aapl.csv'],
  skip_leading_rows = 1,
  field_delimiter = ';'
);