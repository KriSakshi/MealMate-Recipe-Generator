# main.py
from recipe import RecipeGenerator

def main():
    print("🍳 Welcome to MealMate — Your Smart Recipe Buddy!\n")

    ingredients = input("Enter ingredients you have (comma separated): ").strip()
    diet = input("Enter your diet (vegetarian, vegan, keto, none): ").strip()
    max_time = input("Enter max cooking time in minutes: ").strip()
    flavor = input("Do you prefer spicy, sweet, or savory? (optional): ").strip()

    generator = RecipeGenerator()
    recipes = generator.get_recipes(ingredients, diet, max_time, flavor)

    if not recipes:
        print("\nNo recipes found! Try changing ingredients, diet, time, or flavor.")
        return

    print("\n✨ Found some recipes for you:\n")
    for idx, r in enumerate(recipes, start=1):
        print(f"{idx}. {r['title']}")
        print(f"   Recipe Link: https://spoonacular.com/recipes/{r['title'].replace(' ', '-')}-{r['id']}\n")

    choice = input("Enter the number of the recipe you want to view (or press Enter to exit): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(recipes):
        selected = recipes[int(choice)-1]
        instructions = generator.get_recipe_instructions(selected['id'])
        print(f"\n🍲 Recipe for {selected['title']}:\n")
        print(instructions)
    else:
        print("Goodbye! 👋")

if __name__ == "__main__":
    main()
