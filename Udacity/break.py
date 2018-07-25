import time
import webbrowser
total_breaks = 3
total_count = 0
print("This program started on" + time.ctime())
while (total_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=0Wbc5ZwkAMw")
    total_count += 1