import streamlit as st

st.set_page_config(page_title="InnovaTech", page_icon="💻")

st.title("💻InnovaTech SQL Database")

st.write("InnovaTech is a fictitious wholesale company for electronic devices. We've created a SQLite database containing information about orders, products, etc.")
st.write("Ask questions in natural language, and the app will provide both the answer (as a dataframe) and the SQL query used to provide that answer.")
st.write("Practice, test, and improve your SQL skills!")

st.subheader("💻Database Info")

st.write("Explore basic information about the SQLite database: tables, columns, etc.")

st.subheader("🤖Text to SQL Query")

st.write("Ask questions in natural language, and let the chatbot do the hard work!")
st.write("The bot can answer very challenging questions, but not being ambiguous is always a good idea. If the bot struggles, try rephrasing your question for better results.")

st.subheader("👩‍🎓Practice Yourself")

st.write("Test your SQL skills! Write a query and get a dataframe as a result.")
st.write("Follow these steps:")
st.markdown("- Ask a question in '🤖Text to SQL Query', but don't look at the SQL query yet!")
st.markdown("- In '👩‍🎓Practice Yourself', try to replicate the dataframe by yourself. Use the 'Show Chatbot Dataframe' button to reveal/hide the bot's result.")
st.markdown("- Click 'Compare both dataframes' to check if both dataframes are equal or not.")
st.write("Feel free to explore the app on your own!")