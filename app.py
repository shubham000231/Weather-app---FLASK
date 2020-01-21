from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('layout.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      city = request.form.get('text')

      url="https://openweathermap.org/data/2.5/weather?q="+city+"&appid=b6907d289e10d714a6e88b30761fae22"
      try:
         r=requests.get(url)
      except:
         print("Some error occured")
   return render_template("forms.html",result = json.loads(r.text))

if __name__ == '__main__':
   app.run(debug = True)
