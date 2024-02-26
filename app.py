from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Summary

import time
import random as rand

count_metric = Counter('counter', 'total request counter')
home_counter = Counter('home_counter', 'total request for default api')
heavy_counter = Counter('heavy_counter', 'total requests for heavy api')
error_counter = Counter('error_counter', 'total requests for error api')

duration = Summary('duration_compute_seconds', 'Time spent in the heavy() function')

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application Info', version='1.0.1')

@app.route("/")
def main():
    count_metric.inc()
    home_counter.inc()

    return {
        "data": "Connected Successfully!"
    }, 200

@app.route("/heavy")
@duration.time()
def heavy():
    count_metric.inc()
    heavy_counter.inc()
    
    delay = rand.randint(2, 10)
    time.sleep(delay)

    return {
        "status": "Compiled Successfully!",
        "delay": str(delay) + " secs"
    }, 200

@app.route("/error")
def error():
    count_metric.inc()
    error_counter.inc()
    
    return {
        "status": "Error T_T"
    }, 500

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)