from typing import List
from models.image import Subcategory
from config import AI_API_KEY as API_KEY
from openai import OpenAI
import json

AI_BASE_URL = "https://api.thehive.ai/api/v3/"

VISION_MODEL = "meta-llama/llama-3.2-11b-vision-instruct"


client = OpenAI(base_url=AI_BASE_URL, api_key=API_KEY)


# This is where you'd call a real AI API, e.g., DeepAI, HuggingFace, etc.
async def get_image_description(
    image_url: str, subcategories: List[Subcategory]
) -> dict:
    prompt = create_prompt(subcategories)
    description = call_vision_model(prompt, image_url)
    print(f"AI Description: {description}")
    json_description = None
    try:
        json_description = json.loads(description)
    except:
        json_description = {
            "subcategory_id": None,
            "description": "not a clothing item",
        }
    return json_description


def create_prompt(subcategories):
    prompt = f"""
  **Requirements:**
  * Output must be valid and strictly formatted JSON.
  * Only choose from the provided taxonomy.
  * Do not include any explanation or text outside the JSON result.

  Analyze the provided image and determine whether at least 80% of the image content depicts a clothing item.

  If so, return the result in strict JSON format with the following fields: subcategory (id) and description (A concise description of the item including material, color, and style if detectable)

  The `subcategory` must be selected from the following taxonomy:
  {subcategories}

  If the image is not at least 80% a clothing item, return the following JSON:
  {{ "subcategory_id": null, "description": "not a clothing item" }}
  """
    return prompt


def call_vision_model(prompt, img):
    model = VISION_MODEL
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": img}},
                ],
            }
        ],
        temperature=0.7,
        max_tokens=1000,
    )

    return response.choices[0].message.content
