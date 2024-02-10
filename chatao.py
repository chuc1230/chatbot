# phan nghe 
import speech_recognition as sr # nghe 
import pyttsx3  # noi 
from datetime import date
from datetime import datetime 
today = date.today()

#day = today.strftime("%B %d, %Y")

robot_ear = sr.Recognizer() # khởi tạo 1 biến có thể nghe
robot_say = pyttsx3.init()  # biến nói 
robot_brain = "" # biến trả lời 
while True:
     with sr.Microphone() as mic:  # khi dung with mic dung xong se tat di

       print("Toi dang nghe")
       audio = robot_ear.listen(mic)  # Thời gian nghe là 5 giây :(mic,timeout=5)
     print("vui lòng chờ giây lát ")
     try:  
       you = robot_ear.recognize_google(audio,language="vi-VN") # ngôn ngữ nghe được là tiếng việt :language="vi-VN"
     except:
       you = "" # nếu lỗi sẽ trả về 

     print("you:=",you)

    # phan hiểu 
    # day la phan tri tue nhan tao

     if you =="":
        robot_brain = "tôi không nghe thấy , hãy nói lại "
     elif "Hello" in you:
        robot_brain = "chào  bạn  "
     elif "today" in you:
        today = date.today()
        robot_brain = today
     elif "thời gian" in you :
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
     elif "tạm biệt" in you:
        robot_brain = "cảm ơn đã sử dụng "
        robot_say = pyttsx3.init() 
        robot_say.say(robot_brain) 
        robot_say.runAndWait()
        break
     print(robot_brain)


    # phan noi
     
     robot_say = pyttsx3.init() 
     robot_say.say(robot_brain) 
     robot_say.runAndWait() 