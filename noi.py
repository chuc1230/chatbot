import pyttsx3  
robot_brain= "hello chuc"  # suy nghi cua chat ao 
robot_say = pyttsx3.init() 
robot_say.say(robot_brain) 
robot_say.runAndWait() 