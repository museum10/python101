import time
import webbrowser

total_breaks = 3
break_count = 0

print("This problem started on "+ time.ctime() )
while(break_count < total_breaks):
    time.sleep(10) # 두시간 간격으로 해야하지만 테스트를 위해서 10초로 설
    webbrowser.open("https://www.youtube.com/watch?v=bkHzvEnFsZ0")
    break_count = break_count + 1
    
