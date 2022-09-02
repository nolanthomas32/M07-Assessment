from datetime import datetime
import datetime as dt
import json
from json import JSONEncoder
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field



@dataclass
class Holiday:
    name: str
    date: dt

    def __str__(self):
        return f"{self.name} takes place on {self.date}"



class HolidayList:
    def __init__(self):
       self.innerHolidays = []


    def findHoliday(self, HolidayName, Date):
        for a_holiday in self.innerHolidays:
            if a_holiday.name == HolidayName and a_holiday.date.strftime('%Y-%m-%d') == Date:
                print(a_holiday)
                return a_holiday
                
   
    def addHoliday(self, holidayObj):
        a_holiday = self.findHoliday(holidayObj.name, holidayObj.date.strftime('%Y-%m-%d'))
        if type(a_holiday) != Holiday:
            self.innerHolidays.append(holidayObj)
            print(f'Success! {holidayObj.name} has been added.')
        else:
            print('This holiday already exists. Please try again.')
    
    def removeHoliday(self, holidayObj):
        a_holiday = self.findHoliday(holidayObj.name, holidayObj.date.strftime('%Y-%m-%d'))
        if type(a_holiday) == Holiday:
            self.innerHolidays.remove(holidayObj)
            print(f'Success! {holidayObj.name} has been removed.')
        else:
            print('This holiday does not exist. Please try again.')

    def string_date_holiday(self, name, date):
        str_format = '%Y-%m-%d'
        date_obj = dt.datetime.strptime(date, str_format)
        holidayObj = Holiday(name, date_obj)
        return holidayObj

    def read_json(self, filelocation):
        with open(filelocation, 'r') as json_file:
            data = json.load(json_file)
            for dictionary in data['holidays']:
                holiday_obj = self.string_date_holiday(dictionary['name'], dictionary['date'])
                self.addHoliday(holiday_obj)

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
            return o.__dict__

def json_default(value):
    if isinstance(value, dt.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__



Nolan_Holiday_List = HolidayList()
Nolan_Holiday_List.read_json('holidays.json')
# holiday2 = Holiday('Arbor Day', datetime(2022, 8, 30))
# Nolan_Holiday_List.addHoliday(holiday2)
# print(Nolan_Holiday_List.innerHolidays)


running = True
active = True
name = True


def get_2020_holidays():
    response = requests.get('https://www.timeanddate.com/holidays/us/2020?hol=33554809')
    html = response.text
    parsed_html = BeautifulSoup(html, "html.parser")

    table = parsed_html.find('table', attrs= {"id":"holidays-table"})
    body = table.find('tbody')
    tr = body.find_all('tr', attrs={"class":"showrow"})

    th_all = body.find_all("tr", attrs={"class":"showrow"})

    Nolan_Holiday_List = []
    for holiday in tr:
        holiday_object = Holiday(name = holiday.text[6:], date = holiday.text[:6])
        Nolan_Holiday_List.addHoliday(holiday_object)

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

            hol_name = (input("Enter the Holiday name here: "))
            try:
                year = int(input('Enter a 4 digit year: '))
                month = int(input('Enter a 2 digit month: '))
                day = int(input('Enter a 2 digit day: '))
            except:
                print('Please only enter Date information as numbers.')
            hol_date = datetime(year, month, day)
            # Holiday(name = hol_name, date= hol_date)
            holiday_object = Holiday(name = hol_name, date = hol_date)
            Nolan_Holiday_List.addHoliday(holiday_object)
            # print(f'{hol_name} has been adddd on {hol_date}')
            # print(Nolan_Holiday_List.innerHolidays)
            cont = input('Would you like to add another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break

def remove_holiday_2():
        print('Welcome to the Holiday removal screen!')
        while active:

            hol_name = (input("Enter the Holiday name here: "))
            try:
                year = int(input('Enter a 4 digit year: '))
                month = int(input('Enter a 2 digit month: '))
                day = int(input('Enter a 2 digit day: '))
            except:
                print('Please only enter Date information as numbers.')
            hol_date = datetime(year, month, day)
            # Holiday(name = hol_name, date= hol_date)
            holiday_object = Holiday(name = hol_name, date = hol_date)
            Nolan_Holiday_List.removeHoliday(holiday_object)
            # print(f'{hol_name} has been removed.')
            # print(Nolan_Holiday_List.innerHolidays)
            cont = input('Would you like to remove another holiday? (y/n) ')
            if cont == 'y':
                continue
            else:
                break

def view_holiday_3():
    print('View Holidays')
    while active:
        # print(Nolan_Holiday_List.innerHolidays)
        try:
            year_select = int(input('Select the 4 digit year to view: '))
            week_select = int(input('Select the 2 digit week to view: '))
        except:
            print('Please only enter Date information as numbers.')
        list((lambda holidays: print(holidays), Nolan_Holiday_List))
        print(f'{Nolan_Holiday_List.innerHolidays}\n')
        weather = input('Would you like to see the weather for this week? (y/n) ')
        if weather != 'y' and weather != 'n':
            print('Option not recognized. Expecting a y or n')
        if weather == 'y':
            get_weather()
        else:
            break
        # hol_value = datetime.isocalendar(year_select, week_select)
        # print(hol_value)



def save_4():
    print('Save Changes')
    print('============')
    while True:
        global confirm_save
        confirm_save = input('Save changes to JSON? (y/n) ')
        if (confirm_save != 'y' and confirm_save != 'n'):
            print('\nInvalid input. Please try again\n')
        else: break

    if confirm_save == 'n':
        print('\n Abort! Returning to Main Menu\n')
    else:
        out_file = open("holidays.json", "w")
        json.dump(Nolan_Holiday_List, out_file, indent = 2, cls=CustomEncoder, default=json_default)
        out_file.close()
        print('\nYour changes have been saved!\n')


hol_start()

#Pull up main menu and provide function interaction
while running:
    display_main_menu()
    try:
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
                break
    except:
        print('\nPlease only enter a number.')