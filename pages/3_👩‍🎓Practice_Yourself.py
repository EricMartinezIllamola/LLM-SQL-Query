import streamlit as st
from query_to_df import execute_query_with_column_names

st.title("👩‍🎓Practice Yourself")

if 'df_1' not in st.session_state:
    st.session_state['df_1'] = [""]

if 'df_2' not in st.session_state:
    st.session_state['df_2'] = [""]

show_df_1 = st.toggle("Show Chatbot Dataframe")

if show_df_1:
    st.dataframe(st.session_state['df_1'], use_container_width=True, hide_index=True)

question_2 = st.text_area("#", label_visibility="hidden", placeholder="Write the SQL query here and press Ctrl+Enter")

if question_2:
    df_2 = execute_query_with_column_names(question_2)
    st.session_state['df_2'] = df_2

st.dataframe(st.session_state['df_2'], use_container_width=True, hide_index=True)

check = st.button("Compare both dataframes")

if check:
    if st.session_state['df_1'].equals(st.session_state['df_2']):
        st.success('Great Job!', icon="✅")
    else:
        st.error('Keep trying!', icon="❌")