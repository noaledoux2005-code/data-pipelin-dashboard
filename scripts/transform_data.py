import duckdb

conn = duckdb.connect("data/ecommerce.duckdb")

conn.execute("""
CREATE OR REPLACE TABLE silver_orders AS 
SELECT 
    order_id,
    customer_id,
    CAST(order_date AS DATE) AS order_date,
    product_category,
    quantity,
    unit_price,
    ROUND(quantity * unit_price, 2) AS total_amount,
    status
FROM raw_orders; """)

conn.execute("""
CREATE OR REPLACE TABLE gold_monthly_sales AS 
SELECT DATE_TRUNC('month', order_date) AS sales_month,
    product_category,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM silver_orders
WHERE status = 'Livré'
GROUP BY 1, 2
ORDER BY sales_month ASC, total_revenue DESC; """)

print(conn.execute("SELECT * FROM gold_monthly_sales LIMIT 5").df())

conn.close()