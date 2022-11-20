import time

print("its elis birthday today!")

for i in range(1):
    t = 1*6
    while t:
        min = t // 60
        sec = t % 60
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(" " + timer, end = "\r")
        time.sleep(1)
        t -= 1
    print ('john arbuckle is a serial killer')
    t = 1*9
    while t:
        min = t // 60
        sec = t % 60
        timer = '{:02d}:{:02d}'.format(min, sec)
        print (" " + timer, end = "\r")
        time.sleep(1)
        t -= 1
    print ("aunt jamyma is hard to spell")
    break
    
    
