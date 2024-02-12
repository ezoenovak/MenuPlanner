from breakfasts import breakfasts, weekend_breakfasts as w_breakfasts
from dinners import dinners
import random
import calendar

days = [day.upper() for day in calendar.day_name]
all_ingredients = []

selected_breakfasts = set()
selected_dinners = set()
selected_weekend_breakfasts = set()

# for day in range(7):
for day in range(5):
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

for day in range(5, 7):
    available_weekend_breakfasts = [wb for wb in w_breakfasts if wb['name'] not in selected_weekend_breakfasts]
    weekend_breakfast = random.choice(available_weekend_breakfasts)
    selected_weekend_breakfasts.add(weekend_breakfast['name'])
    print(f'{days[day]}:')
    print(f"Weekend breakfast: {weekend_breakfast['name']}\n")
    all_ingredients.extend(weekend_breakfast['ingredients'])


unique_ingredients = list(set(all_ingredients))
print('Ingredients:')
for ingredient in unique_ingredients:
    print(f'- {ingredient}')
