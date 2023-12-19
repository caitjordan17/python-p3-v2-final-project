from models.__init__ import CONN, CURSOR
from models.city import City
from models.restaurant import Restaurant

def seed_database():
    City.drop_table()
    Restaurant.drop_table()
    City.create_table()
    Restaurant.create_table()

    san_francisco = City.create("San Francisco", "California")
    chicago = City.create("Chicago", "Illinois")
    oahu = City.create("Oahu", "Hawaii")
    seattle = City.create("Seattle", "Washington")
    Restaurant.create("Mister Jiu's", "Chinese", san_francisco.id)
    Restaurant.create("Zuni Cafe", "American", san_francisco.id)
    Restaurant.create("La Taqueria", "Mexican", san_francisco.id)
    Restaurant.create("Smyth", "American", chicago.id)
    Restaurant.create("Wazwan", "South Asian", chicago.id)
    Restaurant.create("HaiSous", "Vietnamese", chicago.id)
    Restaurant.create("Fete", "American", oahu.id)
    Restaurant.create("Pig and the Lady", "Vietnamese", oahu.id)
    Restaurant.create("Senia", "American", oahu.id)
    Restaurant.create("Copine", "American", seattle.id)
    Restaurant.create("Wild Ginger", "South East Asian", seattle.id)
    Restaurant.create("Rupee Bar", "Sri Lankan", seattle.id)


seed_database()
print("Cities & restaurants added!")