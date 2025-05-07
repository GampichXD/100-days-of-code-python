from twilio.rest import Client

account_sid = 'ACed8aadda05be248be2ac7804dfe18421'
auth_token = '3a23c3e78e5a3ed2bfdbf99bacfe0528'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  # content_variables='{"1":"12/1","2":"3pm"}',
    body="jasdasjd",
  to='whatsapp:+6282320835440'
)

print(message.body)