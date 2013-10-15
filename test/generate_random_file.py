"""
Generates Random data and writes to a file.
Takes the number of files and size of each file in MB as arguments.
Used for testing.
Author: Indradhanush Gupta
Github: https://github.com/indradhanush
Twitter: https://twitter.com/Indradhanush92
Facebook: https://www.facebook.com/Indradhanush
"""


import os
import sys


def generate_files(n, size):
    BASE_FILE_NAME = "test_file_"
    file_count = 1

    for i in xrange(n):
        name = "%s%s" % (BASE_FILE_NAME, str(file_count))
        file = open(name, "wb")
        file.write(os.urandom((1024**2)*size))
        file.close()
        file_count += 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Insufficient or Too Many Arguments! Enter the no. of files and size of each file in MB respectively."
        sys.exit()

    try:
        n = int(sys.argv[1])
        size = int(sys.argv[2])
    except(ValueError, TypeError):
        print "Arguments must be of type int"
        sys.exit()
    
    print "Creating %d files of size %d MB each..." % (n, size)
    generate_files(n, size)

