import paho.mqtt.client as mqtt  # 确保已安装paho-mqtt库:pip install paho-mqtt

# 定义SIOT服务器的连接信息
broker = "192.168.88.108"  # SIoT服务器的地址
port = 1883  # SIOT服务器的端口号
topic = "lnsf/G5"  # 指定要发布到的主题
username = "AIoT"
password = "AIoT"

# 连接回调函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 订阅主题（如果需要）
    client.subscribe(topic)

# 发布消息的回调函数
def on_publish(client, userdata, mid):
    print("Message published")

# 创建MQTT客户端
client = mqtt.Client()
client.username_pw_set(username, password)

# 设置连接和发布消息的回调函数
client.on_connect = on_connect
client.on_publish = on_publish

# 连接到SIOT服务器
client.connect(broker, port, 60)

# 待发布的数据
data = "hello-from mind+"

# 发布数据到主题
client.publish(topic, data)

# 保持通信
client.loop_forever()