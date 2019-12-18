# Fiducial SLAM
## Author: Addison Pitha
### Introduction
This project began as an effort to improve the localization capabilities of campus rover as an improvement to lidar based localization using AMCL. Motivating its conception were the following issues: Upon startup, in order to localize the robot, the user must input a relatively accurate initial pose estimate. After moving around, if the initial estimate is good, the estimate should converge to the correct pose. When this happens, this form of localization is excellent, however sometimes it does not converge, or begins to diverge, especially if unexpected forces act upon the robot, such as getting caught on obstacles, or being picked up. As AMCL uses a particle filter to estimate the robot's position, if the true pose of the robot starts changing in a significantly different manner than is expected, no particles will be close to the true pose, and will likely not converge again unless a good pose estimate is fed back to the robot.
Fiducials are square grids of large black and white pixels, with a bounding box of black pixels that can be easily identified in images. The pattern of pixels on the fiducial encodes data, and from the geometry of the bounding box of pixels within an image we can calculate its pose with respect to the camera. So, by fixing unique fiducials at different places within the robot's operating environment, fixed locations can be used to feed the robot accurate pose estimates without the user needing to do so manually. 
Therefore, the goal of this project was to use fiducial markers to generate a map of known landmarks, then use them for localization. At first it was unknown how accurate these estimates would be. If they were better than lidar data could achieve, fiducials would be used as the only pose estimation source, if not, they could be used simply as a correction mechanism.
2.	Problem statement, includeing original objectives
2.	Relevant literature
2.	What was created (biggest section)
1.	Technical descriptions, illustrations
2.	Discussion of interesting algorithms, modules, techniques
1.	kalman filter
2.	extended kalman filter
3.	landmark slam as the more advanced form of this project
3.	Story of the project.
1.	How it unfolded, how the team worked together
2.	problems that were solved, pivots that had to be taken
1.	aruco, fid slam running, not showing any errors, but rviz not showing image
1.	I thought this indicated the problem was with the camera, commence wild goose chase.
2.	Eventually determined, the issue was that move base was not being published to. Generated a map of the area and ran amcl on it, and the error changed. I learned I needed to publish the tf to the raspicam, and made a small static transform publisher.
3.	The ceiling lights were problematic because they could blind the camera and keep the robot from viewing fiducials. In our lab there was no real solution for this, and putting fiducials on walls would make them very likely to be obscured. I decided to mount on the ceiling anyway, and go reasonable results.
4.	Approaching the end, when I had gotten fiducial slam working and was preparing to mount more fiducials and improve accuracy, my code stopped working after I had made no changes to how I ran it from the previous time. I'm not sure what happened, and the problem persisted. I tried to diagnose it but couldn't, even with the TAs help.
3.	Your own assessment
1.	I think the error messages I received from the fiducial slam and aruco detect packages (more so fiducial slam) were very misleading at times, and made it so the focus of my project was just figuring out what certain errors meant, and how to configure information getting around to the right places. While I think I did a good job considering I had to deal with a load of frustrating errors, I am disappointed I didn't end up writing more code. I 


