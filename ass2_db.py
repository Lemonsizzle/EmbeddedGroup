import mysql.connector
from datetime import datetime
import time

class db:
    def __init__(self, host="127.0.0.1", user, password, database):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="zane",
            password="password",
            database="embedded_assignment_2"
        )

        self.cursor = conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            timestamp TIMESTAMP,
            temperature REAL,
            humidity REAL,
            roll REAL,
            pitch REAL,
            yaw REAL
        )
        ''')


    def __del__(self):


    def log(self, data):
        # Insert data into the table
        insert_query = '''
        INSERT INTO data (timestamp, temperature, humidity, roll, pitch, yaw)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        self.cursor.execute(insert_query, data)
        self.conn.commit()

while True:
    timestamp = datetime.now()
    
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()

    orientation = sense.get_orientation()

    roll = orientation['roll']
    pitch = orientation['pitch']
    yaw = orientation['yaw']

    # Wait 100ms before inserting the next data
    time.sleep(0.1)

# Close the connection when done
conn.close()

