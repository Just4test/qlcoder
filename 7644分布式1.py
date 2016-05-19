# http://www.qlcoder.com/task/7644
# pip install kazoo

from kazoo.client import KazooClient

zk = KazooClient(hosts='121.201.8.217:2181')
zk.start()
data, stat = zk.get("/qlcoder/zookeeper")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))