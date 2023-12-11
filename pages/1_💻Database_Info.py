import streamlit as st
from query_to_df import execute_query_with_column_names, tables_names, table_schema

st.title("💻Database Info")

st.subheader("Check out the tables in the database:")

query = "SELECT name, seq AS rows FROM sqlite_sequence"
df_1 = execute_query_with_column_names(query)

st.dataframe(df_1, width= 400, hide_index=True)

st.markdown('***')

st.subheader("Check out the columns of each table:")

tables = tables_names()
option = st.selectbox('#', tables)

if option:
    st.write(table_schema(option))