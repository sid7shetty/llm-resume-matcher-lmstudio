import requests

def get_embedding(text):
    response = requests.post(
        "http://localhost:1234/v1/embeddings",
        headers={"Content-Type": "application/json"},
        json={
            "input": text,
            "model": "text-embedding-bge-small-en-v1.5"  # or whichever model you're using
        }
    )
    
    print("DEBUG - Raw response:", response.json())  # Add this line

    # Now handle missing 'data' key safely
    result = response.json()
    if "data" not in result:
        raise ValueError(f"Embedding API error: {result}")
    
    return result["data"][0]["embedding"]
