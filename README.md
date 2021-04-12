# Valentine's-Day-Cards
Since many students chose to continue with online learning this school year, my school decided to do our annual valentine's day cards virtually. I didn't feel like making and sending a couple hundred cards manually so I wrote this script. :)

## Card generator
- Four valentine's card templates were made by other students
- Every student that wants to send a card to someone else fills out a form with the required info (names, email addresses, template choice)
- The program automatically goes through a .csv file with the required information, constructs the cards using the Pillow library, and saves it to the computer (I could have made it just send immediately but I wanted to filter everything manually in case there was anything inappropriate (I don't want to be expelled))

## Card distributor
- The cards are named by their index from the .csv list which corresponds to an email address
- The program finds the card and sends it out to the appropriate address
- I added a 15 second delay between each outgoing email since Google locks down your account if you send too many too quickly
