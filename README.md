# MealMate — Your Smart Recipe Buddy! 🍳
MealMate is a Python console application that generates recipes based on the ingredients you have, your diet (vegetarian, vegan, keto, or none), maximum cooking time, and optional flavor preference (spicy, sweet, or savory). It displays full cooking instructions directly in the console, making it perfect for beginners and anyone looking for quick meal ideas.

**Features:** Suggests recipes based on user inputs; supports diet and flavor filters; displays full recipe instructions in console; beginner-friendly Python code; uses Spoonacular API for real recipe data.

**Technologies Used:** Python 3.x; `requests` (for API calls); `python-dotenv` (for managing API keys securely); Spoonacular API (for recipe data).

**Setup Instructions:** 
1.Clone the repository:  
   git clone https://github.com/krisakshi/MealMate-Recipe-Generator.git
   cd MealMate-Recipe-Generator

2.Create and activate a virtual environment:
    -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate


3.Install dependencies:
    pip install -r requirements.txt


4.Create a .env file in the project root with your Spoonacular API key:
    API_KEY=your_spoonacular_api_key

5.Run the application:
    python main.py


Example Run:

🍳 Welcome to MealMate — Your Smart Recipe Buddy!

Enter ingredients: rice, paneer
Enter diet: vegetarian
Enter max cooking time: 30
Do you prefer spicy, sweet, or savory? spicy

✨ Found some recipes for you:
1. Spicy Paneer Rice
2. Indian Spicy Paneer Curry

Select a recipe to view instructions: 1

🍲 Recipe for Spicy Paneer Rice:
1. Heat oil in a pan...
2. Add spices...
3. Cook rice and paneer...
4. Serve hot!

Credits: Recipe data provided by [Spoonacular API](https://spoonacular.com/food-api). 
Python packages used: requests, python-dotenv. 
