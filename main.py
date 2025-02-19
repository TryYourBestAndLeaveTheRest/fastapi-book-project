from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_router
import httpx

from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}


@app.get("/get-location")
async def get_location(request: Request):
    # Get the user's IP address
    user_ip = request.client.host

    # Fetch geolocation data
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://ip-api.com/json/{user_ip}")
        data = response.json()

    return data
