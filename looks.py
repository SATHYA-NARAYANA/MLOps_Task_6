import os
#function for sending email from source to destination
def email_sent():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    fromaddr = "XXXXXXXXXXXXXX@gmail.com"
    toaddr = "XXXXXXXXXXXXXX@gmail.com"
   
    # instance of MIMEMultipart
    msg = MIMEMultipart()
  
    # For storing the senders email address  
    msg['From'] = fromaddr
  
    # For storing the receivers email address 
    msg['To'] = toaddr
  
    # For storing the subject 
    msg['Subject'] = "Sending sathya Photo from sathya"
  
    # string to store the body of the mail
    body = "this is the face of sathya verified from facial recognization"
  
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
    # open the file to be sent 
    filename = "sathya.jpg"
    attachment = open("./sathya.jpg", "rb")
  
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
  
    # To change the payload into encoded form
    p.set_payload((attachment).read())
  
    # encode into base64
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
  
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
    # start TLS for security
    s.starttls()
  
    # Login Authentication 
    s.login(fromaddr, "**************passward***********")
  
    # Converts the Multipart mmessage into a string
    text = msg.as_string()
  
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
  
    # terminating the session
    s.quit()

    
    
# Function for sending whatsapp message
def whatsapp_msg_sent():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly(
        phone_no="+911111111111", 
        message="Hello Sathya , Your Face Detected.....!!!"
    )