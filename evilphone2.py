from twilio.rest import Client
account_sid = "AC5ced4a736aabb8f79a9cf69ea8510914"
auth_token = "9e6485a950befb36c1c97d4b1bdf00fa"
client = Client(account_sid, auth_token)

call=client.calls.create(
    to="+12014789503",
    from_="+12537858825",
    url="https://demo.twilio.com/docs/voice.xml"
)

print(call.sid)