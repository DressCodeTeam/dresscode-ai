from fastapi import APIRouter, HTTPException
from models.generate_outfits import OutfitGenerationRequest, Outfit
from services.outfit_service import generate_outfits_from_ai
from typing import List

router = APIRouter()


@router.post(
    "/generate",
    response_model=List[Outfit],
    tags=["Outfit Generator"],
)
async def generate_outfits(payload: OutfitGenerationRequest):
    outfits = generate_outfits_from_ai(
        payload.garments,
        payload.nb_outfits,
        payload.style,
        payload.sex,
        payload.weather,
    )

    if outfits is None:
        raise HTTPException(status_code=502, detail=f"AI response parsing failed")

    return outfits
