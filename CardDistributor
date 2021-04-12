import pandas
import yagmail as yg
import time

data = pandas.read_csv( )   # Address of form data
kMail = "Recipient's k12 Email (Please make sure that your spelling is correct. If the email does not " \
        "exist, we will be unable to send your card.)"

error = []
rMail = []

for i in range(len(data[kMail])):
    rMail.append(data[kMail][i])

for i in range(len(rMail)):
    try:
        yag = yg.SMTP(user= , password= )   # gmail address and password of sender
        yag.send(
            to=rMail[i],
            subject="School Valentine's Day Gram!",
            contents=["You received a valentine's day gram!\n\nThis email was an automated message from "
                      "the school, please only reply if there are any issues.", f"{i}.png"]
            )
    except:   # General except used since I'm not sure what exceptions yagmail can throw
        error.append([i, rMail[i]])

    time.sleep(15)   # Delay sot that Google doesn't lock down account

print(error)
