SELECT
  COUNT(*) AS rows,
  MIN(trade_date) AS start_date,
  MAX(trade_date) AS end_date
FROM market_analytics.fct_aapl_daily;
