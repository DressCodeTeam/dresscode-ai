from pydantic import BaseModel
from typing import List


class Garment(BaseModel):
    garment_id: int
    subcategory: str
    description: str


class OutfitGenerationRequest(BaseModel):
    garments: List[Garment]
    nb_outfits: int
    style: str
    sex: str
    weather: str


class Outfit(BaseModel):
    name: str
    garments: List[int]


# class OutfitGenerationResponse(BaseModel):
#     outfits: List[Outfit]
