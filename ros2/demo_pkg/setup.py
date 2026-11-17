from setuptools import find_packages, setup

package_name = 'telemetry_demo'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/demo.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Training maintainers',
    maintainer_email='noreply@example.invalid',
    description='Simulation-only ROS 2 topic and service demonstration',
    license='Apache-2.0',
    entry_points={'console_scripts': [
        'sample_source = telemetry_demo.publisher:main',
        'sample_monitor = telemetry_demo.subscriber:main',
    ]},
)
