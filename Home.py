import streamlit as st

st.set_page_config(page_title="InnovaTech", page_icon="💻")

st.title("💻InnovaTech SQL Database")

st.write("InnovaTech is a fake wholesale company for electronic devices. We have created a SQLite database that contains information about orders, products, etc.")
st.write("With this app, you can ask questions in natural language to the database. In response, you will get both the answer to your question (as a dataframe) and the SQL query used to get that answer.")
st.write("You can also use this app to practice, test, and improve your SQL knowledge.")

st.subheader("💻Database Info")

st.write("In this section, you can check out some basic information about the SQLite database: tables, columns, etc.")

st.subheader("🤖Text to SQL Query")

st.write("In this section, you can ask questions in natural language, and the chatbot will do the hard work for you!")
st.write("The bot can answer very challenging questions, but not being ambiguous is always a good idea. If the bot is having trouble, try to reformulate your question.")

st.subheader("👩‍🎓Practice Yourself")

st.write("It's time to test your SQL skills! Write a SQL query and get a dataframe as a result.")
st.write("The idea here is as follows:")
st.markdown("- Ask any question in the '🤖Text to SQL Query' section, but don't look at the SQL query yet!")
st.markdown("- Go to the '👩‍🎓Practice Yourself' section and try to get the same dataframe by yourself. With the 'Show Chatbot Dataframe' button, you can show/hide the dataframe provided by the bot.")
st.markdown("- Click on the 'Compare both dataframes' button to check if both dataframes are equal or not.")
st.write("Feel free to explore the app on your own!")