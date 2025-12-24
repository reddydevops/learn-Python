import os
import sys
from typing import Optional

import snowflake.connector
from snowflake.connector import SnowflakeConnection


def get_connection(
    account: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    warehouse: Optional[str] = None,
    database: Optional[str] = None,
    schema: Optional[str] = None,
    role: Optional[str] = None,
) -> SnowflakeConnection:
    """Establish a connection to Snowflake using provided or environment variables."""
    account = account or os.environ.get("SNOWFLAKE_ACCOUNT")
    user = user or os.environ.get("SNOWFLAKE_USER")
    password = password or os.environ.get("SNOWFLAKE_PASSWORD")
    warehouse = warehouse or os.environ.get("SNOWFLAKE_WAREHOUSE")
    database = database or os.environ.get("SNOWFLAKE_DATABASE")
    schema = schema or os.environ.get("SNOWFLAKE_SCHEMA")
    role = role or os.environ.get("SNOWFLAKE_ROLE")

    if not all([account, user, password]):
        raise RuntimeError(
            "Missing required Snowflake credentials. Set SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, and SNOWFLAKE_PASSWORD."
        )

    conn = snowflake.connector.connect(
        account=account,
        user=user,
        password=password,
        warehouse=warehouse,
        database=database,
        schema=schema,
        role=role,
    )
    return conn


def execute_sql_file(conn: SnowflakeConnection, sql_file_path: str) -> None:
    """Execute SQL statements from a file."""
    with open(sql_file_path, 'r') as f:
        sql_script = f.read()

    # Split by semicolon and execute each statement
    statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]
    with conn.cursor() as cursor:
        for stmt in statements:
            if stmt:
                cursor.execute(stmt)
                print(f"Executed: {stmt[:50]}...")


def deploy_sql(
    sql_file: str,
    account: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None,
    warehouse: Optional[str] = None,
    database: Optional[str] = None,
    schema: Optional[str] = None,
    role: Optional[str] = None,
):
    """Deploy SQL to Snowflake by executing a SQL file."""
    conn = None
    try:
        conn = get_connection(account, user, password, warehouse, database, schema, role)
        execute_sql_file(conn, sql_file)
        print("SQL deployment successful.")
    except Exception as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Deploy SQL to Snowflake.")
    parser.add_argument("--sql-file", required=True, help="Path to the SQL file to execute.")
    parser.add_argument("--account", help="Snowflake account (or set SNOWFLAKE_ACCOUNT)")
    parser.add_argument("--user", help="Snowflake user (or set SNOWFLAKE_USER)")
    parser.add_argument("--password", help="Snowflake password (or set SNOWFLAKE_PASSWORD)")
    parser.add_argument("--warehouse", help="Snowflake warehouse (or set SNOWFLAKE_WAREHOUSE)")
    parser.add_argument("--database", help="Snowflake database (or set SNOWFLAKE_DATABASE)")
    parser.add_argument("--schema", help="Snowflake schema (or set SNOWFLAKE_SCHEMA)")
    parser.add_argument("--role", help="Snowflake role (or set SNOWFLAKE_ROLE)")

    args = parser.parse_args()

    deploy_sql(
        args.sql_file,
        args.account,
        args.user,
        args.password,
        args.warehouse,
        args.database,
        args.schema,
        args.role,
    )