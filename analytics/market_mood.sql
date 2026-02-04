SELECT
  CASE
    WHEN daily_return > 0 THEN 'Positive'
    ELSE 'Negative'
  END AS day_type,
  COUNT(*) AS days
FROM market_analytics.fct_aapl_daily
GROUP BY day_type;
