import pandas as pd
import sqlite3

def execute_query_with_column_names(query):
    connection = sqlite3.connect('InnovaTech.db')
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        column_names = [description[0] for description in cursor.description]
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=column_names)
        return df

    finally:
        cursor.close()
        connection.close()

def tables_names():
    query = "SELECT name FROM sqlite_sequence"
    connection = sqlite3.connect('InnovaTech.db')
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        table_names = [row[0] for row in result]
        return table_names

    finally:
        cursor.close()
        connection.close()

def table_schema(table):
    query = "SELECT sql FROM sqlite_master WHERE type='table' AND name = ?"
    connection = sqlite3.connect('InnovaTech.db')
    cursor = connection.cursor()

    try:
        cursor.execute(query, (table,))
        result = cursor.fetchall()
        return result

    finally:
        cursor.close()
        connection.close()