from src.functions.embedding import embedding
from dotenv import load_dotenv

load_dotenv()


def main(req):
    response = embedding(req)
    return response


if __name__ == "__main__":
    main()
