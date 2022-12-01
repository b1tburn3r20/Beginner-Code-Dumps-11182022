from twilio.rest import Client
import time

def main():
    start_time = time.time();
    
    From="+12537858825"
    To="+15157716589"
    
    CT = 0
    LIMIT = 15
    
    ACCOUNT_SID="AC5ced4a736aabb8f79a9cf69ea8510914"
    AUTH_TOKEN="9e6485a950befb36c1c97d4b1bdf00fa"
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    while CT < LIMIT:
        call = Client.call.create(
            to=To,
            from_=From,
            url = "https://www.youtube.com/watch?v=DehK_Y0TUbE"
        )
        
        CT = CT+1
        
        time.sleep(3600.0)
if __name__ == '__main__':
    print("Angry BIRDS INCOMING!!")
    main()