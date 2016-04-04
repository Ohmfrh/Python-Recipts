from guideControl import *
import sys


__author__ = 'daniel'


def main():
    try:
        if sys.argv[1] == 'dhl':
            dhl()
        elif sys.argv[1] == 'fedex':
            fedex()
        else:
            print "Invalid argument [",sys.argv[1],"]. Try with 'dhl' or 'fedex'."

    except IndexError:
        print 'Error: Not enough arguments\n Ex: python gprint.py [dhl or fedex]'
    except:
        print 'Unexpected Error:', sys.exc_info()


if __name__ == "__main__":
    main()

