import sqlite3

CONN = sqlite3.connect('restaurant_finder.db')
CURSOR = CONN.cursor()
