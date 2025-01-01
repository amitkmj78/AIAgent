import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
import pandas as pd


engine = create_engine(f"mssql+pyodbc://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}?driver=ODBC+Driver+17+for+SQL+Server")
def get_analytics(query):
    result = engine.execute(query)
    data = pd.DataFrame(result.fetchall(), columns=result.keys())
    return data
