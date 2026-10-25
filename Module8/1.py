import os
import mysql.connector


def main():
    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ.get("DB_NAME", "flight_game"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ["DB_PASSWORD"],
        autocommit=True
    )

    cursor = connection.cursor()

    icao = input("Enter the ICAO code of an airport: ").upper()

    sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
    """

    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        name = result[0]
        city = result[1]

        print(f"Airport name: {name}")
        print(f"Location: {city}")
    else:
        print(f"No airport found with ICAO code {icao}")


    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()