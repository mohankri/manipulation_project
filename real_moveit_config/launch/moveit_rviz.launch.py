from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder(
        "ur",                                   # the real stem from config/ — not "name"
        package_name="real_moveit_config"
    ).to_moveit_configs()

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', str(moveit_config.package_path / 'config' / 'moveit.rviz')],
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,   # the fixed yaml, now non-empty
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            {'use_sim_time': True},                       # per-world
        ],
    )
    return LaunchDescription([rviz_node])