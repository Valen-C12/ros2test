import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    turtlesim_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("launch_tutorial"), "launch"),
                "/turtlesim_world.launch.py",
            ]
        )
    )
    turtlesim_world_1 = GroupAction(
        actions=[
            PushRosNamespace("turtlesim1"),
            turtlesim_world,
        ]
    )
    turtlesim_world_2 = GroupAction(
        actions=[
            PushRosNamespace("turtlesim2"),
            turtlesim_world,
        ]
    )

    broadcaster_listener_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("launch_tutorial"), "launch"),
                "/broadcaster_listener.launch.py",
            ]
        ),
        launch_arguments={"target_frame": "carrot1"}.items(),
    )

    mimic_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("launch_tutorial"), "launch"),
                "/mimic.launch.py",
            ]
        )
    )

    fixed_frame_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("launch_tutorial"), "launch"),
                "/fixed_broadcaster.launch.py",
            ]
        )
    )

    rviz_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(get_package_share_directory("launch_tutorial"), "launch"),
                "/turtlesim_rviz.launch.py",
            ]
        )
    )

    return LaunchDescription(
        [
            turtlesim_world_1,
            turtlesim_world_2,
            broadcaster_listener_nodes,
            mimic_node,
            fixed_frame_node,
            rviz_node,
        ]
    )
