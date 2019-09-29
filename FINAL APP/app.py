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
laptops = Base.classes.both_laptops
locations = Base.classes.both_locations


session = Session(db.engine)


@app.route("/homepage/index.html")
def index():
    # returns the homepage index.html
    return render_template("index.html")


@app.route("/homepage/data.html")
def data():
    stmt_laptops1 = db.session.query(laptops).statement
    df_laptops1 = pd.read_sql_query(stmt_laptops1, db.session.bind)
    data_laptops1 = df_laptops1.to_json()

#     # return jsonify(list(df_map.columns)[2:])
#     # placeholder text till the map is finished
    return render_template("data.html", data=data_laptops1)
#     # return render_template("map.html")
#     #     # placeholder text till the table is finished


@app.route("/homepage/chart.html")
def chart():
    stmt_laptops2 = db.session.query(laptops).statement
    df_laptops2 = pd.read_sql_query(stmt_laptops2, db.session.bind)
    data_laptops2 = df_laptops2.to_json()

#     # return jsonify(list(df_map.columns)[2:])
#     # placeholder text till the map is finished
    return render_template("chart.html", data=data_laptops2)
#     # placeholder text till the table is finished


@app.route("/homepage/map.html")
def map():
    stmt_map = db.session.query(locations).statement
    df_map = pd.read_sql_query(stmt_map, db.session.bind)
    data_map = df_map.to_json()
    # return data_map
    # return jsonify(list(df_map.columns)[2:])
    # placeholder text till the map is finished
    return render_template("map.html", data=data_map)
    # return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
