import streamlit as st 
import duckdb
import plotly.express as px

st.title("Dashboard E-commerce")

conn = duckdb.connect("data/ecommerce.duckdb")
df_gold = conn.execute("SELECT * FROM gold_monthly_sales").df()

st.metric("Chiffre d'Affaire Total", f"{df_gold['total_revenue'].sum():,.2f}€")
st.metric("Commandes Livrées", f"{df_gold['total_orders'].sum()}")

fig = px.line(df_gold, x = "sales_month", y = "total_revenue", color = "product_category", title = "Évolution du Chiffre d'Affaire par Catégorie")
st.plotly_chart(fig, use_container_width = True)

conn.close()