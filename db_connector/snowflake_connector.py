import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine

# Get the parent folder of the current project (projects/)
BASE_DIR = Path(os.getcwd()).resolve().parent

# Load .env from projects/ folder
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=dotenv_path)

def get_snowflake_engine():
    user = os.getenv('SNOWFLAKE_USER')
    password = os.getenv('SNOWFLAKE_PASSWORD')
    account = os.getenv('SNOWFLAKE_ACCOUNT')
    database = os.getenv('SNOWFLAKE_DATABASE')
    schema = os.getenv('SNOWFLAKE_SCHEMA')
    role = os.getenv('SNOWFLAKE_ROLE')
    warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')

    if not all([user, password, account, database, schema, role, warehouse]):
        raise ValueError("Missing one or more required Snowflake environment variables.")

    connection_string = (f"snowflake://{user}:{password}@{account}/" f"{database}/{schema}?warehouse={warehouse}&role={role}")
    engine = create_engine(connection_string)

    return engine