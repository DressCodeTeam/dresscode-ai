import httpx
from PIL import Image
from io import BytesIO
from fastapi import HTTPException


async def download_image(url: str) -> Image.Image:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

        return Image.open(BytesIO(response.content))
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Image download or parsing failed: {e}"
        )
