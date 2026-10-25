import os
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def hae_lentokentta(icao):
    yhteys = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        database=os.environ.get("DB_NAME", "flight_game"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ["DB_PASSWORD"]
    )

    kursori = yhteys.cursor(dictionary=True)

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    kursori.close()
    yhteys.close()

    return tulos


@app.route("/kenttä/<icao>", methods=["GET"])
@app.route("/kentta/<icao>", methods=["GET"])
def kentta(icao):
    icao = icao.upper()
    lentokentta = hae_lentokentta(icao)

    if lentokentta:
        return jsonify({
            "ICAO": lentokentta["ident"],
            "Name": lentokentta["name"],
            "Municipality": lentokentta["municipality"]
        })

    return jsonify({
        "error": "Airport not found",
        "ICAO": icao
    }), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)