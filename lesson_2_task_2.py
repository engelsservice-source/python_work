def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year_to_check = 2021
result = is_year_leap(year_to_check)
print(f"год {year_to_check}: {result}")