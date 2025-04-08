import os
from typing import List

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load environment variables
load_dotenv()

app = FastAPI(title="GenAI News Assistant MCP Server")


class SearchNewsRequest(BaseModel):
    query: str
    language: str = "en"
    pageSize: int = 5


class Article(BaseModel):
    title: str
    description: str
    url: str
    source_name: str
    published_at: str


class SearchNewsResponse(BaseModel):
    articles: List[Article]


@app.post("/search_news", response_model=SearchNewsResponse)
async def search_news(request: SearchNewsRequest):
    """
    Search for recent news articles matching a specific query.
    """
    # TODO: Implement NewsAPI.org integration
    raise HTTPException(status_code=501, detail="Not implemented")


class ExtractInfoRequest(BaseModel):
    query: str
    language: str = "en"


class ExtractInfoResponse(BaseModel):
    result: dict


@app.post("/extract_information_from_article", response_model=ExtractInfoResponse)
async def extract_information_from_article(request: ExtractInfoRequest):
    """
    Extract structured information from a news article.
    """
    # TODO: Implement NewsAPI.org and LLM integration
    raise HTTPException(status_code=501, detail="Not implemented")


class ExtractKeyInfoRequest(BaseModel):
    query: str
    language: str = "en"
    max_articles_to_analyze: int = 5


class ExtractKeyInfoResponse(BaseModel):
    status: str
    result: dict


@app.post("/extract_key_info_and_sentiment", response_model=ExtractKeyInfoResponse)
async def extract_key_info_and_sentiment(request: ExtractKeyInfoRequest):
    """
    Analyze news articles for key entities and sentiment.
    """
    # TODO: Implement NewsAPI.org and LLM integration
    raise HTTPException(status_code=501, detail="Not implemented")


if __name__ == "__main__":
    # Verify environment variables
    required_env_vars = ["NEWS_API_KEY", "LLM_API_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=3000)
