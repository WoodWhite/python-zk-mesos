#!/usr/bin/env python

from __future__ import print_function

import argparse
import json
import logging

from utils import zookeeper_discovery, ZookeeperNoMaster

""" Executable to discover Leading Mesos Master against a ZooKeeper ensemble.

    This is example code to show how the classes in
    `mesos_commons.discovery` could be used to discover a running Master, by
    pointing it to the ZooKeeper ensemble.

    To run it, simply execute it with a `--zk` option pointing to the same URL
    as the one used to launch `mesos-master.sh`.

    Run it for more information with as::

        python run.py --help

    to see all possible command options.

    Author: Shaobo Li (lishaobo@dnion.com)
"""


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--zk', required=True,
                        help="Zookeeper ensemble URI(s), eg, zk://10.10.1.2:2181,10.10.1.3:2181.")
    parser.add_argument('-a', default=False, dest='all', action='store_true',
                        help="Retrieve all Mesos Masters, not just the Leader")
    parser.add_argument('--mesos-version', default='0.24.0',
                        help="The Apache Mesos version for the Master.")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Verbose logging (off by default)")
    return parser.parse_args()


def main(cfg):
    logging.info(
        "Connecting to Zookeeper at {}".format(cfg.zk))
    zk_discovery = zookeeper_discovery(cfg.mesos_version, cfg.zk,
                                       timeout_sec=15)
    logging.info("Connected")
    try:
        if cfg.all:
            res = zk_discovery.retrieve_all()
            logging.info("Found {} Masters; current Leader: {}".format(len(res), res[0].get('hostname')))
        else:
            res = zk_discovery.retrieve_leader()
            logging.info("Found leader: {}".format(res.get('hostname')))
        print(json.dumps(res, indent=4, separators=[',', ':']))
    except ZookeeperNoMaster as ex:
        logging.error("Could not find any Mesos Master: {}".format(ex.message))


if __name__ == "__main__":
    FORMAT = '%(asctime)-15s [%(levelname)-5s] %(message)s'
    config = parse_args()
    level = logging.DEBUG if config.verbose else logging.INFO
    logging.basicConfig(format=FORMAT, level=level, datefmt='%Y-%m-%d %H:%M:%S')
    main(config)
