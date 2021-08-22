# Import all the stuff

import numpy as np
import pandas as pd
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Stations = Base.classes.station

# Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)


    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > '2016-08-23').\
            order_by(Measurement.date).all()
    # Convert the query results to a dictionary using date as the key and prcp as the value.
    precipitations = []

    for result in results:
            row = {}
            row["date"] = result[0]
            row["prcp"] = float(result[1])
            precipitation.append(row)

    return jsonify(precipitations)

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))


