# lib/models/department.py
from models.__init__ import CURSOR, CONN
from models.city import City

class Restaurant:
    all = {}

    def __init__(self, name, cuisine, city_id, id=None):
        self.id = id
        self.name = name
        self.city_id = city_id
        self.cuisine = cuisine

    def __repr__(self):
        return f'<City {self.id}: {self.name}, located in {self.city_id}>'
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def cuisine(self):
        return self._cuisine
    @cuisine.setter
    def cuisine(self, cuisine):
        if isinstance(cuisine, str) and len (cuisine):
            self._cuisine = cuisine
        else:
            raise ValueError(
                "Cuisine must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Restaurant instances """
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cuisine TEXT,
            city_id INTEGER,
            FOREIGN KEY (city_id) REFERENCES cities(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Restaurant instances"""
        sql = """
            DROP TABLE IF EXISTS restaurants;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, cuisine, and city id values 
        of the current Restaurant object. Update object id attribute using the 
        PK value of new row. Save the obj in local dictionary using table
        row's PK as dictionary key"""
        sql = """
            INSERT INTO restaurants (name, cuisine, city_id)
            VALUES (?, ?, ?)
            """
        CURSOR.execute(sql, (self.name, self.cuisine, self.city_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        """Delete the table row corresponding to the current Restaurant instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM restaurants
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]     


    @classmethod
    def create(cls, name, cuisine, city_id):
        """ Initialize a new Restaurant instance and save the object to the database """
        restaurant = cls(name, cuisine, city_id)
        restaurant.save()
        return restaurant

    @classmethod
    def instance_from_db(cls, row):
        """Return an Restaurant object having the attribute values from the table row."""
        restaurant = cls.all.get(row[0])
        if restaurant:
            restaurant.name = row[1]
            restaurant.cuisine = row[2]
            restaurant.city_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            restaurant = cls(row[1], row[2], row[3])
            restaurant.id = row[0]
            cls.all[restaurant.id] = restaurant
        return restaurant   
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Restaurant object per table row"""
        sql = """
            SELECT *
            FROM restaurants
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return Restaurant object corresponding to the table row matching the 
        specified PK"""
        sql = """
            SELECT *
            FROM restaurants
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None    
    
    @classmethod
    def find_by_name(cls, name):
        """Return Restaurant object corresponding to first table row matching 
        specified name"""
        sql = """
            SELECT *
            FROM restaurants
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # @ properties
    # cuisine to validate cuisine is a non empty string
    # city_id to validate city_id references a city in the database

    # @classmethods
    # create_table to persist attributes of Restaurant
    # drop_table to drop the table that has Restaurant instances
    # create_new to initialize a new Restaurant & save object to database
    # get_all to return list of all Restaurants
    # find_by_id to return a Restaurant that matches the id 
    # find_by_name to return a Restaurant that matches the name
    
    # instance methods
    # save to insert new row into the current Restaurant instance & 
    #    save obj in local dictionary
    # delete to delete the table row corresponding to the current
        # Restaurant instance
    