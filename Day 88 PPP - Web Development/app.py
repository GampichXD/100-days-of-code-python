# Professional Portfolio Project - Web Developement
# Cafe and Wifi Website
# Author : Abraham
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_PATH = "cafes.db"

# Home page: list all cafes
@app.route("/")
def home():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cafes = cursor.execute("SELECT * FROM cafes").fetchall()
    conn.close()
    return render_template("index.html", cafes=cafes)

# Add new cafe
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = (
            request.form["name"],
            request.form["location"],
            request.form["map_url"],
            request.form["img_url"],
            request.form["seats"],
            request.form["coffee_rating"],
            request.form["wifi_rating"],
            request.form["power_rating"]
        )
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cafes (name, location, map_url, img_url, seats, coffee_rating, wifi_rating, power_rating)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    return render_template("add.html")

# Delete cafe
@app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cafes WHERE id = ?", (cafe_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5050)
