#The smtplib library is used in Python to send emails using 
# the Simple Mail Transfer Protocol (SMTP).
# it allows us to connect to an email server and send emails.
import smtplib

#We take the Input From the user  
# "abt- to what email the message is to be sent"
#and store it , in the variable 'to'.
to = input("Enter The Email to Which The Message is to be Sent: ")

#The message to be sent is stored in the variable '
message = input("Enter The Message to be Sent:")


#The function sendEmail takes two parameters: 
# to (the recipient’s email address) 
# and message (the message content).
#This function contains the logic for sending the email.
def sendEmail(to, message):
    
    #smtplib.SMTP('smtp.gmail.com', 587) connects to Gmail’s SMTP server
    # using the server address 'smtp.gmail.com' and port 587.
    #Port 587- is commonly used for email submission and supports encrypted communication.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    #starttls() initializes the connection with TLS (Transport Layer Security) encryption,
    # which secures the email exchange.
    #This step is crucial for securely logging in and sending emails.
    server.starttls()
    
    #server.login() logs into the Gmail account using the email address and password
    #Make a new GMAIL account, dont use personel one.
    #For More Detail about Password , Scroll Down at Last
    #server.login('<your_email>@gmail.com', 'xxxx xxxx xxxx xxxx')
    server.login('XXXXXXXXXXXXXXX58@gmail.com', 'xxxx xxxx xxxx xxxx')
    
    
    #server.sendmail() sends the email.
    #It takes three arguments: 
    # the sender’s email address, 
    # the recipient’s email address (to), 
    # and the message content(message).
    server.sendmail('XXXXXXXXXXXXXXX58@gmail.com', to, message)
    
    
    #erver.close() ends the connection to the SMTP server, releasing resources.
    server.close()


#This line calls the sendEmail() function with the to (recipient email) and message as arguments,
# triggering the process of sending the email.
sendEmail(to, message)


'''
#Suggestion: 

#To check Whether this code works , We'll Go to a website Named -
#--> www.10minutemail.com
#there, we'll be copying the Temporary Email generated 
#and pass it in the "to" variable
#the message send to that Temp email, will be showing in the inbox of that website
#Keep note That Temp Email is Only For 10 Mins

'''


'''
#Password:

In this line:
server.login('automationpurpose58@gmail.com', 'xxxx xxxx xxxx xxxx')

the second parameter (`'xxxx xxxx xxxx xxxx'`) is where you would place the password for the Gmail account `automationpurpose58@gmail.com`.
For Gmail, however, you'll typically need an "app-specific password" rather than your "regular Gmail password", 
especially if two-factor authentication (2FA) is enabled.

Here's how to obtain the app-specific password:

### Steps to Get an App-Specific Password for Gmail

1.   Enable Two-Factor Authentication (2FA):
   - Go to [Google Account Security]-->(https://myaccount.google.com/security).
   - Under "Signing in to Google," set up "2-Step Verification" (if it's not already enabled).
   - Follow the prompts to enable two-factor authentication.

2.   Generate an App Password:
   - Once 2FA is enabled, go back to the "Security" section.
   - Look for "App Passwords" under "Signing in to Google."
   - You may need to enter your password again(i.e Regular Password) for security.
   - Choose "Mail" as the app and "Windows Computer" (or other suitable option) as the device.
   - Google will generate a 16-character password specifically for use with this app. 
   - in the form - xxxx xxxx xxxx xxxx
   -ps: Do not Share this with anyone

3.   Use the App-Specific Password in Your Code:
   - Replace "xxxx xxxx xxxx xxxx" in your code with the generated app password:
   
         server.login('automationpurpose58@gmail.com', 'your_generated_app_password') (i.e --> xxxx xxxx xxxx xxxx)

--> Note: An app password is safer than your regular Google password because
it provides access only to that specific app or device. 
Also, avoid hardcoding passwords directly into code.
Instead, you could load them from environment variables or a separate configuration file for better security.

'''
