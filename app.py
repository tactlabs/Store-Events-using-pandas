from flask import Flask, render_template, request
import csv 
from datetime import datetime
import pandas as pd
app = Flask(__name__)
PORT=5000

@app.route('/', methods=['GET', 'POST'])
def root():
	return render_template('index.html')

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    global name
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        date=str(date)


    if request.method == 'POST':
        name2 = request.form['name2']
        date2 = request.form['date2']
        date2=str(date2)

    if request.method == 'POST':
        name3 = request.form['name3']
        date3 = request.form['date3']
        date3=str(date3)
 
    data={'Event_Name':[name,name2,name3],'Date':[date,date2,date3]}
    df = pd.DataFrame(data, columns = ['Event_Name', 'Date'])
                             
    print(df)
    df.to_csv('data.csv', index=False)

    a=pd.read_csv("data.csv")
    a.to_html("output.html")
    return render_template('output.html')
        

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=PORT)
    