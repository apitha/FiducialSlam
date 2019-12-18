ssh donatello@donatello.dyn.brandeis.edu
bu

ssh donatello@donatello.dyn.brandeis.edu
roslaunch raspicam_node camerav2_1280x960_10fps.launch

rosrun fiducial_slam_2_electric_boogaloo rpicam_tf.py

roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/fid_slam_3.yaml

roslaunch fiducial_slam_2_electric_boogaloo fid_slam_all.launch 

roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch









roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

rosrun map_server map_saver -f ~/fid_slam_x
