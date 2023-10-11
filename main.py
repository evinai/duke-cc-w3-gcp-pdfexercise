from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""

    return "Hello I like to make AI Apps-updated"


@app.route("/name/<value>")
def name(value):
    val = {"value": value}
    return jsonify(val)


@app.route("/pandas")
def pandas_sugar():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv"
    )
    return jsonify(df.to_dict())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
