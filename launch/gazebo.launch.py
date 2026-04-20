import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os



def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='walker_rosys').find('walker_rosys')
    default_model_path = os.path.join(pkg_share, 'urdf/walker.urdf')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': Command([
                'xacro ', LaunchConfiguration('model'),
                ' enable_gazebo_plugin:=', LaunchConfiguration('enable_gazebo_plugin')
            ])
        }]
    )

    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )

    spawn_entity = launch_ros.actions.Node(
    package='gazebo_ros',
    executable='spawn_entity.py',
    arguments=['-entity', 'walker_robot', '-topic', 'robot_description'],
    output='screen'
    )

    static_transform_node_wrist_right = launch_ros.actions.Node(
    package='tf2_ros',
    executable='static_transform_publisher',
    arguments=['-0.3', '-0.3', '0.8', '0', '0', '0', 'base_link', 'wrist_right_link'],
    output='screen')

    static_transform_node_wrist_left = launch_ros.actions.Node(
    package='tf2_ros',
    executable='static_transform_publisher',
    arguments=['-0.3', '0.3', '0.8', '0', '0', '0', 'base_link', 'wrist_left_link'],
    output='screen')



    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(
            name="enable_gazebo_plugin",
            default_value="false",
            description="Enable Gazebo plugin section in URDF file",
        ),
        launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'], output='screen'),
        joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_entity,
        static_transform_node_wrist_left,
        static_transform_node_wrist_right,
    ])
