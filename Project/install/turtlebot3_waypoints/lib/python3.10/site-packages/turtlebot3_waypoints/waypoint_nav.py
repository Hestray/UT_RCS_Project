import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose


class WaypointNavigator(Node):
    def __init__(self):
        super().__init__("waypoint_navigator")
        self.client = ActionClient(self, NavigateToPose, "navigate_to_pose")

        self.waypoints = [
            (3.49101352691, 0.933715581893, 0.0, 1.0),
            (6.31191015243, -2.781961917877, 0.0, 1.0),
            (2.3243594169, -3.749510765075, 0.0, 1.0)
        ]

    def make_pose(self, x, y, qz, qw):
        pose = PoseStamped()
        pose.header.frame_id = "map"

        pose.header.stamp.sec = 0
        pose.header.stamp.nanosec = 0
        # pose.header.stamp = self.get_clock().now().to_msg()
        
        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        pose.pose.orientation.z = float(qz)
        pose.pose.orientation.w = float(qw)
        return pose

    def run(self):
        self.get_logger().info("Waiting for navigate_to_pose action server...")
        self.client.wait_for_server()
        self.get_logger().info("Action server ready.")

        for i, (x, y, qz, qw) in enumerate(self.waypoints, start=1):
            goal = NavigateToPose.Goal()
            goal.pose = self.make_pose(x, y, qz, qw)

            self.get_logger().info(f"Sending waypoint {i}: x={x:.3f}, y={y:.3f}")

            send_future = self.client.send_goal_async(goal)
            rclpy.spin_until_future_complete(self, send_future)

            goal_handle = send_future.result()
            if not goal_handle.accepted:
                self.get_logger().error(f"Waypoint {i} rejected")
                return

            result_future = goal_handle.get_result_async()
            rclpy.spin_until_future_complete(self, result_future)

            status = result_future.result().status
            self.get_logger().info(f"Waypoint {i} finished (status={status})")


def main():
    rclpy.init()
    node = WaypointNavigator()
    node.run()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()