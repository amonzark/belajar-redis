import redis
#from redis.cluster import RedisCluster
import json
from redis.commands.json.path import Path

#client = RedisCluster(host='0.0.0.0', port=6379)
r = redis.Redis(host='localhost', port=6379)

profile = {
     'name': "Jane", 
     'Age': 33, 
     'Location': "Chawton"
   }

jsonprofile = json.dumps(profile)

r.setex('profile1', 10, jsonprofile)

result = r.get('profile1')
print(result)