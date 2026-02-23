from setuptools import find_packages, setup

package_name = 'turtlebot3_waypoints'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/static_base_scan_tf.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emma',
    maintainer_email='barzanemma@gmail.com',
    description='Turtlebot3 trajectory planning project',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'waypoint_nav = turtlebot3_waypoints.waypoint_nav:main',
        ],
    },
)
