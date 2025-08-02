import pandas as pd


dish = pd.read_csv('Dish.csv')
# for ic violations we will be checking 4 things
# Same name doesn't show up twice
# first_appeared <= last_appeared
# lowest_price <= highest_price
# menus_appeared <= times_appeared

def ic_check_name_violation(df):
    nameset = set()
    violations = 0
    for _, row in df.iterrows():
        if row['name'].lower() not in nameset:
            nameset.add(row['name'].lower())
        else:
            violations += 1
    return violations

# print(ic_check_name_violation(dish)) 28053

def ic_time_appearance_violation(df):
    violations = 0
    for _, row in df.iterrows():
        if int(row['first_appeared']) > int(row['last_appeared']):
            violations += 1
    return violations

# print(ic_time_appearance_violation(dish)) 6

def ic_price_violation(df):
    violations = 0
    for _, row in df.iterrows():
        if float(row['lowest_price']) > float(row['highest_price']):
            violations += 1
    return violations

# print(ic_price_violation(dish)) 0

def ic_menu_appearance_violation(df):
    violations = 0
    for _, row in df.iterrows():
        if int(row['menus_appeared']) > int(row['times_appeared']):
            violations += 1
    return violations

# print(ic_menu_appearance_violation(dish)) 8274