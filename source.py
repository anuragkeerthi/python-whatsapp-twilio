from twilio.rest import Client 

#You will get the below code after you signup Twilio

account_sid = 'AC10743ae997e17bf5e38d54ca79fcbe7b' 
auth_token = '76062e63d6e4b6b7e8ac39c26d6683f5' 
client = Client(account_sid, auth_token) 

def send_message():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Wake Up! ',      
                                to='whatsapp:+918125559655' 
                            ) 
    
    print(message.sid)