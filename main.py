from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
application = app
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
