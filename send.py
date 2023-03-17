import pywhatkit
import random
import time

MESSAGES=["Message1",
          "Message2",
          "Message3",
          ]

PHONE_NUMBERS=["+9721234567",
               "+9721234567",
               "+9721234567",
               "+9721234567",
               "+9721234567",
               "+9721234567",
               "+9721234567",
               "+9721234567",
               "+9721234567",
               ]

TIME_TO_WAIT_BEFORE_SENDING_FIRST_MESSAGE_SECONDS=1
TIME_TO_WAIT_BETWEEN_MESSAGES_SECONDS=10
MAX_MESSAGES_TO_SEND_TO_EACH_NUMBER=3

time.sleep(TIME_TO_WAIT_BEFORE_SENDING_FIRST_MESSAGE_SECONDS)

phoneNumbersToSendTo=list()

for phone in PHONE_NUMBERS:
    for i in range(MAX_MESSAGES_TO_SEND_TO_EACH_NUMBER):
        phoneNumbersToSendTo.append(phone
                                    )


while (len(phoneNumbersToSendTo)>0): 
    randomPhone=random.choice(phoneNumbersToSendTo)
    phoneNumbersToSendTo.remove(randomPhone)
    randomMessage=random.choice(MESSAGES)
    pywhatkit.sendwhatmsg_instantly(phone_no= randomPhone, message= "hello", wait_time= 10, tab_close= True, close_time= 3)
    print(f"Sending message {randomMessage} to {randomPhone}")
    time.sleep(TIME_TO_WAIT_BETWEEN_MESSAGES_SECONDS)