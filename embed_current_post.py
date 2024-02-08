# %%
from src.services.supabase.table_functions import get_table, insert_table
import os
from sentence_transformers import SentenceTransformer
import torch
from dotenv import load_dotenv

load_dotenv()

model_path = os.getenv("EMBEDDING_MODEL_PATH")
table_name = os.getenv("EMBEDDING_TABLE_NAME")

m = SentenceTransformer(model_path)

# get all current post
post_data = get_table(table_name="posts", columns=["id", "title_raw", "content_raw"])

# %%
embedding_data = []
for i, post in enumerate(post_data.data):
    temp = {}
    temp["post_id"] = post["id"]
    temp["title_embedding"] = m.encode(post["title_raw"]).tolist()
    temp["content_embedding"] = m.encode(post["content_raw"]).tolist()

    embedding_data.append(temp)

# %%
response = insert_table(table_name=table_name, insert_info=embedding_data[0])

# %%
for i in range(1, len(embedding_data)):
    try:
        response = insert_table(
            table_name=table_name, insert_info=embedding_data[i]
        )
        print("success")
    except:
        print("failed", f"post_id {embedding_data[i].get('post_id')}")
