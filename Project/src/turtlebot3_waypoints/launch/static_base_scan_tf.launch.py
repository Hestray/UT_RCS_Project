from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["0", "0", "0", "0", "0", "0", "base_footprint", "base_scan"],
            output="screen",
        )
    ])


# this is the equivalent of running the command:
# ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_footprint base_scan


# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     base_footprint_to_base_scan = Node(
#         package="tf2_ros",
#         executable="static_transform_publisher",
#         arguments=["0", "0", "0", "0", "0", "0", "base_footprint", "base_scan"],
#         output="screen",
#         name="tf_base_footprint_to_base_scan",
#     )

#     base_footprint_to_base_link = Node(
#         package="tf2_ros",
#         executable="static_transform_publisher",
#         arguments=["0", "0", "0", "0", "0", "0", "base_footprint", "base_link"],
#         output="screen",
#         name="tf_base_footprint_to_base_link",
#     )

#     return LaunchDescription([
#         base_footprint_to_base_scan,
#         base_footprint_to_base_link,
#     ])


# # this is the equivalent of running the command:
# # ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_footprint base_scan
# # ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_footprint base_link