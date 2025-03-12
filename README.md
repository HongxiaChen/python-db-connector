# Snowflake Database Connection Package

This package provides a reusable Snowflake database connection using Python. It uses Poetry for dependency management and stores configuration variables in a `.env` file.

## Installation

1. **Clone the repository:**

    ```sh
    git clone git@github.com:polaris-media/python-db-connector.git
    cd db_connector
    ```

2. **Install dependencies using Poetry:**

    ```sh
    poetry install
    ```

## Configuration

Create a `.env` file in the root directory of the project and add the following variables:

```
SNOWFLAKE_USER=<your_snowflake_username>
SNOWFLAKE_PASSWORD=<your_snowflake_password>
SNOWFLAKE_ACCOUNT=<your_snowflake_account>
SNOWFLAKE_WAREHOUSE=<your_snowflake_warehouse>
SNOWFLAKE_DATABASE=<your_snowflake_database>
SNOWFLAKE_SCHEMA=<your_snowflake_schema>
```
## Usage
To use the Snowflake database connection package, follow these steps:

1. Import the package:
```from db_connector import SnowflakeConnector ```
2. Initialize the connector:

## Example
Here is a complete example of how to use the package:
```
from db_connector import SnowflakeConnector

# Initialize the connector
connector = SnowflakeConnector()

# Execute a query
query = "SELECT * FROM your_table"
result = connector.execute_query(query)

# Print the result
print(result)
```
## Contact
For questions or suggestions, contact me: 📧 Email: hongxia.chen06@gmail.com
🔗 GitHub: Hongxia Chen
