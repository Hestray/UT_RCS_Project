import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/emma/Desktop/RCS Project/Project/install/turtlebot3_waypoints'
