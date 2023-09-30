from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def save (cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojo_users').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas_from_db =  connectToMySQL('dojo_users').query_db(query)
        ninjas =[]
        for b in ninjas_from_db:
            ninjas.append(cls(b))
        return ninjas
    
    @classmethod
    def update(cls, data):
        query = """UPDATE ninjas
            SET first_name=%(first_name)s, last_name=%(last_name)s,  age=%(age)s, updated_at = NOW()
            WHERE id = %(id)s;"""
        return connectToMySQL('dojo_users').query_db(query, data)
    
    @classmethod
    def remove(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojo_users').query_db(query, data)
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL('dojo_users').query_db(query, data)
        return cls(result[0])
    