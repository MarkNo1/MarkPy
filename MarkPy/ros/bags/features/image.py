# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

counters = dict(camera0=0,camera1=0,camera2=0)
# Instantiate CvBridge
bridge = CvBridge()

def image_callback_camera0(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        counters['camera0'] +=1
        # Save your OpenCV2 image as a jpeg
        img_name = 'camera_left_' + str(counters['camera0']) + '.jpeg'
        cv2.imwrite(img_name, cv2_img)

def image_callback_camera1(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        counters['camera1'] +=1
        # Save your OpenCV2 image as a jpeg
        img_name = 'camera_central_' + str(counters['camera1']) + '.jpeg'
        cv2.imwrite(img_name, cv2_img)

def image_callback_camera2(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg
        counters['camera2'] +=1
        img_name = 'camera_right_' + str(counters['camera2']) + '.jpeg'
        cv2.imwrite(img_name, cv2_img)

def main():
    rospy.init_node('image_listener')
    # Set up your subscriber and define its callback
    rospy.Subscriber("/HR/Camera/0/Image", Image, image_callback_camera0)
    # rospy.Subscriber("/HR/Camera/1/Image", Image, image_callback_camera1)
    # rospy.Subscriber("/HR/Camera/2/Image", Image, image_callback_camera2)
    # Spin until ctrl + c
    rospy.spin()
