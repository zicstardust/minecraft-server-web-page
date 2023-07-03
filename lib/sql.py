import mysql.connector
import time


class Connection:
    def __init__(self):
        self.connected = False
        self.connection = self.connect()

    def connect(self):
        _tries = 0
        while not self.connected and not _tries > 4:
            try:
                connetion = mysql.connector.connect(
                    host="localhost",
                    database="minecraft_server_db",
                    user="web_page",
                    password="web_page",
                )
                if connetion.is_connected():
                    self.connected = True
                    print("Connected to MySQL database")
            except mysql.connector.Error as e:
                print(e)
                _tries += 1
                time.sleep(1)
        if not self.connected:
            print("Failed to connect to MySQL database")
            exit(1)

        return connetion

    def __call__(self, query):
        if not self.connected:
            self.connection = self.connect()

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
        return cursor


sql = Connection()
