import requests, smtplib
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/cryptocurrencies"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)'}
r = requests.get(url, headers=headers)
r.raise_for_status()
src = r.content
soup = BeautifulSoup(src, "html.parser")
coin_list = {}
for tr_tag in soup.find_all('tr'):
    try:
        td_tag_name = tr_tag.find_all('td', {"aria-label": "Name"})
        td_tag_change = tr_tag.find_all('td', {"aria-label": "% Change"})
        name = td_tag_name[0].get_text()
        name = name.replace(" USD", "")
        change = td_tag_change[0].get_text()
        change = change.replace("+", "")
        change = change.replace("%", "")
        change_float = float(change)
        coin_list[name] = change_float
    except Exception as E: 
        pass
volatile_coin = {}
threshhold = 5
for k in coin_list:
    if abs(coin_list[k]) > threshhold:
        volatile_coin.update({k:coin_list[k]})

message = "Here is today's list of volatile cryptocurrency, by % change \n"
for k in volatile_coin:
    message = message + k + " " + str(coin_list[k]) + "\n"


user = "colingraydon@gmail.com"
pass = secret_key
s = smtplib.SMTP_SSL('smtp.mail.com',465)
s.login(user, pass)
s.sendmail(user, user, message)
s.quit()








    
    




