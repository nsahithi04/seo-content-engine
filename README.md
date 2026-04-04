# SEO AI Backend (MVP - Keyword + SERP)

## Overview

This project is a backend system for generating SEO-focused content ideas.

Current functionality:

- Accepts a domain and target audience
- Generates high-intent search keywords using Gemini
- Fetches real Google search results using SERP API
- Returns structured keyword + SERP data

---

## Project Structure

```
app/
├── index.py              # FastAPI entry point
├── routes/               # API routes
├── controllers/          # Request handling
├── pipelines/            # Workflow orchestration
├── services/             # LLM + SERP integrations
├── schemas/              # Request/response models
├── config/               # Configuration (env, DB later)
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/nsahithi04/seo-content-engine
cd seo-content-engine
```

---

### 2. Create virtual environment

```
python3 -m venv venv
```

---

### 3. Activate environment

```
source venv/bin/activate
```

---

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

### 5. Create `.env` file (in root)

```
GEMINI_API_KEY=your_gemini_api_key
SERP_API_KEY=your_serpapi_key
```

---

## Running the Server

```
uvicorn app.index:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

API docs:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST `/keywords`

#### Request Example

```
{
  "domain": "nike.com",
  "audience": "athletes"
}
```

---

#### Response

```
{
  "data": [
    {
      "keyword": "...",
      "serp_results": [
        {
          "title": "...",
          "link": "...",
          "snippet": "..."
        }
      ]
    }
  ]
}
```

---

## Pipeline Flow

```
Input (domain, audience)
→ Generate keywords (LLM - Gemini)
→ Fetch SERP results (SerpAPI)
→ Return structured response
```

---

## Next Steps

- Extract headings and structure from SERP results
- Generate content outlines using LLM
- Add content generation pipeline
- Store results in database
- Add tracking and optimization loop
