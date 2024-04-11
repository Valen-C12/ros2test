from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    colors = {"background_r": "200"}

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    [
                        PathJoinSubstitution(
                            [
                                FindPackageShare("py_action"),
                                "launch",
                                "sub.launch.py",
                            ]
                        )
                    ]
                ),
                launch_arguments={
                    "turtlesim_ns": "turtlesim2",
                    "use_provided_red": "True",
                    "new_background_r": TextSubstitution(
                        text=str(colors["background_r"])
                    ),
                }.items(),
            )
        ]
    )
