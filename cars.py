impot mysql.connector
#connecting to mysql
conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "Maneesh@B161238",
    database = "CARS_DB"
)
cursor = conn.cursor()
def add_cars(CAR_NAME,CAR_BRAND,CAR_MILAGE):
    sql = "INSERT INTO CARS (CAR_NAME,CAR_BRAND,CAR_MILAGE) VALUES (%s,%s,%s)"
    VALUES = (CAR_NAME,CAR_BRAND,CAR_MILAGE)
    cursor.execute(sql,VALUES)
    conn.commit()
    print("Car added")

def cars():
    CAR_NAME = input("Enter Car Name: ")
    CAR_BRAND = input("Enter Car Brand: ")
    CAR_MILAGE = int(input("Enter Car Milage: "))
    add_cars(CAR_NAME,CAR_BRAND,CAR_MILAGE)
cars()
cursor.close()
conn.close()