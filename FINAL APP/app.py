import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import sqlalchemy

app = Flask(__name__)


# Database Setup

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    'DATABASE_URL', '')
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
bestbuy_table = Base.classes.bestbuy_laptops
frys_table = Base.classes.frys_laptops


@app.route("/")
def index():
    # returns the homepage index.html
    return render_template("index.html")


@app.route("/data")
def index():
    # placeholder text till the table is finished
    return print("This is where the filter and complete data goes!")


@app.route("/chart")
def index():
    # placeholder text till the table is finished
    return print("This is where the chart with multiple axes goes!")


@app.route("/map")
def index():
    # placeholder text till the map is finished
    return print("This is where the map goes!")


if __name__ == "__main__":
    app.run(debug=True)
