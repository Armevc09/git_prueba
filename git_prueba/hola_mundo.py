import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node('nodo_hola_mundo')
    node.get_logger().info('funcionando')
    rclpy.shutdown()

if __name__ == '__main__':
    main()
