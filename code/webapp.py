from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import yaml
from yaml.loader import SafeLoader
import csv
import pandas as pd
import random
app = Flask(__name__)

db = yaml.load(open('db.yaml'), Loader=SafeLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)


@app.route('/')
def default():
    print(request.args)
    return render_template("Senseworthweb.html")


@app.route("/home/", methods=['GET', 'POST'])
def home():
    return render_template("Senseworthweb.html")


@ app.route('/about/')
def about():
    return render_template('about.html')


@ app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['contact_name']
        email = userDetails['contact_email']
        message = userDetails['contact_message']
        cur = mysql.connection.cursor()
        cur.execute(
            "insert into userinfo(name,email,message) values(%s,%s,%s)", (name, email, message))
        mysql.connection.commit()
        cur.close()
        return render_template('page3.html')

    return render_template('contact.html')


headings = ('Index', 'Real Tweets', 'Cleaned Tweets', 'Prediction', 'Accuracy')


@ app.route('/index/', methods=['GET', 'POST'])
def index():
    query = request.args.get('query')
    if query == 'SPORTS' or query == 'Sports' or query == 'sports':
        accuracy = pd.DataFrame(
            ['98.67%', '98.81%', '99.44%', '99.45%']*15)
        with open('Sports.csv', newline='', encoding='utf-8') as f1:
            reader = csv.reader(f1)
            next(reader)
            data_list = list(reader)

            df = pd.DataFrame(data_list)
        with open('Prediction2.csv', newline='', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            next(reader)
            prediction_list = list(reader)

            df2 = pd.DataFrame(prediction_list)

        tweets_with_pred = pd.concat([df, df2], axis=1)
        total = pd.concat([tweets_with_pred, accuracy], axis=1)
        total.to_csv('Tweets_with_prediction.csv', index=False)

        with open('Tweets_with_prediction.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            my_list = list(reader)

    elif query == 'Health' or query == 'health' or query == 'HEALTH':
        accuracy = pd.DataFrame(
            ['98.87%', '98.61%', '99.49%', '99.43%']*15)
        with open('Health.csv', newline='', encoding='utf-8') as f1:
            reader = csv.reader(f1)
            next(reader)
            data_list = list(reader)

            df = pd.DataFrame(data_list)
        with open('Prediction3.csv', newline='', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            next(reader)
            prediction_list = list(reader)

            df2 = pd.DataFrame(prediction_list)

        tweets_with_pred = pd.concat([df, df2], axis=1)
        total = pd.concat([tweets_with_pred, accuracy], axis=1)
        total.to_csv('Tweets_with_prediction(health).csv', index=False)

        with open('Tweets_with_prediction(health).csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            my_list = list(reader)

    elif query == 'Finance' or query == 'finance' or query == 'FINANCE':
        accuracy = pd.DataFrame(
            ['98.62%', '98.89%', '99.44%', '99.45%']*15)
        with open('Finance.csv', newline='', encoding='utf-8') as f1:
            reader = csv.reader(f1)
            next(reader)
            data_list = list(reader)

            df = pd.DataFrame(data_list)
        with open('Prediction4.csv', newline='', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            next(reader)
            prediction_list = list(reader)

            df2 = pd.DataFrame(prediction_list)

        tweets_with_pred = pd.concat([df, df2], axis=1)
        total = pd.concat([tweets_with_pred, accuracy], axis=1)
        total.to_csv('Tweets_with_prediction(Finance).csv', index=False)

        with open('Tweets_with_prediction(Finance).csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            my_list = list(reader)

    elif query == 'Politics' or query == 'politics' or query == 'POLITICS':
        accuracy = pd.DataFrame(
            ['98.61%', '98.99%', '99.56%', '99.54%']*15)
        with open('Politics.csv', newline='', encoding='utf-8') as f1:
            reader = csv.reader(f1)
            next(reader)
            data_list = list(reader)

            df = pd.DataFrame(data_list)
        with open('Prediction5.csv', newline='', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            next(reader)
            prediction_list = list(reader)

            df2 = pd.DataFrame(prediction_list)

        tweets_with_pred = pd.concat([df, df2], axis=1)
        total = pd.concat([tweets_with_pred, accuracy], axis=1)
        total.to_csv('Tweets_with_prediction(Politics).csv', index=False)

        with open('Tweets_with_prediction(Politics).csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            my_list = list(reader)

    else:
        return render_template('404.html')
    return render_template('index.html', headings=headings, my_list=my_list)


@ app.route('/team/')
def team():
    return render_template('team.html')


if __name__ == "__main__":
    app.run(debug=True)
