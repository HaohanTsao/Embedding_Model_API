import os
import logging
import functions_framework
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import torch

from src.services.supabase.table_functions import insert_table


load_dotenv()
model_path = os.getenv("EMBEDDING_MODEL_PATH")
model = SentenceTransformer(model_path)
table_name = os.getenv("EMBEDDING_TABLE_NAME")


@functions_framework.http
def embedding(req):

    try:
        req = req.get_json(silent=True)
        post_id = req["record"].get("id")
        raw_content = req["record"].get("content_raw")
        raw_title = req["record"].get("title_raw")

        title_embedding = model.encode(raw_title, normalize_embeddings=True)
        content_embedding = model.encode(raw_content, normalize_embeddings=True)

        embedding_data = {
            "post_id": post_id,
            "title_embedding": title_embedding.tolist(),
            "content_embedding": content_embedding.tolist(),
        }

        response = insert_table(table_name, embedding_data)

        return response

    except Exception as e:
        logging.error(e)
