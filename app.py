import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import 'load.py' which calls the 'transform.py' which intern calls the 'extract.py'
import load.py

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///immunization_db.sqlite")
# Create Engine and Pass in MySQL Connection
#conn_str = "root:root@127.0.0.1/immunization_db"
#engine = create_engine(f'mysql://{conn_str}')

# Connect
#conn = engine.connect()

# Query All Records to confirm the load
#data = pd.read_sql("SELECT * FROM wa_immunizations", conn)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Wa_immunizations = Base.classes.wa_immunizations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/immunizations<br/>"
    )


@app.route("/api/v1.0/immunizations")
def names():
    """Return all immunizations"""
    # Query all immunizations
    results = session.query(Wa_immunizations).all()

    # Create a dictionary from the row data and append to a list of all_immunizations
    all_immunizations = []
    for immunization in results:
        immunizations_dict = {}
        immunizations_dict["id"] = immunization.id
        immunizations_dict["county"] = immunization.county
        immunizations_dict["school_year"] = immunization.school_year
        immunizations_dict["number_reported"] = immunization.number_reported
        immunizations_dict["number_completed"] = immunization.number_completed
        immunizations_dict["pop_2016"] = immunization.pop_2016
        all_immunizations.append(immunizations_dict)

    return jsonify(all_immunizations)


if __name__ == '__main__':
    app.run(debug=True)
