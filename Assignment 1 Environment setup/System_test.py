import sys

try:
    import numpy
except ImportError:
    print('Numpy is not installed, you will need this for some assignments in this course')

cur_version = sys.version_info

if cur_version >= (3,6):
    print("This an acceptable version of Python, version " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
else:
    print("Your Python version is to low, it needs to be 3.6 or greater and this is " + str(cur_version[0]) + '.' + str(
        cur_version[1]) + '.')

if 'numpy' in sys.modules:
    print('Numpy is installed, you are good to go here!')
