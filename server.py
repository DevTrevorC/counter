from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'i used to be an adventurer like you, until i took an arrow to the knee'

@app.route('/')
def counter():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template("index.html", session = session)

if __name__ == "__main__":
    app.run(debug = True)