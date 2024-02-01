import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_API_URL")
key: str = os.environ.get("SUPABASE_API_SECRET_KEY")
supabase: Client = create_client(url, key)


def update_table(table_name: str, update_info: dict, conditions: dict):
    try:
        query = supabase.table(table_name).update(update_info)

        for column, value in conditions.items():
            query = query.eq(column, value)

        data, count = query.execute()

        logging.info(
            f"Successfully updated {update_info} \n with condition {conditions} in table {table_name}"
        )
    except Exception as e:
        logging.error(f"Error updating table {table_name}: {str(e)}")


def get_table(table_name: str, conditions: dict, columns: list = []):
    try:
        if columns:
            columns_str = ", ".join(columns)
            query = supabase.table(table_name).select(columns_str)
        else:
            query = supabase.table(table_name).select("*")

        for column, value in conditions.items():
            query = query.eq(column, value)

        data, count = query.execute()

        logging.info(
            f"Successfully retrieved {count} rows from table {table_name} with condition {conditions}"
        )

        return data

    except Exception as e:
        logging.error(f"Error retrieving table {table_name}: {str(e)}")

        return {}
