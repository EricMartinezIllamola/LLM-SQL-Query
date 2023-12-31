import streamlit as st
from query_to_df import execute_query_with_column_names

st.title("👩‍🎓Practice Yourself")

if 'question_1' not in st.session_state:
    st.session_state['question_1'] = ""

if 'df_1' not in st.session_state:
    st.session_state['df_1'] = [""]

if 'df_2' not in st.session_state:
    st.session_state['df_2'] = [""]

if 'query_2' not in st.session_state:
    st.session_state['query_2'] = ""

show_df_1 = st.toggle("Show Chatbot Answer")

if show_df_1:
    st.write(st.session_state['question_1'])
    st.dataframe(st.session_state['df_1'], use_container_width=True, hide_index=True)

query_2 = st.text_area("#", label_visibility="hidden", placeholder="Write the SQL query here and press Ctrl+Enter")

if query_2:
    df_2 = execute_query_with_column_names(query_2)
    st.session_state['df_2'] = df_2
    st.session_state['query_2'] = query_2

st.write(st.session_state['query_2'])

st.dataframe(st.session_state['df_2'], use_container_width=True, hide_index=True)

check = st.button("Compare both dataframes")

if check:
    if st.session_state['df_1'].equals(st.session_state['df_2']):
        st.success('Great Job!', icon="✅")
    else:
        st.error('Keep trying!', icon="❌")