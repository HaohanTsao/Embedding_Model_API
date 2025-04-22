# Embedding Model API

A cloud function that generates and stores embeddings for content received from Supabase webhooks.

## Overview

This project deploys a Google Cloud Function that:
1. Receives webhook requests from Supabase containing post data
2. Extracts the post_id, title, and content
3. Generates embeddings for both the title and content using a sentence transformer model
4. Stores the post_id with its corresponding embeddings in a Supabase table

## Architecture

```
├── main.py                # Entry point for the cloud function
├── src/                   # Source code
│   ├── functions/
│   │   └── embedding.py   # Core embedding functionality
│   └── services/
│       └── supabase/
│           └── table_functions.py  # Supabase operations
├── embed_current_post.py  # Utility to embed existing posts
├── deploy.sh              # Deployment script
└── requirements.txt       # Dependencies
```

## Setup

### Prerequisites

- Python 3.9+
- Google Cloud CLI
- A Supabase account with API credentials
- Sentence-transformers model

### Environment Variables

Create a `.env` file with the following variables:

```
SUPABASE_API_URL=your_supabase_url
SUPABASE_API_SECRET_KEY=your_supabase_key
EMBEDDING_MODEL_PATH=your_model_path
EMBEDDING_TABLE_NAME=your_embedding_table_name
```

### Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Deploy to Google Cloud

Run the deployment script:

```bash
chmod +x deploy.sh
./deploy.sh
```

This will deploy the cloud function to Google Cloud in the `asia-east1` region.

### Embedding Existing Posts

To generate embeddings for all existing posts:

```bash
python embed_current_post.py
```

### Webhook Integration

Configure a Supabase webhook to trigger on post creation/update events. The webhook should point to your deployed cloud function URL and include the following payload:

```json
{
  "record": {
    "id": "post_id",
    "title_raw": "post title",
    "content_raw": "post content"
  }
}
```

## Database Schema

The embedding table should have the following structure:

- `post_id`: Foreign key to the posts table
- `title_embedding`: Vector array for the title embedding
- `content_embedding`: Vector array for the content embedding

## Note
This project is in production for [OfferLand](https://offerland.cc/)
