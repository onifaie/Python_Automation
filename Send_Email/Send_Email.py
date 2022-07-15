import smtplib, ssl

def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "xxxxxx@gmail.com"
    receiver_email = "xxxxxxx@gmail.com"
    password = "xxxxxxxx"  # this password for application access from securty gmail ( manager email >> security >>>> create password application access 
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")
            
# send_email("hello this come from obeid 202")
# this file  for  how you can setting Timer to working every i minuit's 
