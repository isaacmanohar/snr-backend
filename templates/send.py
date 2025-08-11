from twilio.rest import Client

account_sid = 'AC6ab203e14c95d74b68686f1dc3769ddb'
auth_token = '9ac20e7e95a57ebe4e9bff23d76d3bde'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',  # Twilio sandbox number
    to='whatsapp:+918639975947',    # Your verified WhatsApp number
    body='🚨 SnapResolve Alert:\nOverflowing garbage near the park entrance.',
    media_url=['https://res.cloudinary.com/dndlmtrgx/image/upload/v1/ea5wderpyxxq176llsul.png']
)

print("Message SID:", message.sid)
