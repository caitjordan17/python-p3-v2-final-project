# lib/models/department.py
from models.__init__ import CURSOR, CONN

class City:
    all = {}

    def __init__(self, name, state, id=None):
        self.id = id
        self.name = name
        self.state = state

    @classmethod
    def get_id(cls, name_value):
        for city in City.all.values():
            if str(name_value) == city.name:
                return city.id
    
    def return_state(self):
        return f'{self.state}'
    
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
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if isinstance(state, str) and len(state):
            self._state = state
        else:
            raise ValueError(
                "State must be a non-empty string"
            )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of City instances """
        sql = """
            CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            state TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists City instances """
        sql = """
            DROP TABLE IF EXISTS cities;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and state values of the current City instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO cities (name, state)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.state))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, state):
        """ Initialize a new City instance and save the object to the database """
        city = cls(name, state)
        city.save()
        return city
    
    def delete(self):
        """Delete the table row corresponding to the current City instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM cities
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        """Return a City object having the attribute values from the table row."""
        city = cls.all.get(row[0])
        if city:
            city.name = row[1]
            city.state = row[2]
        else:
            city = cls(row[1], row[2])
            city.id = row[0]
            cls.all[city.id] = city
        return city
    
    @classmethod
    def get_all(cls):
        """Return a list containing a City object per row in the table"""
        sql = """
            SELECT *
            FROM cities
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a City object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM cities
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a City object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM cities
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def restaurants(cls, id):
        """Return list of restaurants in current city"""
        from models.restaurant import Restaurant
        sql = """
            SELECT * FROM restaurants
            WHERE city_id = ?
        """
        CURSOR.execute(sql, (id,),)
        rows = CURSOR.fetchall()
        return [
            Restaurant.instance_from_db(row) for row in rows
        ]
