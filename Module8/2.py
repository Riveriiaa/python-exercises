import os
import mysql.connector


def get_airports_by_country(country_code):
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
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
    """

    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def run_country_program():
    print("Enter the country code (e.g., FI for Finland):")
    code = input().upper()

    airports = get_airports_by_country(code)

    if len(airports) == 0:
        print(f"No airports found for country code {code}.")
    else:
        print()
        print(f"Airports in {code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")


run_country_program()