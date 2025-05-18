from embedding import get_embedding
from sklearn.metrics.pairwise import cosine_similarity
import requests

def get_match_score(resume_text, jd_text):
    resume_emb = get_embedding(resume_text)
    jd_emb = get_embedding(jd_text)
    similarity = cosine_similarity([resume_emb], [jd_emb])[0][0]
    return round(similarity * 100, 2)




def get_llm_feedback(resume, jd):
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        headers={"Content-Type": "application/json"},
        json={
            "model": "mistralai_-_mistral-7b-instruct-v0.2",  # ✅ Must match LM Studio model ID exactly
            "messages": [
                {
                    "role": "user",
                    "content": f"""You're a recruiter. Compare the resume and job description below, and give detailed feedback:

Resume:
{resume}

Job Description:
{jd}

Evaluate how well the candidate fits the job, and suggest improvements."""
                }
            ],
            "temperature": 0.7
        }
    )

    result = response.json()
    print("DEBUG - Chat Response:", result)

    if "choices" not in result:
        return f"⚠️ Chat model returned error: {result}"

    return result["choices"][0]["message"]["content"]


