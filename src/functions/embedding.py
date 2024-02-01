import os
import logging
import functions_framework
from dotenv import load_dotenv

from src.services.supabase.table_functions import get_table

load_dotenv()


"""
supabase webhook payload:

type InsertPayload = {
  type: 'INSERT'
  table: string
  schema: string
  record: TableRecord<T>
  old_record: null
}
type UpdatePayload = {
  type: 'UPDATE'
  table: string
  schema: string
  record: TableRecord<T>
  old_record: TableRecord<T>
}
type DeletePayload = {
  type: 'DELETE'
  table: string
  schema: string
  record: null
  old_record: TableRecord<T>
}
"""


@functions_framework.http
def embedding(req):
    pass
