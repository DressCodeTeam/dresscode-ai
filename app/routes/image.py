from fastapi import APIRouter
from typing import List
from models.image import ImageAnalysisRequest, SubcategoryDescription
from services.image_analyzer import get_image_description

router = APIRouter()


@router.post(
    "/analyze",
    response_model=SubcategoryDescription,
    summary="Analyze image with subcategories",
    description="Analyzes the image and returns a description for each subcategory provided.",
    tags=["Image Analysis"],
)
async def analyze_image(request: ImageAnalysisRequest):
    """
    Analyze the given image URL and generate a description for each provided subcategory.

    - **image_url**: Publicly accessible image link
    - **subcategories**: List of objects with `id` and `name` representing subcategories
    """
    return await get_image_description(str(request.image_url), request.subcategories)
