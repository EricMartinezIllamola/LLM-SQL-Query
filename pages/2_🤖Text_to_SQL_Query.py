import streamlit as st
from text_to_query import question_to_query

st.title("🤖Text to SQL Query")

if 'df_1' not in st.session_state:
    st.session_state['df_1'] = [""]

if 'query_1' not in st.session_state:
    st.session_state['query_1'] = ""

if 'question_1' not in st.session_state:
    st.session_state['question_1'] = ""

question_1 = st.text_area("#", value=st.session_state['question_1'], label_visibility="hidden", placeholder="Write your question here and press Ctrl+Enter")

if question_1:
    query_1 = question_to_query(question_1)
    # st.session_state['df_1'] = df_1
    st.session_state['query_1'] = query_1
    st.session_state['question_1'] = question_1

st.dataframe(st.session_state['df_1'], use_container_width=True, hide_index=True)

show_query = st.toggle("Wait... Show me the SQL Query!")

if show_query:
    st.write(st.session_state['query_1'])