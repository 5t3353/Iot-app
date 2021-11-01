from flask import Flask , render_template ,request
import pymysql


app = Flask(__name__)


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
  
  app.run()

