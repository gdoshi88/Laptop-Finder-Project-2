import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Database Setup

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:monicapatel4020@localhost:5432/laptop_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# os.environ.get('DATABASE_URL', '')

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
laptop_data = Base.classes.bestbuy_laptops
# Store_data = Base.classes.  # name of store data table

session = Session(db.engine)


@app.route("/homepage/index.html")
def index():
    # returns the homepage index.html
    return render_template("index.html")


@app.route("/homepage/data.html")
def data():
    #     # placeholder text till the table is finished
    return render_template("data.html")


@app.route("/homepage/chart.html")
def chart():
    # placeholder text till the table is finished
    return render_template("chart.html")


@app.route("/homepage/map.html")
def map():
    # placeholder text till the map is finished
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
