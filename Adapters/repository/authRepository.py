import mysql.connector
from Core.user import User
import yaml 
from werkzeug.security import generate_password_hash, check_password_hash

class AuthRepository:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    @staticmethod
    def getInstance():
        configFile = 'config.yaml'
        with open(configFile) as f:
            config = yaml.safe_load(f)
        host = config['host']
        username = config['username']
        password = config['password']
        database = config['database']
        return AuthRepository(host,username,password,database)
    def __connectToDB__(self):
        connection = mysql.connector.connect(
        host=self.host,
        user=self.username,
        password=self.password,
        database=self.database
        )
        return connection
    def create(self, user: User) -> User:
        connection = self.__connectToDB__()
        cursor = connection.cursor()
        hashed_password = generate_password_hash(user.password)
        insert_query = "INSERT INTO users (userID, username, password) VALUES (%s, %s, %s)"
        values = (user.userID, user.username, hashed_password)
        cursor.execute(insert_query, values)
        userID = cursor.lastrowid
        user.userID = userID
        connection.commit()
        cursor.close()
        connection.close()
        return user

    def get_by_id(self, userID: int) -> User:
        connection = self.__connectToDB__()

        cursor = connection.cursor()
        select_query = "SELECT username, password FROM users WHERE userID = %s"
        cursor.execute(select_query, (userID,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            username, password = result
            return User(userID, username, password)
        return None
    

    def update_username(self, user: User) -> User:
        connection = self.__connectToDB__()
        print(user)
        cursor = connection.cursor()
        update_query = "UPDATE users SET username = %s WHERE userID = %s"
        values = (user.username, user.userID)
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return user
    
    def update_password(self, user: User) -> User:
        connection = self.__connectToDB__()
        print(user)
        cursor = connection.cursor()
        hashed_password = generate_password_hash(user.password)
        update_query = "UPDATE users SET password = %s WHERE userID = %s"
        values = (hashed_password, user.userID)
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return user
    
    def delete(self, userID: int) -> None:
        print(type(userID))
        connection = self.__connectToDB__()
        cursor = connection.cursor()
        delete_query = "DELETE FROM users WHERE userID = %s"
        cursor.execute(delete_query, (userID,))
        connection.commit()
        cursor.close()
        connection.close()
