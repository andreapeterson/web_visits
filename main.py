from flask import Flask
import redis

app = Flask(__name__)
client = redis.StrictRedis(host='redis-server', port=6379) # So when our app starts up, it will try to create a connection to a redis server & reach out looking for a host name of 'redis-server' and will be redirected to redis container
client.set('visits', 1)

@app.route('/')
def index():
    visits = client.get('visits').decode('utf-8')
    client.set('visits', int(visits) + 1)
    return 'Number of visits is: ' + visits

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)