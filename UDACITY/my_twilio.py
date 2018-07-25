from twilio.rest import Client

# your account Sid and auth token from twilio.com/user/account
account_sid = "ACca66de517eee4d8d0d639aaac7139abc"
auth_token = "93c3620639823115019bf96b9c1a6238"
client = Client(account_sid, auth_token)

message =client.messages.create(
	body = "Hi Eva, you can do it! Never give and keep trying < 3",
	to = "+254722811823",
	from_ = "+18472683315")
print(message.sid)
