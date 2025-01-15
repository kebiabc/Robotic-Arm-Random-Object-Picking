'''
ROS 话题触发：
发布话题 /to_485 并发送字符串命令：
rostopic pub /to_485 std_msgs/String "data: 'open_gripper'"

接收响应：
夹爪设备的 485 响应通过 from_485 话题发布，可以通过以下命令查看：
rostopic echo /from_485

打开夹爪:
rostopic pub /to_485 std_msgs/String "data: 'open_gripper'"

关闭夹爪:
rostopic pub /to_485 std_msgs/String "data: 'close_gripper'"
'''


#!/usr/bin/env python
import rospy
import socket
from std_msgs.msg import String

class TCPTo485:
    def __init__(self, ip, port):
        self.server_address = (ip, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect(self.server_address)
            rospy.loginfo(f"Connected to TCP server at {ip}:{port}")
        except socket.error as e:
            rospy.logerr(f"Failed to connect to TCP server: {e}")
            rospy.signal_shutdown("TCP connection error")

    def send_to_485(self, data):
        try:
            rospy.loginfo(f"Sending data (hex): {' '.join(format(x, '02x') for x in data)}")
            self.client.sendall(data)
            rospy.loginfo(f"Sent to 485: {data}")
        except socket.error as e:
            rospy.logerr(f"Error sending data: {e}")

    
    def receive_from_485(self):
        try:
            return self.client.recv(1024)
        except socket.error as e:
            rospy.logerr(f"Error receiving data: {e}")
            return b""

def tcp_to_485_node():
    rospy.init_node("tcp_to_485_node")
    
    # 获取参数
    ip = rospy.get_param("~ip", "192.168.1.40")  # TCP 服务器 IP
    port = rospy.get_param("~port", 8890)     # TCP 服务器端口

    tcp_client = TCPTo485(ip, port)

    # 发布和订阅 ROS 话题
    pub = rospy.Publisher("from_485", String, queue_size=10)  # 从 485 收到的数据
    
    def callback(msg):
        rospy.loginfo(f"Processing command: {msg.data}")
        # 将指令转为字节形式
        if msg.data == "open_gripper":
            # 夹爪打开指令
            command = bytearray([0x01, 0x10, 0x9C, 0x40, 0x00, 0x01, 0x02, 0x00, 0x64, 0xF5, 0x72])
        elif msg.data == "close_gripper":
            # 夹爪关闭指令
            command = bytearray([0x01, 0x10, 0x9C, 0x40, 0x00, 0x01, 0x02, 0x00, 0x00, 0xF4, 0x99])

        else:
            rospy.logwarn(f"Unknown command: {msg.data}")
            return
        
        tcp_client.send_to_485(command)
    
    rospy.Subscriber("to_485", String, callback)  # 需要发送到 485 的数据
    
    # 持续接收数据并发布
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        recv_data = tcp_client.receive_from_485()
        if recv_data:
            rospy.loginfo(f"Received from 485: {recv_data}")
            pub.publish(recv_data.decode(errors='ignore'))
        rate.sleep()

if __name__ == "__main__":
    try:
        tcp_to_485_node()
    except rospy.ROSInterruptException:
        pass

