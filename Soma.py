import rospy
from std_msgs.msg import String

rospy.init_node('Soma')


def CallBack(msg):  # Recebe a matricula e calcula a soma
    soma = 0
    for a in range(len(msg.data)):
        soma = soma + int(msg.data[a])
    msg.data = str(soma)
    pub.publish(msg)


pub = rospy.Publisher('/Soma', String, queue_size=10)
sub = rospy.Subscriber('/Matricula', String, CallBack)

rospy.spin()