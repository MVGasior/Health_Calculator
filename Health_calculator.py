# This program counting calories and making a diet's menu
# Author : Mateusz Gąsior
# 1 # Counting calories based on inputs from users, including fat percentage
# 2 # Taking from excel file all information about nutrition
# 3 # Need a file with recipes, based on neutrons information and ingredients is counting all recipe neutrons

import sqlite3

conn = sqlite3.connect('health.db')
cur = conn.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS health(
                    product TEXT UNIQUE,
                    weight REAL DEFAULT 100,
                    protein REAL,
                    carbs REAL,
                    fat REAL
                    );
'''
cur.execute(create_table)
conn.commit()
while True:
    product = input('Insert additional product:\n')
    protein = float(input('How much protein:\n '))
    carbs = float(input("How much carbs:\n"))
    fat = float(input("How much fat:\n"))
    insert_product = "INSERT INTO health (product, protein, carbs, fat) VALUES (?, ?, ?, ?)"
    cur.execute(insert_product, (product, protein, carbs, fat))
    conn.commit()
    decision = input("Do you want to continue (Yes/No): ")
    if decision == 'Yes':
        continue
    elif decision == 'No':
        break

conn.close()
#print(cur.fetchall())
#print(type(cur.fetchall()))
