import time

print("eli eatin loafs")

for i in range(1):
    t = 1*6
    while t:
        min = t // 60
        sec = t % 60
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(" " + timer, end = "\r")
        time.sleep(1)
        t -= 1
    print("now hes hungry.")
    t = 1*7
    while t:
        min = t // 60
        sec = t % 60
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(" " + timer, end = "\r")
        time.sleep(1)
        t -= 1
    print("turn the frogs gay")
