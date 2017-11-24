# import argparse
# import sys
# parser = argparse.ArgumentParser(
#     description='sum the integers at the command line')
# parser.add_argument(
#     'integers', metavar='int', nargs='+', type=int,
#     help='an integer to be summed')
# args = parser.parse_args()
# print sum(args.integers)

# print sum([1,2,4,5,6])

# import urlparse
# parse_url = urlparse.urlparse('zk://1.1.1.1:2181,2.2.2.2:2181,3.3.3.3:2181/mesos', scheme='zk:', allow_fragments=False)
# print parse_url.netloc, parse_url.path

# import os
# print os.path.join('/mesos', '')