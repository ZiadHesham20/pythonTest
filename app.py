import os
import sqlite3
import requests
from flask import g
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from datetime import datetime


app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {'user1': 'password1', 'user2': 'password2'}


@app.route('/')
def login_redirect():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username  # Store the username in the session
            return redirect(url_for('home'))  # Redirect to the home page
        else:
            message = 'Invalid username or password'
    return render_template('login.html', message=message)


@app.route('/home', methods=['GET', 'POST'])
def home():
    user_name = session.get('username', None)
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username  # Store the username in the session
            return redirect(url_for('search'))  # Redirect to the search page after login
        else:
            message = 'Invalid username or password'
    return render_template('home.html', user_name=user_name, message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/today_matches', methods=['GET'])
def today_matches():

    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('TDM.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")



@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/scorers')
def scorers():
    return render_template('scorers.html')

@app.route('/cl', methods=['GET'])
def cl():

    url = "https://api.football-data.org/v4/competitions/CL/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('cl.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/premier_league', methods=['GET'])
def premier_league():

    url = "https://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('pl.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")

@app.route('/la_liga', methods=['GET'])
def la_liga():

    url = "https://api.football-data.org/v4/competitions/PD/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('liga.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")

@app.route('/bundesliga')
def bundesliga():
    # Logic for handling Bundesliga button click
    url = "https://api.football-data.org/v4/competitions/BL1/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('bl.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")

@app.route('/serie_a')
def serie_a():
    url = "https://api.football-data.org/v4/competitions/SA/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('sa.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")

@app.route('/ligue_1')
def ligue_1():
    url = "https://api.football-data.org/v4/competitions/FL1/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('l1.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/Eredivisie', methods=['GET'])
def Eredivisie():

    url = "https://api.football-data.org/v4/competitions/DED/standings"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('Eredivisie.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/pls', methods=['GET'])
def pls():

    url = "https://api.football-data.org/v4/competitions/PL/scorers"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('pls.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/ligas', methods=['GET'])
def ligas():

    url = "https://api.football-data.org/v4/competitions/PD/scorers"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('ligas.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/bls', methods=['GET'])
def bls():

    url = "https://api.football-data.org/v4/competitions/BL1/scorers"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('bls.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/sas', methods=['GET'])
def sas():

    url = "https://api.football-data.org/v4/competitions/SA/scorers"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('sas.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/l1s', methods=['GET'])
def l1s():

    url = "https://api.football-data.org/v4/competitions/FL1/scorers"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('l1s.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/Eredivisies', methods=['GET'])
def Eredivisies():

    url = "https://api.football-data.org/v4/competitions/DED/scorers"
    headers = {"X-Auth-Token": "0a547523f3414dd5ae1280609f83f1bd"}
    response = requests.get(url, headers=headers)

    # Print the response text for debugging
    print(response.text)

    # Check if the response status code is 200
    if response.status_code == 200:
        try:
            # Use the data retrieved from the API
            data = response.json()
            return render_template('Eredivisies.html', data=data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return apology("Failed to decode JSON response from the API")
    else:
        print(f"Request failed with status code: {response.status_code}")
        return apology("Failed to retrieve data from the API")


@app.route('/logout', methods=['GET'])
def logout():
    # Clear the user session
    session.clear()
    # Redirect the user to the login page
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
