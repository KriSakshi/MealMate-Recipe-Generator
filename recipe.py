# recipe.py
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("❌ API key is missing! Please add it in .env")
    exit()

BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

class RecipeGenerator:
    def __init__(self):
        self.api_key = API_KEY

    def get_recipes(self, ingredients, diet, max_time, flavor=None):
        """Fetch recipes from Spoonacular API based on inputs."""
        params = {
            "apiKey": self.api_key,
            "includeIngredients": ingredients,
            "diet": diet if diet.lower() != "none" else None,
            "maxReadyTime": max_time,
            "number": 5,
            "addRecipeInformation": True
        }

        # Remove any None values
        params = {k: v for k, v in params.items() if v}

        if flavor:
            params["query"] = flavor

        try:
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 401:
                print("❌ Unauthorized: API key is invalid or missing.")
                return []
            if response.status_code != 200:
                print(f"❌ Error fetching recipes: {response.status_code}")
                return []

            data = response.json()
            return data.get("results", [])

        except requests.exceptions.RequestException as e:
            print("❌ Network error:", e)
            return []

    def get_recipe_instructions(self, recipe_id):
        """Fetch full recipe instructions for a given recipe ID"""
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        params = {"apiKey": self.api_key}
        try:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print(f"❌ Error fetching recipe details: {response.status_code}")
                return "Instructions not available."
            data = response.json()
            return data.get("instructions") or "No instructions provided."
        except requests.exceptions.RequestException as e:
            print("❌ Network error:", e)
            return "Instructions not available."




   
