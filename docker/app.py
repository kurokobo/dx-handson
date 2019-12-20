from flask import Flask
from redis import Redis, RedisError
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)


@app.route("/")
def helloworld():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Cannot connect to Redis, counter disabled.</i>"

    html = """
        <h3>Hello World!</h3>
        <p>Here I am having fun with Docker and Kubernetes!!</p>
        <p><strong>Visits:</strong> {visits}</p>
        <p>Request served by server: {hostname}</p>
        """.format(
        visits=visits, hostname=socket.gethostname()
    )
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
