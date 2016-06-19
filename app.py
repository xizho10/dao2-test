from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=53810)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.===' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="10.10.189.180", debug=True)
