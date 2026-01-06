import redis
#from redis.cluster import RedisCluster
import json
from redis.commands.json.path import Path

#client = RedisCluster(host='0.0.0.0', port=6379)
r = redis.Redis(host='localhost', port=6379)

result = r.get('profile1')
print(result)

info = r.info()
total_connections = info['total_connections_received']
print(total_connections)