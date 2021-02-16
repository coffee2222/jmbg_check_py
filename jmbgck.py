import sys
import time
import argparse as ap
import datetime
from termcolor import colored
def main():
    try:
        jmbg = (str(sys.argv[1]))
    except:
        sys.exit("JMBG not provided!")
    if (len(jmbg) == 13):
        print(jmbg)
        print("JMBG number is correct length!")
       
        print(dob())
        print(location(str(list(jmbg)[7] + list(jmbg)[8])))
        print(mof())
        controlnumber()
      

    else:
        print("Not a valid JMBG number")


def controlnumber():
    jmbg = (str(sys.argv[1]))
    L = 11 - ((7 *( (int(list(jmbg)[0])) + (int(list(jmbg)[6])) ) + 6 * ( (int(list(jmbg)[1])) + (int(list(jmbg)[7])) ) + 5 * ( (int(list(jmbg)[2])) + (int(list(jmbg)[8])) ) + 4 * ( (int(list(jmbg)[3])) + (int(list(jmbg)[9])) )  + 3*  ( (int(list(jmbg)[4])) + (int(list(jmbg)[10])) ) + 2* ( (int(list(jmbg)[5])) + (int(list(jmbg)[11])) ) ))
    if int(list(jmbg)[12]) == (L%11):
         print(colored('JMBG control number valid!', 'green'))
         return
    elif int(list(jmbg)[12]) != (L%11):
        print(colored('JMBG control number invalid!', 'red'))
        return


def mof():
    jmbg = (str(sys.argv[1]))
    mofnum=  str(list(jmbg)[9] + list(jmbg)[10] +  list(jmbg)[11])
    if  500  <= int(mofnum) <= 999:
        return 'Female'
    elif 0 <= int(mofnum) <= 499:
        return 'Male'
def dob(): # first 7 numbers from jmbg.
    jmbg = (str(sys.argv[1]))
    date = str(list(jmbg)[0] + list(jmbg)[1])
    month = str(list(jmbg)[2] + list(jmbg)[3])
    y = str(list(jmbg)[4] + list(jmbg)[5] + list(jmbg)[6])
    if 900 <int(y) < 1000:
        year = "1" + str(list(jmbg)[4] + list(jmbg)[5] + list(jmbg)[6]) 
    elif int(y) > 0 :
        year = "2" + str(list(jmbg)[4] + list(jmbg)[5] + list(jmbg)[6])
    elif int(y) == 0:
        year = "2000"

    try:
        newDate = datetime.datetime(int(year),int(month),int(date))
import sys
import time
import argparse as ap

import datetime
from termcolor import colored
def main():
    try:
        jmbg = (str(sys.argv[1]))
    except:
        sys.exit("JMBG not provided!")
    if (len(jmbg) == 13):
        print(jmbg)
        print("JMBG number is correct length!")
       
        print(dob())
        print(location(str(list(jmbg)[7] + list(jmbg)[8])))
        print(mof())
        controlnumber()
      

    else:
        print("Not a valid JMBG number")


def controlnumber():
    jmbg = (str(sys.argv[1]))
    L = 11 - ((7 *( (int(list(jmbg)[0])) + (int(list(jmbg)[6])) ) + 6 * ( (int(list(jmbg)[1])) + (int(list(jmbg)[7])) ) + 5 * ( (int(list(jmbg)[2])) + (int(list(jmbg)[8])) ) + 4 * ( (int(list(jmbg)[3])) + (int(list(jmbg)[9])) )  + 3*  ( (int(list(jmbg)[4])) + (int(list(jmbg)[10])) ) + 2* ( (int(list(jmbg)[5])) + (int(list(jmbg)[11])) ) ))
    if int(list(jmbg)[12]) == (L%11):
         print(colored('JMBG control number valid!', 'green'))
         return
    elif int(list(jmbg)[12]) != (L%11):
        print(colored('JMBG control number invalid!', 'red'))
        return
def mof():
    jmbg = (str(sys.argv[1]))
    mofnum=  str(list(jmbg)[9] + list(jmbg)[10] +  list(jmbg)[11])
    if  500  <= int(mofnum) <= 999:
        return 'Female'
    elif 0 <= int(mofnum) <= 499:
        return 'Male'
def dob(): # first 7 numbers from jmbg.
    jmbg = (str(sys.argv[1]))
    date = str(list(jmbg)[0] + list(jmbg)[1])
    month = str(list(jmbg)[2] + list(jmbg)[3])
    y = str(list(jmbg)[4] + list(jmbg)[5] + list(jmbg)[6]) 
    CurrentDate = datetime.datetime.now()
    if 900 <int(y) < 1000:
        year = "1" + str(list(jmbg)[4] + list(jmbg)[5] + list(jmbg)[6]) 
    elif int(y) > 0 :
        year = "2" + str(list(jmbg)[4] + list(jmbg)[5] + list(jmbg)[6])
    elif int(y) == 0:
        year = "2000"
    ExpectedDate = date +"/"+month + "/" + year + " 4:00"
    try:
        newDate = datetime.datetime(int(year),int(month),int(date))
        ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y %H:%M")
        if (CurrentDate < ExpectedDate):
            raise ValueError
        return (colored("DOB:" + str(date) + "d-" + str(month) + "m-"+ str(year)+ "y" , 'cyan')) 
    except ValueError as e:
        return (colored("DOB ERROR:" + str(date) + "d-" + str(month) + "m-"+ str(year)+ "y", 'red'))
        
         
def location(val):
    return {
        '01': "Foreigner in Bosnia And Herzegovina",
        '02':"Foreigner in Montenegro",
        '03': "Foreigner in Croatia",
        '04': "Foreigner in Macedonia",
        '05': "Foreigner in Slovenia",
        '07': "Foreigner in Serbia (no domicile territory)",
        
        '08': "Foreigner in Vojvodina",
        '09': "Foreigner in Kosovo And Metohija",

        '10': "Bosnia And Herzegovina : Banja Luka",                    
        '11': "Bosnia And Herzegovina : Bihac"  ,
        '12': "Bosnia And Herzegovina : Doboj"  ,
        '13': "Bosnia And Herzegovina : Gorazde",  
        '14': "Bosnia And Herzegovina : Livno" , 
        '15': "Bosnia And Herzegovina : Mostar",
        '16': "Bosnia And Herzegovina : Prijedor",
        '17': "Bosnia And Herzegovina : Sarajevo",
        '18':"Bosnia And Herzegovina : Tuzla",
        '19': "Bosnia And Herzegovina : Zenica",

        '21': "Montenegro : Podgorica",    
        '26': "Montenegro : Niksic",    
        '29': "Montenegro : Pljevlja",    
 
        '30': "Croatia : Osijek, Slavonia region",
        '31': "Croatia : Bjelovar, Virovitica, Koprivnica, Pakrac, Podravina region ",
        '32': "Croatia : Varazdin, Medjimurje region",
        '33': "Croatia : Zagreb",
        '34': "Croatia : Karlovac ",
        '35': "Croatia : Gospic, Lika region",
        '36': "Croatia : Rijeka, Pula, Istra i Primorje region",
        '37': "Croatia : Sisak, Banovina region",
        '38':"Croatia :Split, Zadar, Dubrovnik, Dalmacia region",
        '39':"Croatia : other",

        '41': "Macedonia : Bitolj",
        '42': "Macedonia : Kumanovo",
        '43':  "Macedonia : Ohrid",
        '44':  "Macedonia : Prilep",
        '45':  "Macedonia : Skoplje",
        '46': "Macedonia : Strumica",
        '47':  "Macedonia : Tetovo",
        '48':  "Macedonia : Veles",
        '49': "Macedonia : Stip",
        '50' or '51' or '52' or '53' or '54' or '55' or '56' or '57' or '58' or '59' : "Slovenia ",
        '60' or '61' or '62' or '63' or '64' or '65' or '66' or '67' or '68' or '69' : "Not used!",
        '70' : "Serbia : Central Serbia" ,
        '71':"Serbia : Central Serbia : Beograd region ",
        '72': "Serbia : Central Serbia : Sumadija",
        '73': "Serbia : Central Serbia : Nis",
        '74': "Serbia : Central Serbia : Juzna Morava",
        '75':"Serbia : Central Serbia : Zajecar",
        '76': "Serbia : Central Serbia : Podunavlje",
        '77': "Serbia : Central Serbia : Podrinje i Kolubara",
        '78': "Serbia : Central Serbia : Kraljevo",
        '79': "Serbia : Central Serbia : Uzice ",
        '80': "Serbia : Autonomous Province of Vojvodina : Novi Sad ",
        '81': "Serbia : Autonomous Province of Vojvodina : Sombor",
        '82': "Serbia : Autonomous Province of Vojvodina : Subotica",
        '84' or '83': "Serbia : Autonomous Province of Vojvodina",
        '85': "Serbia : Autonomous Province of Vojvodina : Zrenjanin",
        '86': "Serbia : Autonomous Province of Vojvodina : Pancevo",
        '87': "Serbia : Autonomous Province of Vojvodina : Kikinda",
        '88': "Serbia : Autonomous Province of Vojvodina : Ruma",
        '89': "Serbia : Autonomous Province of Vojvodina : Sremska Mitrovica",
        
        '91': "Serbia : Autonomous Province of Kosovo and Metohija  : Pristina",
        '92': "Serbia : Autonomous Province of Kosovo and Metohija  : Kosovska Mitrovica",
        '93': "Serbia : Autonomous Province of Kosovo and Metohija  : Pec",
        '94': "Serbia : Autonomous Province of Kosovo and Metohija  : Djakovica",
        '95': "Serbia : Autonomous Province of Kosovo and Metohija  : Prizren",
        '96': "Serbia : Autonomous Province of Kosovo and Metohija  : Kosovo Pomoravski District",
        '97' or '98' or '99': "Serbia : Autonomous Province of Kosovo and Metohija",
    }.get(val, 'Not used!') 

if __name__ == "__main__":
    print('Developed by (offe^4')
    print('version 0.0.1')
    print(colored(":----------:::::://////::::////:::::::-----------:", 'white',))
    print(colored(":.-.-:..------:--:///::::/:-://///////:::/::-----:", 'white',))
    print(colored(":.-.---.------....//////-///://-::::::/+++:---..-:", 'white',))
    print(colored(":...`........```.::::----............-/+/:------.:", 'white',))
    print(colored(":.`  `-/o+/-`  `./+//-.............-//::-----..--:", 'white',))
    print(colored(":.`  /hydhyho` `.////::::........-//:--++++++-...:", 'white',))
    print(colored(":.` `so///+hd. `.+///+///-----...-:--..////+/----:", 'white',))
    print(colored(":.`  /so//o+s. `./+://:///+-...........://///--:-:", 'white',))
    print(colored(":.   .+++/:/-` `.//-:-----///::/::::--...--------:", 'white',))
    print(colored(":.  `.+oo+//:.``.+/--::::::////::::::---.-//.---.:", 'white',))
    print(colored(":`..-:oo+///o::-.+/:///++/+-..-..--.----.-//.....:", 'white',))
    print(colored(":...--+/::::+--:.//://////-..........---.:::-....:", 'white',))
    print(colored(":..------:-------/:-:::/::/.........------.......:", 'white',))
    print(colored(":.:++:++/+/+o/+++/////-----......----://::-/::...:", 'white',))
    print(colored(":----------::--:::::::-------::------------------:", 'white',))
    print(colored('Jedinstveni matični broj građana', 'white', 'on_blue'))
    print(colored('exYu ID number check', 'red', 'on_white'))
    print(colored('_____________________________________________________________________________________________________________________','red'))
    print('Keep in mind: This tools just check the data based on set of rules. It does not communicate to any external database!')
    print(colored('_____________________________________________________________________________________________________________________','red'))
    time.sleep(2)
    print()
    print()
    print()
    main()
    print(colored('_____________________________________________________________________________________________________________________','red'))




        '73': "Serbia : Central Serbia : Nis",
        '74': "Serbia : Central Serbia : Juzna Morava",
        '75':"Serbia : Central Serbia : Zajecar",
        '76': "Serbia : Central Serbia : Podunavlje",
        '77': "Serbia : Central Serbia : Podrinje i Kolubara",
        '78': "Serbia : Central Serbia : Kraljevo",
        '79': "Serbia : Central Serbia : Uzice ",
        '80': "Serbia : Autonomous Province of Vojvodina : Novi Sad ",
        '81': "Serbia : Autonomous Province of Vojvodina : Sombor",
        '82': "Serbia : Autonomous Province of Vojvodina : Subotica",
        '84' or '83': "Serbia : Autonomous Province of Vojvodina",
        '85': "Serbia : Autonomous Province of Vojvodina : Zrenjanin",
        '86': "Serbia : Autonomous Province of Vojvodina : Pancevo",
        '87': "Serbia : Autonomous Province of Vojvodina : Kikinda",
        '88': "Serbia : Autonomous Province of Vojvodina : Ruma",
        '89': "Serbia : Autonomous Province of Vojvodina : Sremska Mitrovica",
        
        '91': "Serbia : Autonomous Province of Kosovo and Metohija  : Pristina",
        '92': "Serbia : Autonomous Province of Kosovo and Metohija  : Kosovska Mitrovica",
        '93': "Serbia : Autonomous Province of Kosovo and Metohija  : Pec",
        '94': "Serbia : Autonomous Province of Kosovo and Metohija  : Djakovica",
        '95': "Serbia : Autonomous Province of Kosovo and Metohija  : Prizren",
        '96': "Serbia : Autonomous Province of Kosovo and Metohija  : Kosovo Pomoravski District",
        '97' or '98' or '99': "Serbia : Autonomous Province of Kosovo and Metohija",
    }.get(val, 'Not used!') 

if __name__ == "__main__":
    
    print('Developed by (offe^4')
    print('version 0.0.1')
    print(colored(":----------:::::://////::::////:::::::-----------:", 'white',))
    print(colored(":.-.-:..------:--:///::::/:-://///////:::/::-----:", 'white',))
    print(colored(":.-.---.------....//////-///://-::::::/+++:---..-:", 'white',))
    print(colored(":...`........```.::::----............-/+/:------.:", 'white',))
    print(colored(":.`  `-/o+/-`  `./+//-.............-//::-----..--:", 'white',))
    print(colored(":.`  /hydhyho` `.////::::........-//:--++++++-...:", 'white',))
    print(colored(":.` `so///+hd. `.+///+///-----...-:--..////+/----:", 'white',))
    print(colored(":.`  /so//o+s. `./+://:///+-...........://///--:-:", 'white',))
    print(colored(":.   .+++/:/-` `.//-:-----///::/::::--...--------:", 'white',))
    print(colored(":.  `.+oo+//:.``.+/--::::::////::::::---.-//.---.:", 'white',))
    print(colored(":`..-:oo+///o::-.+/:///++/+-..-..--.----.-//.....:", 'white',))
    print(colored(":...--+/::::+--:.//://////-..........---.:::-....:", 'white',))
    print(colored(":..------:-------/:-:::/::/.........------.......:", 'white',))
    print(colored(":.:++:++/+/+o/+++/////-----......----://::-/::...:", 'white',))
    print(colored(":----------::--:::::::-------::------------------:", 'white',))
    print(colored('Jedinstveni matični broj građana', 'white', 'on_blue'))
    print(colored('exYu ID number check', 'red', 'on_white'))
    print(colored('_____________________________________________________________________________________________________________________','red'))
    print('Keep in mind: This tools just check the data based on set of rules. It does not communicate to any external database!')
    print(colored('_____________________________________________________________________________________________________________________','red'))
    time.sleep(2)
    print()
    print()
    print()
    main()
    print(colored('_____________________________________________________________________________________________________________________','red'))



