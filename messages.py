# -*- coding: utf-8 -*-



# Change this to your name!
name = 'Guido van Rossum'



from bs4 import BeautifulSoup
import datetime
import json
import codecs

with open("messages.htm") as f:
  text = f.read()
soup = BeautifulSoup(text, 'html.parser')

messages_from_this_name = codecs.open("messages_from_this_name.txt", "w+",'utf-8')

data = []
for a in soup.find_all('div', attrs={'class':'thread'}):
  thread = []
  for b in  a.find_all('div', attrs={'class':'message'}):
    user    = b.find('span', attrs={'class':'user'}).text
    time    = datetime.datetime.strptime(b.find('span', attrs={'class':'meta'}).text, "%A, %B %d, %Y at %I:%M%p UTC")
    message = b.find_next('p').text
    thread.append({
        'user'    : user,
        'time'    : time.strftime("%Y-%m-%d %H:%M:%S"),
        'message' : message
      })
    if user.encode('utf8') == name:
      messages_from_this_name.write(message+'\n')
  data.append(thread)

json_file = open("facebook_messages.json", "w+")
json_file.write(json.dumps(data,indent=2,ensure_ascii=False).encode('utf8'))
json_file.close()

print ':)'