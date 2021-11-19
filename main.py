from numpy import mean ,random , linspace
from flask import Flask , render_template ,request
from pymongo import MongoClient,DESCENDING


app = Flask(__name__)

dir = "mongodb+srv://aqiots_syst:Password@iot-cluster.zo4ge.mongodb.net/test"

client = MongoClient(dir)

app.database = client.get_database("Iot")


@app.route('/')
def principal():

    return render_template("principal.html")

@app.route('/database')
def database():

    stored_data = [s for s in app.database.sensors.find().sort("_id", DESCENDING).limit(15)]

    return render_template("data.html" ,data = stored_data)


@app.route('/dashboard')
def dashboard():

    stored_data = [s for s in app.database.sensors.find().sort("_id", DESCENDING).limit(15)]

    time_series = []

    temp_series = []

    hum_series = []

    co2_series = []

    for doc in reversed(stored_data):

        time_series.append(doc.get("DATE-TIME")[-6:])

        temp_series.append(float(doc.get("TEMPERATURE")))

        hum_series.append(float(doc.get("HUMIDITY")))

        co2_series.append(float(doc.get("CO2")))

    avgs = [mean(temp_series),
            mean(hum_series),
            mean(co2_series)]


    return render_template("dashboard.html", time_base = time_series ,
                                             temp = temp_series,
                                             hum = hum_series,
                                             co2 = co2_series,
                                             stats = avgs)


if __name__ == '__main__':

    app.run()
