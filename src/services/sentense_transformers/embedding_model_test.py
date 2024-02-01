# %%
import os
from sentence_transformers import SentenceTransformer
import torch
from dotenv import load_dotenv

load_dotenv()

model_path = os.getenv("EMBEDDING_MODEL_PATH")

m = SentenceTransformer(model_path)
sentences = ["美國錄取心得 ", "真的很煩的室友😠", "MSBA申請心得(二)"]

sentence_embeddings = m.encode(
    sentences, normalize_embeddings=True, convert_to_tensor=True
)
print("Sentence embeddings:")
print(sentence_embeddings)

# %%
import torch.nn.functional as F

cosine_similarity = F.cosine_similarity(
    sentence_embeddings[2], sentence_embeddings[1], dim=0
)
print("Cosine-Similarity of two sentences:")
print(cosine_similarity)
