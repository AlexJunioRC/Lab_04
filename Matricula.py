import rospy
from std_msgs.msg import String
    
rospy.init_node('Matricula')

soma = String()
matricula = String()
       
def FunCB (msg):
    global soma
    soma = msg
    print ("A soma e :" + soma.data)
    
def Timer(event):
    msg = String()
    msg.data = '2017004555'
    print ("A Matricula e " + msg.data)
  
    pub.publish(msg) 

    
pub = rospy.Publisher ('/Matricula', String, queue_size =10)
sub = rospy.Subscriber('/Soma', String,FunCB)
timer = rospy.Timer(rospy.Duration(0.1),Timer)

rospy.spin()