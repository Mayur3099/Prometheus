from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

import time
import random as rand

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application Info', version='1.0.1')

@app.route("/")
def main():
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

@app.route("/error")
def error():
    return {
        "status": "Error T_T"
    }, 500

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)