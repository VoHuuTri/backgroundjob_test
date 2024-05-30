import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return f"Current temperature in {city} is {data['main']['temp']}°C"

def create_content():
    return "this is content for email"

def send_email(sender_email, password, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Configuration
sender_email = 'tricopro789@gmail.com'
password = '0966188549As'
receiver_email = 'vo.huu.tri578@mail.com'

# Main
email_content = create_content()
send_email(sender_email, password, receiver_email, 'test job email', email_content)
