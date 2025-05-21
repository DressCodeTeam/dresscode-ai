from typing import Optional
from pydantic import BaseModel, HttpUrl, Field
from typing import List


# ---------- Request Models ----------
class Subcategory(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Winter")


class ImageAnalysisRequest(BaseModel):
    image_url: HttpUrl = Field(
        ...,
        example="https://example.com/image.jpg",
        description="A publicly accessible image URL",
    )
    subcategories: List[Subcategory] = Field(
        ..., description="List of subcategories to analyze against the image"
    )


# ---------- Response Models ----------
class SubcategoryDescription(BaseModel):
    subcategory_id: Optional[int] = Field(..., example=1)
    description: str = Field(
        ..., example="This image contains a winter jacket with a fur hood."
    )
