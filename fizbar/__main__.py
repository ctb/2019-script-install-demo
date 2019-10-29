import sys
import os

import pkg_resources
from pkg_resources import Requirement, resource_filename, ResolutionError

def get_pkg_data(filename):
    filepath = None
    try:
        filepath = resource_filename(
            Requirement.parse("fizbar"), "fizbar/" + filename)
    except ResolutionError:
        pass
    if not filepath or not os.path.isfile(filepath):
        filepath = os.path.join(os.path.dirname(__file__), filename)
    return filepath


def main():
    print('hello, world!')

    print('Running code from this directory:', os.path.dirname(__file__))
    print('')

    data = get_pkg_data('dist.dat')
    print('loading dist.dat from:', data)
    print('dist.dat contains:', open(data).read())
    return 0


if __name__ == '__main__':
    sys.exit(main())
