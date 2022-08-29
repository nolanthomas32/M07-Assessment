import json
from dataclasses import dataclass, field
from datetime import datetime, date
import requests
from bs4 import BeautifulSoup

@dataclass
class Holiday:
    name: str
    date: datetime.date
    def __str__(self):
        return f"{self.name} takes place on {self.date}"


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if Holiday.is_dataclass(o):
            return Holiday.asdict(o)
        return super().default(o)

#define global variables
running = True
active = True
name = True
roster = {}
def hol_start():
    print('\nWelcome to the Holiday Tracker.')

def get_weather():
    response = requests.get("https://api.weather.gov/gridpoints/MKX/87,64/forecast")
    weather_json = response.json()
    test = weather_json['properties']
    weather_info = test['periods']
    print(weather_info[0])
    print(weather_info[1])
    print(weather_info[2])
    print(weather_info[3])
    print(weather_info[4])
    print(weather_info[5])
    print(weather_info[6])

def get_2020_holidays():
    response = requests.get('https://www.timeanddate.com/holidays/us/2020?hol=33554809')
    html = response.text
    parsed_html = BeautifulSoup(html, "html.parser")

    table = parsed_html.find('table', attrs= {"id":"holidays-table"})
    body = table.find('tbody')
    tr = body.find_all('tr', attrs={"class":"showrow"})

    th_all = body.find_all("tr", attrs={"class":"showrow"})

    holidays = []
    for holiday in tr:
        holiday_object = Holiday(name = holiday.text[6:], date = holiday.text[:6])
        holidays.append(holiday_object)

def get_2021_holidays():
    response = requests.get('https://www.timeanddate.com/holidays/us/2021?hol=33554809')
    html = response.text
    parsed_html = BeautifulSoup(html, "html.parser")

    table = parsed_html.find('table', attrs= {"id":"holidays-table"})
    body = table.find('tbody')
    tr = body.find_all('tr', attrs={"class":"showrow"})

    th_all = body.find_all("tr", attrs={"class":"showrow"})

    holidays = []
    for holiday in tr:
        holiday_object = Holiday(name = holiday.text[6:], date = holiday.text[:6])
        holidays.append(holiday_object)

def get_2022_holidays():
    response = requests.get('https://www.timeanddate.com/holidays/us/2022?hol=33554809')
    html = response.text
    parsed_html = BeautifulSoup(html, "html.parser")

    table = parsed_html.find('table', attrs= {"id":"holidays-table"})
    body = table.find('tbody')
    tr = body.find_all('tr', attrs={"class":"showrow"})

    th_all = body.find_all("tr", attrs={"class":"showrow"})

    holidays = []
    for holiday in tr:
        holiday_object = Holiday(name = holiday.text[6:], date = holiday.text[:6])
        holidays.append(holiday_object)
        
def get_2023_holidays():
    response = requests.get('https://www.timeanddate.com/holidays/us/2023?hol=33554809')
    html = response.text
    parsed_html = BeautifulSoup(html, "html.parser")

    table = parsed_html.find('table', attrs= {"id":"holidays-table"})
    body = table.find('tbody')
    tr = body.find_all('tr', attrs={"class":"showrow"})

    th_all = body.find_all("tr", attrs={"class":"showrow"})

    holidays = []
    for holiday in tr:
        holiday_object = Holiday(name = holiday.text[6:], date = holiday.text[:6])
        holidays.append(holiday_object)

def get_2024_holidays():
    response = requests.get('https://www.timeanddate.com/holidays/us/2024?hol=33554809')
    html = response.text
    parsed_html = BeautifulSoup(html, "html.parser")

    table = parsed_html.find('table', attrs= {"id":"holidays-table"})
    body = table.find('tbody')
    tr = body.find_all('tr', attrs={"class":"showrow"})

    th_all = body.find_all("tr", attrs={"class":"showrow"})

    holidays = []
    for holiday in tr:
        holiday_object = Holiday(name = holiday.text[6:], date = holiday.text[:6])
        holidays.append(holiday_object)
    
def display_main_menu():
    print(f'\nView your menu options below.\n')
    print('Holiday Menu')
    print('================')
    print('1. Add a Holiday')
    print('2. Remove a Holiday')
    print('3. View Holidays')
    print('4. Save Changes')
    print('5. Exit')

def add_holiday_1():
        print('Welcome to the Holiday addition screen!')
        while active:
            holidays = []
            hol_name = input("Enter the Holiday name here: ")
            hol_date = input('Enter Holiday date here in the form of YYYY-MM-DD: ')
            
            # Holiday(name = hol_name, date= hol_date)
            holiday_object = Holiday(name = hol_name, date = hol_date)
            holidays.append(holiday_object)
            print(f'{holidays} has been added!')
            cont = input('Would you like to add another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break
        return holidays

def remove_holiday_2():
    while active:
        hol_year = int(input('Select year to remove Holiday from: '))
        if hol_year != 2020 and hol_year != 2021 and hol_year != 2022 and hol_year != 2023 and hol_year != 2024:
            print('Please select a valid year')
        if hol_year == 2020:
            with open('M07-Assessment\\holiday_2020.json') as json_file:
                data = json.load(json_file)
                hol_name = input('Type the name of the holiday to remove: ')
                if data.values() == hol_name:
                    data.pop(hol_name)
                    print(f'{hol_name} has been removed!')
                else:
                    print('That name did not work. Please try again')   
            cont = input('Would you like to remove another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break

        if hol_year == 2021:
            with open('M07-Assessment\\holiday_2021.json') as json_file:
                data = json.load(json_file)
                hol_name = input('Type the name of the holiday to remove: ')
                if data.values() == hol_name:
                    data.pop(hol_name)
                    print(f'{hol_name} has been removed!')
                else:
                    print('That name did not work. Please try again')   
            cont = input('Would you like to remove another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break

        if hol_year == 2022:
            with open('M07-Assessment\\holiday_2022.json') as json_file:
                data = json.load(json_file)
                hol_name = input('Type the name of the holiday to remove: ')
                if data.values() == hol_name:
                    data.pop(hol_name)
                    print(f'{hol_name} has been removed!')
                else:
                    print('That name did not work. Please try again')   
            cont = input('Would you like to remove another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break   

        if hol_year == 2023:
            with open('M07-Assessment\\holiday_2023.json') as json_file:
                data = json.load(json_file)
                hol_name = input('Type the name of the holiday to remove: ')
                if data.values() == hol_name:
                    data.pop(hol_name)
                    print(f'{hol_name} has been removed!')
                else:
                    print('That name did not work. Please try again')   
            cont = input('Would you like to remove another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break   

        if hol_year == 2024:
            with open('M07-Assessment\\holiday_2024.json') as json_file:
                data = json.load(json_file)
                hol_name = input('Type the name of the holiday to remove: ')
                if data.values() == hol_name:
                    data.pop(hol_name)
                    print(f'{hol_name} has been removed!')
                else:
                    print('That name did not work. Please try again')   
            cont = input('Would you like to remove another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break               




def view_holiday_3():
    print('View Holidays')
    while active:
        view_year = int(input('Select a year to view from 2020-2024: '))
        if (view_year !=2020 and view_year != 2021 and view_year != 2022 and view_year != 2023 and view_year != 2024):
            print('Please select a valid year.')
        if view_year == 2020:
            with open('M07-Assessment\\holidays_2020.json') as json_file:
                data = json.load(json_file)
            holidays = []
            for i in data['holidays_2020']:
                holiday_object = Holiday(name = i['name'], date = i['date'])
                holidays.append(holiday_object)
            week_select = int(input('Select the week you would like to view(1-53): '))
            if week_select == 1:
                list((lambda holidays: print(holidays[0]), Holiday))
                print(holidays[0])
            if week_select == 2:
                list((lambda holidays: print('NONE'), Holiday))
                print('NONE')
            if week_select == 3:
                list((lambda holidays: print(holidays[1]), Holiday))
                print(holidays[1])
            if week_select == 4:
                list((lambda holidays: print(holidays[2:4]), Holiday))
                print(holidays[2:4])
            if week_select == 5:
                list((lambda holidays: print(holidays[4:7]), Holiday))
                print(holidays[4:7])
            if week_select == 6:
                list((lambda holidays: print(holidays[7:11]), Holiday))
                print(holidays[7:11])
            if week_select == 7:
                list((lambda holidays: print(holidays[11]), Holiday))
                print(holidays[11])
            if week_select == 8:
                list((lambda holidays: print(holidays[12]), Holiday))
                print(holidays[12])
            if week_select == 9:
                list((lambda holidays: print(holidays[13]), Holiday))
                print(holidays[13])
            if week_select == 10:
                list((lambda holidays: print(holidays[14:20]), Holiday))
                print(holidays[14:20])
            if week_select == 11:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')  
            if week_select == 12:
                list((lambda holidays: print(holidays[20:22]), Holiday))
                print(holidays[20:22]) 
            if week_select == 13:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 14:
                list((lambda holidays: print(holidays[22:24]), Holiday))
                print(holidays[22:24]) 
            if week_select == 15:
                list((lambda holidays: print(holidays[24:26]), Holiday))
                print(holidays[24:26]) 
            if week_select == 16:
                list((lambda holidays: print(holidays[26:29]), Holiday))
                print(holidays[26:29])
            if week_select == 17:
                list((lambda holidays: print(holidays[29:32]), Holiday))
                print(holidays[29:32]) 
            if week_select == 18:
                list((lambda holidays: print(holidays[32:39]), Holiday))
                print(holidays[32:39]) 
            if week_select == 19:
                list((lambda holidays: print(holidays[39:45]), Holiday))
                print(holidays[39:45]) 
            if week_select == 20:
                list((lambda holidays: print(holidays[45:50]), Holiday))
                print(holidays[45:50]) 
            if week_select == 21:
                list((lambda holidays: print(holidays[50:52]), Holiday))
                print(holidays[50:52]) 
            if week_select == 22:
                list((lambda holidays: print(holidays[52:54]), Holiday))
                print(holidays[52:54]) 
            if week_select == 23:
                list((lambda holidays: print(holidays[52:58]), Holiday))
                print(holidays[52:58]) 
            if week_select == 24:
                list((lambda holidays: print(holidays[58]), Holiday))
                print(holidays[58]) 
            if week_select == 25:
                list((lambda holidays: print(holidays[59:65]), Holiday))
                print(holidays[59:65]) 
            if week_select == 26:
                list((lambda holidays: print(holidays[65]), Holiday))
                print(holidays[65]) 
            if week_select == 27:
                list((lambda holidays: print(holidays[66:68]), Holiday))
                print(holidays[66:68]) 
            if week_select == 28:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 29:
                list((lambda holidays: print(holidays[68:71]), Holiday))
                print(holidays[68:71]) 
            if week_select == 30:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 31:
                list((lambda holidays: print(holidays[71:73]), Holiday))
                print(holidays[71:73]) 
            if week_select == 32:
                list((lambda holidays: print(holidays[73:76]), Holiday))
                print(holidays[73:76]) 
            if week_select == 33:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 34:
                list((lambda holidays: print(holidays[76:78]), Holiday))
                print(holidays[76:78]) 
            if week_select == 35:
                list((lambda holidays: print(holidays[78]), Holiday))
                print(holidays[78]) 
            if week_select == 36:
                list((lambda holidays: print(holidays[79]), Holiday))
                print(holidays[79]) 
            if week_select == 37:
                list((lambda holidays: print(holidays[80:84]), Holiday))
                print(holidays[80:84]) 
            if week_select == 38:
                list((lambda holidays: print(holidays[84:90]), Holiday))
                print(holidays[84:90]) 
            if week_select == 39:
                list((lambda holidays: print(holidays[90:92]), Holiday))
                print(holidays[90:92]) 
            if week_select == 40:
                list((lambda holidays: print(holidays[92]), Holiday))
                print(holidays[92]) 
            if week_select == 41:
                list((lambda holidays: print(holidays[93:96]), Holiday))
                print(holidays[93:96]) 
            if week_select == 42:
                list((lambda holidays: print(holidays[96:101]), Holiday))
                print(holidays[96:101]) 
            if week_select == 43:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 44:
                list((lambda holidays: print(holidays[101]), Holiday))
                print(holidays[101]) 
            if week_select == 45:
                list((lambda holidays: print(holidays[102:104]), Holiday))
                print(holidays[102:104]) 
            if week_select == 46:
                list((lambda holidays: print(holidays[104:106]), Holiday))
                print(holidays[104:106]) 
            if week_select == 47:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 48:
                list((lambda holidays: print(holidays[106:109]), Holiday))
                print(holidays[106:109]) 
            if week_select == 49:
                list((lambda holidays: print(holidays[109:111]), Holiday))
                print(holidays[109:111]) 
            if week_select == 50:
                list((lambda holidays: print(holidays[111:113]), Holiday))
                print(holidays[111:113]) 
            if week_select == 51:
                list((lambda holidays: print(holidays[113:117]), Holiday))
                print(holidays[113:117]) 
            if week_select == 52:
                list((lambda holidays: print(holidays[117:121]), Holiday))
                print(holidays[117:121]) 
            if week_select == 53:
                list((lambda holidays: print(holidays[121:len(holidays)]), Holiday))
                print(holidays[121:len(holidays)])             
            # else:
            #     print("Please select a valid number.")

        if view_year == 2021:
            with open('M07-Assessment\\holidays_2021.json') as json_file:
                data = json.load(json_file)
            holidays = []
            for i in data['holidays_2021']:
                holiday_object = Holiday(name = i['name'], date = i['date'])
                holidays.append(holiday_object)
            week_select = int(input('Select the week you would like to view(1-53): '))
            if week_select == 1:
                list((lambda holidays: print(holidays[0]), Holiday))
                print(holidays[0])
            if week_select == 2:
                list((lambda holidays: print('NONE'), Holiday))
                print('NONE')
            if week_select == 3:
                list((lambda holidays: print(holidays[1:9]), Holiday))
                print(holidays[1:9])
            if week_select == 4:
                list((lambda holidays: print(holidays[9:11]), Holiday))
                print(holidays[9:11])
            if week_select == 5:
                list((lambda holidays: print(holidays[11]), Holiday))
                print(holidays[11])
            if week_select == 6:
                list((lambda holidays: print(holidays[12:17]), Holiday))
                print(holidays[12:17])
            if week_select == 7:
                list((lambda holidays: print(holidays[17:19]), Holiday))
                print(holidays[17:19])
            if week_select == 8:
                list((lambda holidays: print(holidays[19:22]), Holiday))
                print(holidays[19:22])
            if week_select == 9:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 10:
                list((lambda holidays: print(holidays[22:27]), Holiday))
                print(holidays[22:27])
            if week_select == 11:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')  
            if week_select == 12:
                list((lambda holidays: print(holidays[27:29]), Holiday))
                print(holidays[27:29]) 
            if week_select == 13:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 14:
                list((lambda holidays: print(holidays[29:31]), Holiday))
                print(holidays[29:31]) 
            if week_select == 15:
                list((lambda holidays: print(holidays[31:35]), Holiday))
                print(holidays[31:35]) 
            if week_select == 16:
                list((lambda holidays: print(holidays[35]), Holiday))
                print(holidays[35])
            if week_select == 17:
                list((lambda holidays: print(holidays[36:38]), Holiday))
                print(holidays[36:38]) 
            if week_select == 18:
                list((lambda holidays: print(holidays[38:46]), Holiday))
                print(holidays[38:46]) 
            if week_select == 19:
                list((lambda holidays: print(holidays[46:51]), Holiday))
                print(holidays[46:51]) 
            if week_select == 20:
                list((lambda holidays: print(holidays[51:54]), Holiday))
                print(holidays[51:54]) 
            if week_select == 21:
                list((lambda holidays: print(holidays[54:58]), Holiday))
                print(holidays[54:58]) 
            if week_select == 22:
                list((lambda holidays: print(holidays[58]), Holiday))
                print(holidays[58]) 
            if week_select == 23:
                list((lambda holidays: print(holidays[59:63]), Holiday))
                print(holidays[59:63]) 
            if week_select == 24:
                list((lambda holidays: print(holidays[63:65]), Holiday))
                print(holidays[63:65]) 
            if week_select == 25:
                list((lambda holidays: print(holidays[65:70]), Holiday))
                print(holidays[65:70]) 
            if week_select == 26:
                list((lambda holidays: print(holidays[70:72]), Holiday))
                print(holidays[70:72]) 
            if week_select == 27:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 28:
                list((lambda holidays: print(holidays[72:74]), Holiday))
                print(holidays[72:74]) 
            if week_select == 29:
                list((lambda holidays: print(holidays[74:76]), Holiday))
                print(holidays[74:76]) 
            if week_select == 30:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 31:
                list((lambda holidays: print(holidays[76:78]), Holiday))
                print(holidays[76:78]) 
            if week_select == 32:
                list((lambda holidays: print(holidays[78:81]), Holiday))
                print(holidays[78:81]) 
            if week_select == 33:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 34:
                list((lambda holidays: print(holidays[81:83]), Holiday))
                print(holidays[81:83]) 
            if week_select == 35:
                list((lambda holidays: print(holidays[83]), Holiday))
                print(holidays[83]) 
            if week_select == 36:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 37:
                list((lambda holidays: print(holidays[84:88]), Holiday))
                print(holidays[84:88]) 
            if week_select == 38:
                list((lambda holidays: print(holidays[88:94]), Holiday))
                print(holidays[88:94]) 
            if week_select == 39:
                list((lambda holidays: print(holidays[94:96]), Holiday))
                print(holidays[94:96]) 
            if week_select == 40:
                list((lambda holidays: print(holidays[96]), Holiday))
                print(holidays[96]) 
            if week_select == 41:
                list((lambda holidays: print(holidays[97:100]), Holiday))
                print(holidays[97:100]) 
            if week_select == 42:
                list((lambda holidays: print(holidays[100:107]), Holiday))
                print(holidays[100:107]) 
            if week_select == 43:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 44:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 45:
                list((lambda holidays: print(holidays[107:110]), Holiday))
                print(holidays[107:110]) 
            if week_select == 46:
                list((lambda holidays: print(holidays[110:113]), Holiday))
                print(holidays[110:113]) 
            if week_select == 47:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 48:
                list((lambda holidays: print(holidays[113:116]), Holiday))
                print(holidays[113:116]) 
            if week_select == 49:
                list((lambda holidays: print(holidays[116:118]), Holiday))
                print(holidays[116:118]) 
            if week_select == 50:
                list((lambda holidays: print(holidays[118:120]), Holiday))
                print(holidays[118:120]) 
            if week_select == 51:
                list((lambda holidays: print(holidays[120:124]), Holiday))
                print(holidays[120:124]) 
            if week_select == 52:
                list((lambda holidays: print(holidays[124:127]), Holiday))
                print(holidays[124:127]) 
            if week_select == 53:
                list((lambda holidays: print(holidays[127:len(holidays)]), Holiday))
                print(holidays[127:len(holidays)])             
            # else:
            #     print("Please select a valid number.")

        if view_year == 2022:
            with open('M07-Assessment\\holidays_2022.json') as json_file:
                data = json.load(json_file)
            holidays = []
            for i in data['holidays_2022']:
                holiday_object = Holiday(name = i['name'], date = i['date'])
                holidays.append(holiday_object)
            week_select = int(input('Select the week you would like to view(1-53) (the current week is 36): '))
            if week_select == 1:
                list((lambda holidays: print(holidays[0]), Holiday))
                print(holidays[0])
            if week_select == 2:
                list((lambda holidays: print('NONE'), Holiday))
                print('NONE')
            if week_select == 3:
                list((lambda holidays: print(holidays[1]), Holiday))
                print(holidays[1])
            if week_select == 4:
                list((lambda holidays: print(holidays[2:4]), Holiday))
                print(holidays[2:4])
            if week_select == 5:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 6:
                list((lambda holidays: print(holidays[4:9]), Holiday))
                print(holidays[4:9])
            if week_select == 7:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 8:
                list((lambda holidays: print(holidays[9:11]), Holiday))
                print(holidays[9:11])
            if week_select == 9:
                list((lambda holidays: print(holidays[11]), Holiday))
                print(holidays[11])
            if week_select == 10:
                list((lambda holidays: print(holidays[12:18]), Holiday))
                print(holidays[12:18])
            if week_select == 11:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')  
            if week_select == 12:
                list((lambda holidays: print(holidays[18]), Holiday))
                print(holidays[18]) 
            if week_select == 13:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 14:
                list((lambda holidays: print(holidays[19:21]), Holiday))
                print(holidays[19:21]) 
            if week_select == 15:
                list((lambda holidays: print(holidays[21]), Holiday))
                print(holidays[21]) 
            if week_select == 16:
                list((lambda holidays: print(holidays[22:24]), Holiday))
                print(holidays[22:24])
            if week_select == 17:
                list((lambda holidays: print(holidays[24:29]), Holiday))
                print(holidays[24:29]) 
            if week_select == 18:
                list((lambda holidays: print(holidays[29:31]), Holiday))
                print(holidays[29:31]) 
            if week_select == 19:
                list((lambda holidays: print(holidays[31:43]), Holiday))
                print(holidays[31:43]) 
            if week_select == 20:
                list((lambda holidays: print(holidays[43:45]), Holiday))
                print(holidays[43:45]) 
            if week_select == 21:
                list((lambda holidays: print(holidays[45:48]), Holiday))
                print(holidays[45:48]) 
            if week_select == 22:
                list((lambda holidays: print(holidays[48:51]), Holiday))
                print(holidays[48:51]) 
            if week_select == 23:
                list((lambda holidays: print(holidays[51:53]), Holiday))
                print(holidays[51:53]) 
            if week_select == 24:
                list((lambda holidays: print(holidays[53:55]), Holiday))
                print(holidays[53:55]) 
            if week_select == 25:
                list((lambda holidays: print(holidays[55:58]), Holiday))
                print(holidays[55:58]) 
            if week_select == 26:
                list((lambda holidays: print(holidays[58:64]), Holiday))
                print(holidays[58:64]) 
            if week_select == 27:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 28:
                list((lambda holidays: print(holidays[64]), Holiday))
                print(holidays[64]) 
            if week_select == 29:
                list((lambda holidays: print(holidays[65:67]), Holiday))
                print(holidays[65:67]) 
            if week_select == 30:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 31:
                list((lambda holidays: print(holidays[67:69]), Holiday))
                print(holidays[67:69]) 
            if week_select == 32:
                list((lambda holidays: print(holidays[69:71]), Holiday))
                print(holidays[69:71]) 
            if week_select == 33:
                list((lambda holidays: print(holidays[71]), Holiday))
                print(holidays[71]) 
            if week_select == 34:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 35:
                list((lambda holidays: print(holidays[72:74]), Holiday))
                print(holidays[72:74]) 
            if week_select == 36: #CURRENT WEEK
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
                weather = input('Would you like to see the weather for this week? (y/n) ')
                if weather != 'y' and weather != 'n':
                    print('Option not recognized. Expecting a y or n')
                if weather == 'y':
                    get_weather()
                else:
                    break
            if week_select == 37:
                list((lambda holidays: print(holidays[74]), Holiday))
                print(holidays[74]) 
            if week_select == 38:
                list((lambda holidays: print(holidays[75:83]), Holiday))
                print(holidays[75:83]) 
            if week_select == 39:
                list((lambda holidays: print(holidays[83:86]), Holiday))
                print(holidays[83:86]) 
            if week_select == 40:
                list((lambda holidays: print(holidays[86]), Holiday))
                print(holidays[86]) 
            if week_select == 41:
                list((lambda holidays: print(holidays[87:89]), Holiday))
                print(holidays[87:89]) 
            if week_select == 42:
                list((lambda holidays: print(holidays[89:95]), Holiday))
                print(holidays[89:95]) 
            if week_select == 43:
                list((lambda holidays: print(holidays[95]), Holiday))
                print(holidays[95]) 
            if week_select == 44:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 45:
                list((lambda holidays: print(holidays[96:98]), Holiday))
                print(holidays[96:98]) 
            if week_select == 46:
                list((lambda holidays: print(holidays[98:102]), Holiday))
                print(holidays[98:102]) 
            if week_select == 47:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 48:
                list((lambda holidays: print(holidays[102:105]), Holiday))
                print(holidays[102:105]) 
            if week_select == 49:
                list((lambda holidays: print(holidays[105:107]), Holiday))
                print(holidays[105:107]) 
            if week_select == 50:
                list((lambda holidays: print(holidays[107:109]), Holiday))
                print(holidays[107:109]) 
            if week_select == 51:
                list((lambda holidays: print(holidays[109:112]), Holiday))
                print(holidays[109:112]) 
            if week_select == 52:
                list((lambda holidays: print(holidays[112:114]), Holiday))
                print(holidays[112:114]) 
            if week_select == 53:
                list((lambda holidays: print(holidays[114:len(holidays)]), Holiday))
                print(holidays[114:len(holidays)])             
            # else:
            #     print("Please select a valid number.")

        if view_year == 2023:
            with open('M07-Assessment\\holidays_2023.json') as json_file:
                data = json.load(json_file)
            holidays = []
            for i in data['holidays_2023']:
                holiday_object = Holiday(name = i['name'], date = i['date'])
                holidays.append(holiday_object)
            week_select = int(input('Select the week you would like to view(1-53): '))
            if week_select == 1:
                list((lambda holidays: print(holidays[0:2]), Holiday))
                print(holidays[0:2])
            if week_select == 2:
                list((lambda holidays: print(holidays[2]), Holiday))
                print(holidays[2])
            if week_select == 3:
                list((lambda holidays: print(holidays[3]), Holiday))
                print(holidays[3])
            if week_select == 4:
                list((lambda holidays: print(holidays[4]), Holiday))
                print(holidays[4])
            if week_select == 5:
                list((lambda holidays: print(holidays[5:11]), Holiday))
                print(holidays[5:11])
            if week_select == 6:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 7:
                list((lambda holidays: print(holidays[11:13]), Holiday))
                print(holidays[11:13])
            if week_select == 8:
                list((lambda holidays: print(holidays[13:15]), Holiday))
                print(holidays[13:15])
            if week_select == 9:
                list((lambda holidays: print(holidays[15:20]), Holiday))
                print(holidays[15:20])
            if week_select == 10:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 11:
                list((lambda holidays: print(holidays[20]), Holiday))
                print(holidays[20])  
            if week_select == 12:
                list((lambda holidays: print(holidays[21]), Holiday))
                print(holidays[21]) 
            if week_select == 13:
                list((lambda holidays: print(holidays[22:24]), Holiday))
                print(holidays[22:24]) 
            if week_select == 14:
                list((lambda holidays: print(holidays[24]), Holiday))
                print(holidays[24]) 
            if week_select == 15:
                list((lambda holidays: print(holidays[25:28]), Holiday))
                print(holidays[25:28]) 
            if week_select == 16:
                list((lambda holidays: print(holidays[28:30]), Holiday))
                print(holidays[28:30])
            if week_select == 17:
                list((lambda holidays: print(holidays[30:33]), Holiday))
                print(holidays[30:33]) 
            if week_select == 18:
                list((lambda holidays: print(holidays[33:43]), Holiday))
                print(holidays[33:43]) 
            if week_select == 19:
                list((lambda holidays: print(holidays[43:45]), Holiday))
                print(holidays[43:45]) 
            if week_select == 20:
                list((lambda holidays: print(holidays[45:50]), Holiday))
                print(holidays[45:50]) 
            if week_select == 21:
                list((lambda holidays: print(holidays[50:53]), Holiday))
                print(holidays[50:53]) 
            if week_select == 22:
                list((lambda holidays: print(holidays[53:56]), Holiday))
                print(holidays[53:56]) 
            if week_select == 23:
                list((lambda holidays: print(holidays[56:58]), Holiday))
                print(holidays[56:58]) 
            if week_select == 24:
                list((lambda holidays: print(holidays[58:61]), Holiday))
                print(holidays[58:61]) 
            if week_select == 25:
                list((lambda holidays: print(holidays[61:66]), Holiday))
                print(holidays[61:66]) 
            if week_select == 26:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 27:
                list((lambda holidays: print(holidays[66]), Holiday))
                print(holidays[66]) 
            if week_select == 28:
                list((lambda holidays: print(holidays[67]), Holiday))
                print(holidays[67]) 
            if week_select == 29:
                list((lambda holidays: print(holidays[68]), Holiday))
                print(holidays[68]) 
            if week_select == 30:
                list((lambda holidays: print(holidays[69:71]), Holiday))
                print(holidays[69:71]) 
            if week_select == 31:
                list((lambda holidays: print(holidays[71:73]), Holiday))
                print(holidays[71:73]) 
            if week_select == 32:
                list((lambda holidays: print(holidays[73]), Holiday))
                print(holidays[73]) 
            if week_select == 33:
                list((lambda holidays: print(holidays[74]), Holiday))
                print(holidays[74]) 
            if week_select == 34:
                list((lambda holidays: print(holidays[75:77]), Holiday))
                print(holidays[75:77]) 
            if week_select == 35:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 36:
                list((lambda holidays: print(holidays[77:79]), Holiday))
                print(holidays[77:79]) 
            if week_select == 37:
                list((lambda holidays: print(holidays[79:84]), Holiday))
                print(holidays[79:84]) 
            if week_select == 38:
                list((lambda holidays: print(holidays[84:88]), Holiday))
                print(holidays[84:88]) 
            if week_select == 39:
                list((lambda holidays: print(holidays[88]), Holiday))
                print(holidays[88]) 
            if week_select == 40:
                list((lambda holidays: print(holidays[89:91]), Holiday))
                print(holidays[89:91]) 
            if week_select == 41:
                list((lambda holidays: print(holidays[91:95]), Holiday))
                print(holidays[91:95]) 
            if week_select == 42:
                list((lambda holidays: print(holidays[95:98]), Holiday))
                print(holidays[95:98]) 
            if week_select == 43:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 44:
                list((lambda holidays: print(holidays[98:100]), Holiday))
                print(holidays[98:100]) 
            if week_select == 45:
                list((lambda holidays: print(holidays[100:105]), Holiday))
                print(holidays[100:105]) 
            if week_select == 46:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 47:
                list((lambda holidays: print(holidays[105:108]), Holiday))
                print(holidays[105:108]) 
            if week_select == 48:
                list((lambda holidays: print(holidays[108:110]), Holiday))
                print(holidays[108:110]) 
            if week_select == 49:
                list((lambda holidays: print(holidays[110:112]), Holiday))
                print(holidays[110:112]) 
            if week_select == 50:
                list((lambda holidays: print(holidays[112:114]), Holiday))
                print(holidays[112:114]) 
            if week_select == 51:
                list((lambda holidays: print(holidays[114:117]), Holiday))
                print(holidays[114:117]) 
            if week_select == 52:
                list((lambda holidays: print(holidays[117:120]), Holiday))
                print(holidays[117:120]) 
            if week_select == 53:
                list((lambda holidays: print(holidays[120:len(holidays)]), Holiday))
                print(holidays[120:len(holidays)])             
            # else:
            #     print("Please select a valid number.")

        if view_year == 2024:
            with open('M07-Assessment\\holidays_2024.json') as json_file:
                data = json.load(json_file)
            holidays = []
            for i in data['holidays_2024']:
                holiday_object = Holiday(name = i['name'], date = i['date'])
                holidays.append(holiday_object)
            week_select = int(input('Select the week you would like to view(1-52): '))
            if week_select == 1:
                list((lambda holidays: print(holidays[0]), Holiday))
                print(holidays[0])
            if week_select == 2:
                list((lambda holidays: print(holidays[1]), Holiday))
                print(holidays[1])
            if week_select == 3:
                list((lambda holidays: print(holidays[2]), Holiday))
                print(holidays[2])
            if week_select == 4:
                list((lambda holidays: print(holidays[3:8]), Holiday))
                print(holidays[3:8])
            if week_select == 5:
                list((lambda holidays: print(holidays[8:10]), Holiday))
                print(holidays[8:10])
            if week_select == 6:
                list((lambda holidays: print(holidays[10:13]), Holiday))
                print(holidays[10:13])
            if week_select == 7:
                list((lambda holidays: print(holidays[13]), Holiday))
                print(holidays[13])
            if week_select == 8:
                list((lambda holidays: print(holidays[14:19]), Holiday))
                print(holidays[14:19])
            if week_select == 9:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 10:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 11:
                list((lambda holidays: print(holidays[19:21]), Holiday))
                print(holidays[19:21])  
            if week_select == 12:
                list((lambda holidays: print(holidays[21:23]), Holiday))
                print(holidays[21:23]) 
            if week_select == 13:
                list((lambda holidays: print(holidays[23:26]), Holiday))
                print(holidays[23:26]) 
            if week_select == 14:
                list((lambda holidays: print(holidays[26:28]), Holiday))
                print(holidays[26:28]) 
            if week_select == 15:
                list((lambda holidays: print(holidays[28:30]), Holiday))
                print(holidays[28:30]) 
            if week_select == 16:
                list((lambda holidays: print(holidays[30:32]), Holiday))
                print(holidays[30:32])
            if week_select == 17:
                list((lambda holidays: print(holidays[32:41]), Holiday))
                print(holidays[32:41]) 
            if week_select == 18:
                list((lambda holidays: print(holidays[41:46]), Holiday))
                print(holidays[41:46]) 
            if week_select == 19:
                list((lambda holidays: print(holidays[46:51]), Holiday))
                print(holidays[46:51]) 
            if week_select == 20:
                list((lambda holidays: print(holidays[51:54]), Holiday))
                print(holidays[51:54]) 
            if week_select == 21:
                list((lambda holidays: print(holidays[54:57]), Holiday))
                print(holidays[54:57]) 
            if week_select == 22:
                list((lambda holidays: print(holidays[57:59]), Holiday))
                print(holidays[57:59]) 
            if week_select == 23:
                list((lambda holidays: print(holidays[59:62]), Holiday))
                print(holidays[59:62]) 
            if week_select == 24:
                list((lambda holidays: print(holidays[62:67]), Holiday))
                print(holidays[62:67]) 
            if week_select == 25:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 26:
                list((lambda holidays: print(holidays[67]), Holiday))
                print(holidays[67]) 
            if week_select == 27:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 28:
                list((lambda holidays: print(holidays[68]), Holiday))
                print(holidays[68]) 
            if week_select == 29:
                list((lambda holidays: print(holidays[69]), Holiday))
                print(holidays[69]) 
            if week_select == 30:
                list((lambda holidays: print(holidays[70]), Holiday))
                print(holidays[70]) 
            if week_select == 31:
                list((lambda holidays: print(holidays[71:74]), Holiday))
                print(holidays[71:74]) 
            if week_select == 32:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 33:
                list((lambda holidays: print(holidays[74:76]), Holiday))
                print(holidays[74:76]) 
            if week_select == 34:
                list((lambda holidays: print(holidays[76]), Holiday))
                print(holidays[76]) 
            if week_select == 35:
                list((lambda holidays: print(holidays[77:79]), Holiday))
                print(holidays[77:79]) 
            if week_select == 36:
                list((lambda holidays: print(holidays[79:82]), Holiday))
                print(holidays[79:82]) 
            if week_select == 37:
                list((lambda holidays: print(holidays[82:86]), Holiday))
                print(holidays[82:86]) 
            if week_select == 38:
                list((lambda holidays: print(holidays[86:88]), Holiday))
                print(holidays[86:88]) 
            if week_select == 39:
                list((lambda holidays: print(holidays[88]), Holiday))
                print(holidays[88]) 
            if week_select == 40:
                list((lambda holidays: print(holidays[89:92]), Holiday))
                print(holidays[89:92]) 
            if week_select == 41:
                list((lambda holidays: print(holidays[92:98]), Holiday))
                print(holidays[92:98]) 
            if week_select == 42:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE') 
            if week_select == 43:
                list((lambda holidays: print(holidays[98:100]), Holiday))
                print(holidays[98:100]) 
            if week_select == 44:
                list((lambda holidays: print(holidays[100:102]), Holiday))
                print(holidays[100:102]) 
            if week_select == 45:
                list((lambda holidays: print(holidays[102:104]), Holiday))
                print(holidays[102:104]) 
            if week_select == 46:
                list((lambda holidays: print(holidays('NONE')), Holiday))
                print('NONE')
            if week_select == 47:
                list((lambda holidays: print(holidays[104:107]), Holiday))
                print(holidays[104:107]) 
            if week_select == 48:
                list((lambda holidays: print(holidays[107:111]), Holiday))
                print(holidays[107:111]) 
            if week_select == 49:
                list((lambda holidays: print(holidays[111]), Holiday))
                print(holidays[111]) 
            if week_select == 50:
                list((lambda holidays: print(holidays[112:116]), Holiday))
                print(holidays[112:116]) 
            if week_select == 51:
                list((lambda holidays: print(holidays[116:120]), Holiday))
                print(holidays[116:120]) 
            if week_select == 52:
                list((lambda holidays: print(holidays[120:len(holidays)]), Holiday))
                print(holidays[120:len(holidays)])       
            # else:
            #     print("Please select a valid number.")

        view_again = input('Would you like to view more holidays? (y/n) ')
        if(view_again != 'y' and view_again != 'n'):
            print('Invalid response. Expected "y" or "n".')
            continue
        if view_again == 'y':
            continue
        if view_again == 'n': 
            break


def save_4():
    print('Save Changes')
    print('============')
    while True:
        global confirm_save
        confirm_save = input('Save changes to JSON? [y/n]')
        if (confirm_save != 'y' and confirm_save != 'n'):
            print('\nInvalid input. Please try again\n')
        else: break

    if confirm_save == 'n':
        print('\n Abort! Returning to Main Menu\n')
    else:
        with open('holidays.json', 'w') as file:
            json.dump('Holiday', file)#, cls=EnhancedJSONEncoder)
            print('\nYour changes have been saved!\n')
  

hol_start()

#Pull up main menu and provide function interaction
while running:
    display_main_menu()
    menu_option = int(input('Select your menu option number: '))
    if menu_option != 1 and menu_option != 2 and menu_option !=3 and menu_option != 4 and menu_option != 5:
        print('\nPlease select a valid menu option')
    elif menu_option == 1:
        add_holiday_1()
    elif menu_option == 2:
        remove_holiday_2()
    elif menu_option == 3:
        view_holiday_3()
    elif menu_option == 4:
        save_4()
    elif menu_option == 5:
        print('Exit')
        print('====')
        print('Any unsaved changes will be lost.')
        while True:
            global exit
            exit = input('Are you sure you want to exit? (y/n): ')
            if (exit != 'y' and exit != 'n'):
                print('Invalid response. Expected "y" or "n".')
            else: break

        if exit == 'n':
            print('Returning to main menu')
        else: 
            print('Goodbye!')
            running = False
else:
     print('\nPlease select a valid menu option')