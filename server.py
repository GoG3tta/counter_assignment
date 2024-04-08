from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'this is a secret test' # set a secret key for security purposes

@app.route("/")
def test_session_counter():
    if'count' in session:
        session["count"] += 1
    else:
        session["count"] = 1
    return render_template("counter.html")

@app.route("/add_two", methods=["POST"])
def add_two():
    if "count" in session:
        session["count"] += 1
    else:
        session['count'] = 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True)  