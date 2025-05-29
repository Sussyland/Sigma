#importē bibliotēkas pēc pieprasījuma ar pip install
import randfacts
import pyfiglet
import cowsay
import datetime
#izveido random faktu
fakts=randfacts.get_fact()
#pārveido faktu figlet formātā pēc pieprasījuma
f=pyfiglet.figlet_format(fakts,font="tanja")
#ievade dzimšanas dienai
gads=int(input("ievadi dzimšanas gadu!"))
menesis=int(input("ievadi dzimšanas mēnesi!"))
diena=int(input("ievadi dzimšanas dienu!"))
#pārbauda šodienas datumu
sodien=(datetime.date.today())
#pārveido dzimšanas dienas ievadi par datumu
dz=(datetime.date(gads,menesis,diena))
#izrēķina cik dienas pagājušas kops dzimšanas dienas
pagajisd=(sodien-dz).days*24
#izrēķina cik minūtes pagājušas kops dzimšanas diena
pagajism=(sodien-dz).days*24*60
#izveido un atver teksta dokumentu kur izvadīs nepieciešamo
txt=open("darbs.txt","a",encoding="utf-8")
#izvada pirmā uzdevuma izvadi teksta dokumentā
txt.write(cowsay.get_output_string('trex',f))
#izvada otrā uzdevuma izvadi teksta dokumentā
txt.write(f"kopš dzimšanas dienas, pagājušas {pagajisd} dienas, vai {pagajism} minūtes!")
#nobeidz teksta rakstīšanu
txt.close