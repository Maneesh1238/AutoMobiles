import mysql.connector
#connect mysql
conn = mysql.connector.connect(
host = "localhost",
user = "root",
password = "Maneesh@B161238",
database = "motorcycles"
)
cursor =conn.cursor()
def add_bikes(BIKE_NAME,BIKE_CC,BIKE_MILAGE):
    sql = "INSERT INTO bikes (BIKE_NAME,BIKE_CC,BIKE_MILAGE) VALUES (%s,%s,%s)"
    VALUES = (BIKE_NAME,BIKE_CC,BIKE_MILAGE)
    cursor.execute(sql,VALUES)
    conn.commit()
    print("bike added")

def view_bikes():
    sql = "SELECT * FROM bikes"
    cursor.execute(sql)
    for bike in cursor:
        print(bike)

def update_bike(BIKE_NAME,BIKE_CC):
    sql = "update bikes set BIKE_CC=%s WHERE BIKE_NAME=%s"
    VALUES = (BIKE_CC,BIKE_NAME)
    cursor.execute(sql,VALUES)
    conn.commit()
    print("bike updated")

def delete_bike(BIKE_NAME):
    sql = "DELETE FROM bikes WHERE BIKE_NAME=%s"
    VALUES = (BIKE_NAME,)
    cursor.execute(sql,VALUES)
    conn.commit()
    print("bike deleted")

#def bikes():
    #BIKE_NAME = input("Enter bike name: ")
    #BIKE_CC = input("Enter bike CC: ")
    #BIKE_MILAGE = input("Enter bike MILAGE: ")
    #add_bikes(BIKE_NAME,BIKE_CC,BIKE_MILAGE)
#view_bikes()

#update_bike("DUCATI","986")
delete_bike("DUCATI")



#bikes()
cursor.close()
conn.close()

