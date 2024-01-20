from breakfasts import breakfasts
from dinners import dinners
import random
import calendar

days = [day.upper() for day in calendar.day_name]
all_ingredients = []


for day in range(7):
    breakfast = random.choice(breakfasts)
    dinner = random.choice(dinners)
    print(f'{days[day]}:')
    print(f"Breakfast: {breakfast['name']}")
    print(f"Dinner: {dinner['name']}\n")
    all_ingredients.extend(breakfast['ingredients'] + dinner['ingredients'])

unique_ingredients = list(set(all_ingredients))
print('Ingredients:')
for ingredient in unique_ingredients:
    print(f'- {ingredient}')
