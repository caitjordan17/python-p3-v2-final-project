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
        return f'<City {self.id}: {self.name}, located in {self.city}>'
    
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
    