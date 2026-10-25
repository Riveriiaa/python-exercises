import os
import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):

    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ.get("DB_NAME", "flight_game"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ["DB_PASSWORD"],
        autocommit=True
    )

    cursor = connection.cursor()

    sql = """
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
    """

    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def run_airport_distance():

    first = input("Enter the ICAO code of the first airport: ").upper()
    second = input("Enter the ICAO code of the second airport: ").upper()

    coord1 = get_airport_coordinates(first)
    coord2 = get_airport_coordinates(second)

    if coord1 is None or coord2 is None:
        print("One or both ICAO codes were not found.")
        return

    location1 = (coord1[0], coord1[1])
    location2 = (coord2[0], coord2[1])

    distance_km = geodesic(location1, location2).kilometers

    print(f"Distance between {first} and {second}: {distance_km:.2f} kilometers")


run_airport_distance()