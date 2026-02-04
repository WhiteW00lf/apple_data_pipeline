CREATE OR REPLACE TABLE market_analytics.fct_aapl_daily
PARTITION BY trade_date
AS
SELECT
  trade_date,
  open,
  high,
  low,
  close,
  volume,
  SAFE_DIVIDE(close - open, open) AS daily_return,
  high - low AS daily_range
FROM market_staging.stg_aapl_daily;
