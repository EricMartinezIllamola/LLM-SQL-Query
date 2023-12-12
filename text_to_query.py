from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
import streamlit as st
import os

from few_shots import few_shots
from query_to_df import execute_query_with_column_names

os.environ["api_key"] = st.secrets["api_key"]

def question_to_query(question):

    instructor_embeddings = HuggingFaceInstructEmbeddings()
    vectordb = FAISS
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        # This is the list of examples available to select from.
        few_shots,
        # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
        instructor_embeddings,
        # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
        vectordb,
        # This is the number of examples to produce.
        k=2
    )

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery"],
        template="Question: {Question}\nSQLQuery: {SQLQuery}",
    )

    sqlite_prompt = """You are a SQLite expert. Given an input question, first create a syntactically correct SQLite query to answer the question.
    You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use date('now') function to get the current date, if the question involves "today".
    Use JOIN to combine rows from multiple tables when needed.

    Use the following format:

    Question: Question here
    SQLQuery: SQL Query
    """

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=sqlite_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info"], #These variables are used in the prefix and suffix
    )

    llm = GooglePalm(google_api_key=os.environ["api_key"], temperature=0)
    db = SQLDatabase.from_uri("sqlite:///InnovaTech.db", sample_rows_in_table_info=3)

    db_chain = create_sql_query_chain(llm, db, prompt=few_shot_prompt)

    #Exaple of final use

    response = db_chain.invoke({"question": question})
    # df = execute_query_with_column_names(response)

    return response