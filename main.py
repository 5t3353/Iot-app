from flask import Flask , render_template ,request
from pymongo import MongoClient,DESCENDING

app = Flask(__name__)

dir = "mongodb+srv://aqiots_syst:ProtectedPa55W@iot-cluster.zo4ge.mongodb.net/test"

client = MongoClient(dir)

app.database = client.get_database("Iot")

stored_data = [s for s in app.database.sensors.find().sort("_id", DESCENDING).limit(10)]

features = list(stored_data[0].keys())[1:]


@app.route('/')
def principal():

    return render_template("principal.html")


@app.route('/database')
def database():


    return render_template("data.html" , columns = features,data = stored_data)


@app.route('/dashboard')
def dashboard():

    return render_template("dashboard.html")


if __name__ == '__main__':

    app.run()
