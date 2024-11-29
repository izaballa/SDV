import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/natxozm13/Desktop/SDV/ros2/vesc/install/vesc'
