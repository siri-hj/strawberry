import random
from redis import Redis

class Config():
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

def Random_num():
    num = random.randint(1000, 9999)
    return num

#数据路径链接
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Root123@localhost:3306/hj'


redis_store = Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)