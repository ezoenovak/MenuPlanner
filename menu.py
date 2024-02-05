from breakfasts import breakfasts
from dinners import dinners
import random
import calendar

days = [day.upper() for day in calendar.day_name]
all_ingredients = []

selected_breakfasts = set()
selected_dinners = set()

for day in range(7):
    available_breakfasts = [b for b in breakfasts if b['name'] not in selected_breakfasts]
    breakfast = random.choice(available_breakfasts)
    selected_breakfasts.add(breakfast['name'])
    available_dinners = [d for d in dinners if d['name'] not in selected_dinners]
    dinner = random.choice(available_dinners)
    selected_dinners.add(dinner['name'])
    print(f'{days[day]}:')
    print(f"Breakfast: {breakfast['name']}")
    print(f"Dinner: {dinner['name']}\n")
    all_ingredients.extend(breakfast['ingredients'] + dinner['ingredients'])

unique_ingredients = list(set(all_ingredients))
print('Ingredients:')
for ingredient in unique_ingredients:
    print(f'- {ingredient}')
