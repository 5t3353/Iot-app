from flask import Flask , render_template ,request
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host = '192.168.1.82',
                       user = 'local',
                       passwd = 'userroot')

print("connection successfully!")

cursor = conn.cursor()

query = "SELECT temperature , humidity , co2 FROM iot.sensors;"

cursor.execute(query)

values = cursor.fetchall()
print(values)
conn.close()

data = {'id':[1,2,3,4,5],
      'temp':[14,15,14,24,10],
      'hum':[0.5,0.9,1.1,0.09,1],
      'co2':[0.4,0.6,0.3,0.1,0.8],
      'datm':["oct 19 13:55",
             "oct 19 17:40",
             "oct 19 22:54","oct 20 1:34",
             "oct 20 5:56"]}


columns = list(data.keys())

columns = columns[1:4]

print (columns)

@app.route('/')
def principal():

    return render_template("principal.html")


@app.route('/database')
def database():

    return render_template("data.html",db = data)


@app.route('/dashboard')
def dashboard():

    test_data = [4,6,2]

    return render_template("dashboard.html",data = data)



if __name__ == '__main__':

    app.run(debug = True, host = '192.168.1.82')

    #conn.close()