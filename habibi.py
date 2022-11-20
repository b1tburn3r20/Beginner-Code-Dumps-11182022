import time

print("Yassalah habeeeb")

for i in range(1):
    t = 1*8
    while t:
        min = t//60
        sec = t%60
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(" " + timer, end= '\r')
        time.sleep(1)
        t-=1
    print("WE DID IT!")
    break
    