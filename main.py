from flask import Flask , render_template ,request
import pymysql


app = Flask(__name__)

msg = ""

try:
      conn = pymysql.connect(host = '192.168.1.82',
                             user = 'iot-cluster',
                             password = 'heroku5y5t3m',
                             bind_address = '201.188.122.150')
      
      msg = "error conencting"
      
except:
      msg = "error conencting"
      
      
data = {'id':[1,2,3,4,5],
      'temp':[14,15,14,24,10],
      'hum':[0.5,0.9,1.1,0.09,1],
      'co2':[0.4,0.6,0.3,0.1,0.8],
      'datm':["oct 19 13:55",
             "oct 19 17:40",
             "oct 19 22:54","oct 20 1:34",
             "oct 20 5:56"]}

@app.route('/')
def principal():

    return render_template("principal.html",msg = msg)

@app.route('/database')
def database():

    return render_template("data.html",db = data)

@app.route('/dashboard')
def dashboard():

    test_data = [4,6,2]

    return render_template("dashboard.html",data = data)



if __name__ == '__main__':
  
  app.run()

