import speech_recognition as sr

robot_ear = sr.Recognizer() # khởi tạo 1 biến có thể nghe
with sr.Microphone() as mic:  # khi dung with mic dung xong se tat di

   print("Toi dang nghe")
   audio = robot_ear.listen(mic)  # Thời gian nghe là 5 giây :(mic,timeout=5)
try:  
   you = robot_ear.recognize_google(audio,language="vi-VN") # ngôn ngữ nghe được là tiếng việt 
except:
   you = "" # nếu lỗi sẽ trả về 

print("you:=",you)
