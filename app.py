from flask import Flask
import time
import random as rand

app = Flask(__name__)

@app.route("/")
def default():
    return {
        "data": "Connected Successfully!"
    }, 200

@app.route("/heavy")
def heavy():
    delay = rand.randint(2, 10)
    time.sleep(delay)

    return {
        "status": "Compiled Successfully!",
        "delay": str(delay) + " secs"
    }, 200


if __name__ == "__main__":
    app.run()