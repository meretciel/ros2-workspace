from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            output='screen',
            emulate_tty=True,
            package='python_package_that_uses_parameters_and_launch_files',
            executable='amazing_quote_configurable_publisher_node',
            name='peanut_butter_falcon_quote_publisher_node',
            parameters=[{
                'topic_name': 'truly_inspirational_quote',
                'period': 0.25,
                'quote': 'Yeah, that is right',
                'philosopher_name': 'Tyler'
            }]
        )
    ])