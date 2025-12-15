import smtplib,ssl

#content="Subject: Hi user \n hello,sending mail from python code"

email_to=['receiver's email id']
content=f'''Subject: A plain text email
To: {','.join(email_to)}
This is a new test email sent from python.'''

# Create a secure SSL context
context = ssl.create_default_context()
mail=smtplib.SMTP_SSL("smtp.gmail.com",465, context=context)
mail.login("abc@gmail.com","qgvhkmyft")
mail.sendmail("abc@gmail.com",email_to,content)
print("email sent")
mail.quit()
