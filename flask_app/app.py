import os
import redis
from flask import Flask, render_template_string
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Flask app with Redis counter', version='1.0.0')


@app.route('/')
def index():
    visits = r.incr('visits')
    return render_template_string('''
        <h1>Счётчик посещений</h1>
        <p>Вы посетили эту страницу {{ visits }} раз(а).</p>
    ''', visits=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
