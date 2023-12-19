# lib/models/department.py
from models.__init__ import CURSOR, CONN

class City:
    all = {}

    def __init__(self, name, state, id=None):
        self.id = id
        self.name = name
        self.state = state

    def __repr__(self):
        return f'<City {self.id}: {self.name}, located in {self.state}>'
    
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

    # state @property to validate state is a valid state in array

    # @classmethods
    # create_table to persist attributes of City
    # drop_table to drop the table that has City instances
    # create_new to initialize a new City & save object to database
    # get_all to return list of all Cities
    # find_by_id to return a City that matches the id 
    # find_by_name to return a City that matches the name
    
    # instance methods
    # save to insert new row into the current City instance & save
        # obj in local dictionary
    # delete to delete the table row corresponding to the current
        # City instance
    # restaurants to return a list of restaurants associated with
        # the city; from models.restaurant import Restaurant
    