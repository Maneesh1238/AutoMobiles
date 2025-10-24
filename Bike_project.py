import mysql.connector
# ----- connecting mysql to python ----- #
try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Maneesh@B161238",
        database = "bikes_db"
    )
    cursor = conn.cursor()
    print("connected to mysql database successfully")

except mysql.connector.Error as err:
    print(f"Error:{err}")
    exit(1)

# ----- CRUD FUNCTIONS ----- #
def add_bike(name,cc,mileage):
    try:
        sql = "INSERT INTO bikes (BIKE_NAME,BIKE_CC,BIKE_Mileage) VALUES (%s,%s,%s)"
        cursor.execute(sql,(name,cc,mileage))
        conn.commit()
        print("Bike added successfully")
    except mysql.connector.Error as err:
        print(f"Error:{err}")

def view_bikes():
    try:
        cursor.execute("SELECT * FORM bikes")
        rows = cursor.fetchall()
        if rows:
            print("\n ----- Bikes list -----")
            print("NAME | CC | Mileage")
            for row in rows:
                print((f"({row[0]} | {row[1]} | {row[2]})"))
        else:
            print("No bikes found in the database")
    except mysql.connector.Error as err:
        print(f"Error:{err}")

def update_bike(name):
    try:
        # check if the bike exists
        cursor.execute("SELECT * FROM bikes WHERE BIKE_NAME = %s", (name,))
        bike = cursor.fetchone()
        if not bike:
            print("No bike found in the database with that name")
            return
        print(f"Current_details : Name = {bike[0]}, CC = {bike[1]}, Mileage = {bike[2]} ")

        # get new values
        new_name = input("Enter new bike name: ").strip()
        new_name = new_name if new_name else bike[0]

        while True:
            new_cc = input("Enter new CC: ").strip()
            if not new_cc:
                new_cc = bike[1]
                break
            if new_cc.isdigit():
                new_cc = int(new_cc)
                break
            print("cc should be an integer")
        while True:
            new_mileage = input("Enter new Mileage : ").strip()
            if not new_mileage:
                new_mileage = bike[2]
                break
            if new_mileage.replace('.', '', 1).isdigit():
                new_mileage = float(new_mileage)
                break
            print("⚠ Mileage must be a number.")
            # Update bike
            cursor.execute(
                "UPDATE bikes SET BIKE_NAME=%s, BIKE_CC=%s, BIKE_MILAGE=%s WHERE BIKE_NAME=%s",
                (new_name, new_cc, new_mileage, name)
            )
            conn.commit()
            print(" Bike updated successfully!")

    except mysql.connector.Error as err:
    print(f"Error:{err}")

def delete_bike(name):
    try:
        cursor.execute("DELETE FROM bikes WHERE BIKE_NAME=%s", (name,))
        conn.commit()
        if cursor.rowcount == 0:
            print("⚠ No bike found with that name.")
        else:
            print(" Bike deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")



# --- Input Helper ---
def get_bike_input():
    name = input("Enter bike name: ").strip()
    while True:
        cc = input("Enter bike CC: ").strip()
        if cc.isdigit():
            cc = int(cc)
            break
        print("⚠ CC must be a number.")
    while True:
        mileage = input("Enter bike mileage: ").strip()
        if mileage.replace('.', '', 1).isdigit():
            mileage = float(mileage)
            break
        print(" Mileage must be a number.")
    return name, cc, mileage

# --- Main Menu ---
def main_menu():
    while True:
        print("\n--- Bike Management Menu ---")
        print("1. View Bikes")
        print("2. Add Bike")
        print("3. Update Bike (all details)")
        print("4. Delete Bike")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_bikes()
        elif choice == "2":
            name, cc, mileage = get_bike_input()
            add_bike(name, cc, mileage)
        elif choice == "3":
            name = input("Enter bike name to update: ").strip()
            update_bike(name)
        elif choice == "4":
            name = input("Enter bike name to delete: ").strip()
            delete_bike(name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print(" Invalid option. Try again.")

# --- Run Program ---
try:
    main_menu()
finally:
    cursor.close()
    conn.close()
    print("Connection closed.")

