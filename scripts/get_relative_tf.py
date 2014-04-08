#!/usr/bin/env python

import roslib
import rospy
import sys
import argparse
import tf



def main(args):
  parser = argparse.ArgumentParser()
  parser.add_argument('from_tf', help='Base Frame')
  parser.add_argument('to_tf', help='Target Frame')
  args = parser.parse_args()
  from_tf, to_tf = args.from_tf, args.to_tf

  rospy.init_node('get_relative_tf', anonymous=True)
  tf_listener = tf.TransformListener()
  rospy.sleep(rospy.Duration(0, 500 * 1000))

  try:
    tf_listener.waitForTransform(to_tf, from_tf, rospy.Time(), rospy.Duration(4.0))

  position, quaternion = tf_listener.lookupTransform(to_tf, from_tf, rospy.Time.now())
  print position, quaternion


if __name__ == '__main__':
  main(sys.argv)
