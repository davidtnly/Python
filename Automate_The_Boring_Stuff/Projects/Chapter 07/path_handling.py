import os
# os.path module provides functions for returning the absolute path of a relative path and for checking whether a given
# path is an absolute path

# os.path.abspath(path) will return a string of the absolute path of the argument, which is an easy way to convert
# a relative path into an absolute one
p = os.path.abspath(' .')
print(p)
os.path.abspath('.\\Scripts')

# os.path(isabs(path)) will return True if the argument is an absolute path and False if it's a relative path
os.path.isabs('.')

# os.path.relpath(path, start) will return a string of a relative path from the start part to path
os.path.isabs(os.path.abspath('.'))

