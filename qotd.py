# Import the required modules
import requests
from lxml import html
import smtplib
from smtplib import SMTPException
import yagmail

# Extracting the Quote of the Day from the webpage below
page = requests.get("https://www.brainyquote.com/quotes_of_the_day.html") # Get the webpage
tree = html.fromstring(page.content) # Convert page content into string, delete all html tags
qotdList = tree.xpath('//a[@title="view quote"]/text()') # Get the quote of the day by finding the html "a" tag titled "view quote"
qotdAuthorList = tree.xpath('//a[@title="view author"]/text()') # Get the author of the qotd by finding the html "a" tag titled "view author"
qotd = qotdList[0] # We only need the first element
qotdAuthor = qotdAuthorList[0] # We only need the first element
# print (qotd + "\n" +qotdAuthor) # To check the quote on the terminal screen

# Mail sending part
sender = "sender e-mail"
receiver = "receiver e-mail"
subject = "Quote of the Day"
message = "\"" + qotd + "\"" + "\n\n" + qotdAuthor + "\n\nFor more quotes please visit https://www.brainyquote.com/quotes_of_the_day.html"
yag = yagmail.SMTP(sender, 'Sender pass') # YAG is a powerful module which can easily handle sending mail for Google STMP  
yag.send(receiver,subject, message)
