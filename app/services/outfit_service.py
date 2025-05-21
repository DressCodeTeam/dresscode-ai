from openai import OpenAI
from config import AI_API_KEY as API_KEY
import json

BASE_URL = "https://api.thehive.ai/api/v3/"

GENERATIVE_MODEL = "meta-llama/llama-3.1-8b-instruct"


client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def create_prompt(garments, nb_outfits, style, sex, weather):
    prompt = f"""
  **Requirements:**
  * Output must be valid and strictly formatted JSON.
  * Only choose from the provided taxonomy.
  * Do not include any explanation or text outside the JSON result.

  You are a fashion stylist AI.

  Here is my wardrobe, provided in JSON format, where each item has a garment_id and a description:
  {garments}

  Your task is to generate {nb_outfits} complete outfit suggestions based only on the garment descriptions. The style of the outfits should match the theme: {style}.

  Take into account the current weather conditions: {weather} and the sex: {sex}.

  Each outfit should be suitable for the weather and consistent with the requested style.
  Return the output in strict JSON format with only the garment_id.
  """
    return prompt


def call_generetive_model(prompt):
    model = GENERATIVE_MODEL
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000,
    )

    return response.choices[0].message.content


def generate_outfits_from_ai(garments, nb_outfits, style, sex, weather):
    prompt = create_prompt(garments, nb_outfits, style, sex, weather)
    outfits = call_generetive_model(prompt)

    json_outfits = None
    try:
        formated_outfits = []
        json_tmp = json.loads(outfits)
        for outfit_name in json_tmp.keys():
            formated_outfits.append(
                {
                    "name": outfit_name,
                    "garments": json_tmp[outfit_name],
                }
            )
        json_outfits = formated_outfits
    except:
        json_outfits = None

    print(f"AI Outfits: {json_outfits}")
    return json_outfits
