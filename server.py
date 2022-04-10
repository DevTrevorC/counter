from operator import methodcaller
from turtle import clear
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'i used to be an adventurer like you, until i took an arrow to the knee'

@app.route('/')
def counter():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    if "visits" in session:
        session["visits"] += 1
    else:
        session["visits"] = 1
    return render_template("index.html", session = session)

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/by_2')
def by_2():
    session["counter"] += 1
    return redirect('/')

@app.route('/this_to_counter', methods = ['POST'])
def this_to_counter():
    session["counter"] += (int(request.form["more_to_counter"]) - 1)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)