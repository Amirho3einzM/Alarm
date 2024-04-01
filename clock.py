from playsound import playsound
import time
ClEAR = "\033[2J"
ClEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elased=0
    print(ClEAR)
    while seconds>time_elased:
        time.sleep(1)
        time_elased+=1
        time_lift=seconds-time_elased
        minutes_left=time_lift//60
        seconds_left=time_lift%60
    
        print(f"{ClEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    playsound("./alarm.mp3")
    
minutes=int(input("Please Enter Your Minutes: "))
seconds=int(input("Please Enter Your Seconds: "))
total_time=minutes*60+seconds
alarm(total_time)