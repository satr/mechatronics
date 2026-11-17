# Independent headless lab; leave the existing ros2/ telemetry Dockerfile unchanged.
# The tag and APT repositories are moving inputs: reproducible steps, not locked bytes.
FROM ros:jazzy-ros-base
SHELL ["/bin/bash", "-c"]
# Inherit ROS_DISTRO from the official image; change only FROM to select a release.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-ros2-controllers \
    ros-${ROS_DISTRO}-robot-state-publisher \
    ros-${ROS_DISTRO}-tf2-ros \
    ros-${ROS_DISTRO}-ros2launch \
    ros-${ROS_DISTRO}-ros2controlcli \
    ros-${ROS_DISTRO}-std-msgs \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/control_lab
COPY arm.urdf controllers.yaml control.launch.py ./
# A new docker exec ... bash session uses its own interactive .bashrc.
RUN echo 'source "/opt/ros/${ROS_DISTRO}/setup.bash"' >> /root/.bashrc
CMD ["/bin/bash", "-lc", "source /opt/ros/${ROS_DISTRO}/setup.bash && exec ros2 launch /opt/control_lab/control.launch.py"]
