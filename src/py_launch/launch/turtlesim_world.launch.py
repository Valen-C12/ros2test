import os

from ament_index_python.packages import get_package_share_directory
from launch.actions import GroupAction
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory("py_launch"), "config", "turtlesim.yaml"
    )

    namespace = LaunchConfiguration("namespace", default="default")
    node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="sim",
        parameters=[config],
    )
    node_with_namespace = GroupAction(
        actions=[PushRosNamespace(namespace), node],
    )

    return LaunchDescription([node_with_namespace])
