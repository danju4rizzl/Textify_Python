from twilio.rest import Client
import requests
import config

# Random verse API
text_message = requests.get(config.verse_of_the_day_url)

# Twilio Client
client = Client(config.account_sid, config.auth_token)
# The nu
receivers_number = ["+27812896956", "+13322014056"]


def send_message(receivers_number):
    """Send an SMS to the receivers number accepts the phone number as an argument """
    message = client.messages \
                    .create(
                        body=text_message,
                        from_=config.sender_number,
                        to=receivers_number
                    )


# If a verse of the day is available it will run the send_message function
if text_message.status_code == 200:
    send_message(receivers_number)
    print(f"Message has been sent to 😎👍: {receivers_number}")


# Sample of how the config file should look

# account_sid = "AC36***********"
# auth_token = "e7255***********"
# sender_number = "+19******"
# verse_of_the_day_url = "http://www.ourmanna.com/verses/api/get?format=text&order=random"
