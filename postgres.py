# CREATE TODO_APP DATABASE WITH POSTGRES
import psycopg2
from psycopg2 import OperationalError


def connect(db_name, db_user, db_password, db_host, db_port):
    connection_status = None
    try:
        connection_status = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"We couldn`t connect to the database: The error '{e}' occurred")
    return connection_status


connection = connect("postgres", "postgres", "ope.david*200", "127.0.0.1", "5432")


def query_execute(connector, query):
    connector.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


# create_database_query = "CREATE DATABASE  color_app"
#
# query_execute(connection, create_database_query)


create_table = """
CREATE TABLE color_table (
  id SERIAL PRIMARY KEY,
  color TEXT NOT NULL,
  frequency NUMERIC NOT NULL
)
"""


def insert_todo(list_query,connection):
    query_execute(connection, create_table)

    user_records = ", ".join(["%s"] * len(list_query))

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query, list_query)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


connection.close()