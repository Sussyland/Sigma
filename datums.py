
#vajag ielāded num2words bibliotēku lai pārveidotu skaitļus vārdos, kā arī datetime bibliotēku lai lietotu laika funkcijas
#pip install datetime
#pip install num2words

from datetime import date
from num2words import num2words

class Persona:
    def __init__(self, dzimsanas_datums_str):
        #Inicializē objektu ar lietotāja dzimšanas datumu
        self.dzimsanas_datums=date.fromisoformat(dzimsanas_datums_str)

    def aprekinat_minutes(self):
        #Pārbauda šodienas datumu
        sodienas_datums=date.today()
        #Aprēķina minūšu skaitu no dzimšanas datuma līdz šodienai
        dienas_pagajusas=(sodienas_datums-self.dzimsanas_datums).days
        return dienas_pagajusas * 24 * 60

    def izvadit_rezultatu(self):
        #Izvada minūšu skaitu vārdos
        minutes=self.aprekinat_minutes()
       #pārveido skaitļus vārdos.
        minutes_vardos=num2words(minutes, lang='en').capitalize()
        print(f"{minutes_vardos} minutes")

# Pieprasām lietotāja dzimšanas datumu
dzimsanas_datums_str=input("Ievadi dzimšanas dienu (YYYY-MM-DD): ")

# Izvade
persona=Persona(dzimsanas_datums_str)
persona.izvadit_rezultatu()

        
