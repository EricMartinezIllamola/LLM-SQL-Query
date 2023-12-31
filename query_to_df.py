import pandas as pd
import sqlite3
import streamlit as st

def execute_query_with_column_names(query):
    with sqlite3.connect('file:InnovaTech.db?mode=ro', uri=True) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            result = cursor.fetchall()
            df = pd.DataFrame(result, columns=column_names)
            return df

        except sqlite3.Error as e:
            # Handle SQLite-specific errors
            error_message = str(e)
            st.error(f"SQLite Error: {error_message}")

        except Exception as e:
            # Handle other exceptions
            error_message = str(e)
            st.error(f"Error: {error_message}")

        finally:
            cursor.close()

def tables_names():
    query = "SELECT name FROM sqlite_sequence"
    with sqlite3.connect('file:InnovaTech.db?mode=ro', uri=True) as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            table_names = [row[0] for row in result]
            return table_names

        finally:
            cursor.close()

def table_schema(table):
    query = "SELECT sql FROM sqlite_master WHERE type='table' AND name = ?"
    with sqlite3.connect('file:InnovaTech.db?mode=ro', uri=True) as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(query, (table,))
            result = cursor.fetchall()
            return result

        finally:
            cursor.close()