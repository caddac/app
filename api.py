import os
from flask import Flask, request

app = Flask(__name__)

env = os.environ["ENV"]
assert env


@app.route("/")
def alive():
    data = {"ENV": env}
    return data, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
