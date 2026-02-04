SELECT trade_date,volume FROM `market-data-analytics-486307.market_analytics.fct_aapl_daily` 
GROUP BY trade_date,volume
ORDER BY volume DESC
LIMIT 5;
