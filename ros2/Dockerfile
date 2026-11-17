# ROS 2 Jazzy Jalisco (LTS, supported through May 2029).
# The base image tag AND apt package indexes are mutable. An image digest
# pins only the base; fixed package inputs and controlled builds are needed
# before any stronger reproducibility claim. Review upstream updates.
FROM ros:jazzy-ros-base
# Official image ENV ROS_DISTRO supplies the package prefix and setup path.
SHELL ["/bin/bash", "-c"]
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    ros-${ROS_DISTRO}-rclpy \
    ros-${ROS_DISTRO}-demo-nodes-cpp \
    ros-${ROS_DISTRO}-demo-nodes-py \
    ros-${ROS_DISTRO}-std-msgs \
    ros-${ROS_DISTRO}-std-srvs \
    ros-${ROS_DISTRO}-launch-ros \
    ros-${ROS_DISTRO}-ros2launch \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/training_ws
COPY demo_pkg/ src/telemetry_demo/
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon build --packages-select telemetry_demo
# Enable ROS underlay and this compiled overlay in all new interactive exec shells.
RUN { echo 'source "/opt/ros/${ROS_DISTRO}/setup.bash"'; \
      echo 'source /opt/training_ws/install/setup.bash'; } >> /root/.bashrc
CMD ["/bin/bash", "-lc", "source /opt/ros/${ROS_DISTRO}/setup.bash && source /opt/training_ws/install/setup.bash && exec ros2 launch telemetry_demo demo.launch.py"]
