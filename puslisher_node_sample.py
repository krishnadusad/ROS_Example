import rospy
from std_msgs.msg import String # Replace String with any other ROS Message type

def Example():
	pub = rospy.Publisher('TOPIC_NAME_HERE', String) # Replace STRING with message type
	rospy.init_node('NODE_NAME_HERE', anonymous=True)
	rate = rospy.Rate(10) # 10hz # RATE AT WHICH YOU WANT TO PUBLISH
	


	while not rospy.is_shutdown():
		# Add any 'work' you're doing goes here.
		message_text = "Enter message here %s" % rospy.get_time()
		rospy.loginfo(hello_str) # Logs + sends message to ROSOUT
		pub.publish(hello_str) # Published message
		rate.sleep() # sleep for 10 seconds

if __name__ == '__main__':
	try:
 		Example()
 	except rospy.ROSInterruptException:
		pass