import appsignal
from appsignal import set_category
from opentelemetry import trace

# open telemetry instrumentation
appsignal.start()
tracer = trace.get_tracer(__name__)

from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

weather_data = [
    {"city": "New York", "temperature": 77, "condition": "Cloudy"},
    {"city": "Los Angeles", "temperature": 70, "condition": "Sunny"},
    {"city": "Chicago", "temperature": 73, "condition": "Sunny"},
    {"city": "Houston", "temperature": 81, "condition": "Cloudy"},
    {"city": "Phoenix", "temperature": 92, "condition": "Sunny"},
]


@app.route('/weather', methods=['GET'])
def get_weather():
    with tracer.start_as_current_span("random_weather"):
        set_category("get_weather")
        return jsonify(random.choice(weather_data))


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    host = os.getenv('ADDRESS', 'localhost')

    app.run(debug=True, host=host, port=port)
