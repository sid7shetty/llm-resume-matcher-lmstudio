# LLM-Powered Resume Matcher with LM Studio

This project is a local LLM resume matcher that uses LM Studio for obtaining text embeddings and generating feedback. It compares resumes with job descriptions by computing cosine similarity between their embeddings and optionally provides feedback via a local chat model.

## Features

- **Local Embedding Extraction:** Uses LM Studio's API to get embeddings.
- **Resume Matching:** Computes cosine similarity between resume and job description embeddings.
- **Feedback Generation:** (Optional) Provides recruiter-like feedback using a local LLM.
- **Web Interface:** A simple Streamlit app for interactive usage.

## Setup

1. **Clone the repository and navigate into the project directory:**

   ```bash
   git clone <repository_url>
   cd llm-resume-matcher-lmstudio
