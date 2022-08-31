import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect an existing database into a new mocel
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
        #creates sessionn from python to the db
        session = Session(engine)

        results = session.query(Measurement.prcp, Measurement.date).all()

        session.close()

        all_precip_date = []
        for date, prcp in results:
            precip_date_dict = {}
            precip_date_dict[date] = prcp
            all_precip_date.append(precip_date_dict)

        return jsonify(all_precip_date)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close

    all_station = []

    for station,name,latitude,longitude,elevation in results:
        station_dict = {}
        station_dict['station'] = station
        station_dict['name'] = name
        station_dict['latitude'] = latitude
        station_dict['longitude'] = longitude
        station_dict['elevation'] = elevation
        all_station.append(station_dict)
    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    activity = session.query(Measurement.station, func.count(Measurement.station)).\
            group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc()).all()

    most_active = activity[0][0]

    recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #change the row to be a list and take the first instance in the list to get a string
    str_date=list(recent)[0]
    #change the string to be in the date time format
    latest = dt.datetime.strptime(str_date,"%Y-%m-%d")

    year_ago = latest - dt.timedelta(days=366)

    results = session.query(Measurement.tobs, Measurement.date).\
                    filter(Measurement.station == most_active).\
                    filter(Measurement.date >= year_ago).all()
    session.close()

    all_temp = []

    for tobs, date in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_temp.append(temp_dict)

    return jsonify(all_temp)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    #start date must be in the format "YYYY-MM-DD"
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                filter(Measurement.date >= start).all()
    
    session.close()

    temp_date = []
    for min, max, avg in results:
        temp_date_dict = {}
        temp_date_dict["Min_Temp"] = min
        temp_date_dict["Max_Temp"] = max
        temp_date_dict["Avg_Temp"] = avg
        temp_date.append(temp_date_dict)

    return jsonify(temp_date)


@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start,end):
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    temp_start_end_dict = {}
    temp_start_end_dict["Min_Temp"] = results[0][0]
    temp_start_end_dict["Max_Temp"] = results[0][1]
    temp_start_end_dict["Avg_Temp"] = results[0][2]

    return jsonify(temp_start_end_dict)



if __name__ == '__main__':
    app.run(debug=True)



