from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Dirty little secret"

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/form', methods=["POST"])
def form():
    session['name'] = request.form['name']
    session['d_location'] = request.form['d_location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/results")

@app.route('/results')
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)