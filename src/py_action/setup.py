import os
from glob import glob
from setuptools import find_packages, setup

package_name = "py_action"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (
            os.path.join("share", package_name, "launch"),
            glob(os.path.join("launch", "*launch.[pxy][yma]*")),
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="valen",
    maintainer_email="valen@valen.wang",
    description="My first action",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "action_server = py_action.action_server:main",
            "action_client = py_action.action_client:main",
        ],
    },
)
