import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
    name: str
    date: datetime

    def __str__(self):
        return f"{self.name} takes place on {self.date}"

    
                 
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []


    def findHoliday(self, HolidayName, Date):
        for a_holiday in self.innerHolidays:
            if a_holiday.name == HolidayName and a_holiday.date.strftime('%Y-%m-%d') == Date:
                print(a_holiday)
                return a_holiday
                
        #for each holiday in self inner holiday:
            #does holiday name equal name that was input and does holiday date = holiday date input
            #holiday date strf time '%Y-%m-%d'
    # Find Holiday in innerHolidays
    # Return Holiday
   
    def addHoliday(self, holidayObj):
        a_holiday = self.findHoliday(holidayObj.name, holidayObj.date.strftime('%Y-%m-%d'))
        if type(a_holiday) != Holiday:
            self.innerHolidays.append(holidayObj)
            print(f'Success! {holidayObj.name} has been added.')
        else:
            print('This holiday already exists. Please try again.')
            # print(self.innerHolidays)
        #We need this to be a holiday object
    
    def removeHoliday(self, holidayObj):
        a_holiday = self.findHoliday(holidayObj.name, holidayObj.date.strftime('%Y-%m-%d'))
        if type(a_holiday) == Holiday:
            self.innerHolidays.remove(holidayObj)
            print(f'Success! {holidayObj.name} has been removed.')
            # print(self.innerHolidays)
    # Find Holiday in innerHolidays by searching the name and date combination.
    # remove the Holiday from innerHolidays
    # inform user you deleted the holiday

    def string_date_holiday(self, name, date):
        str_format = '%Y-%m-%d'
        date_obj = datetime.datetime.strptime(date, str_format)
        holidayObj = Holiday(name, date_obj)
        return holidayObj

    def read_json(self, filelocation):
        with open(filelocation, 'r') as json_file:
            data = json.load(json_file)
            for dictionary in data['holidays']:
                holiday_obj = self.string_date_holiday(dictionary['name'], dictionary['date'])
                self.addHoliday(holiday_obj)

                

# def read_json(self, filelocation):
#     with open(filelocation, 'r') as json_file:
#         data = json.load(json_file)
#         for dictionary in data['holidays']:
#             self.string_date_holiday(dictionary['name'], dictionary['date'])
#             print(dictionary['name'], dictionary['date'])

# read_json('holidays.json')

holiday1 = Holiday('My Birthday', datetime.datetime.now())
holiday2 = Holiday('Arbor Day', '2022-08-30')
holiday3 = Holiday('Veterans Day', datetime.datetime.now())
# print(holiday1)


Nolan_Holiday_List = HolidayList()
Nolan_Holiday_List.addHoliday(holiday1)
Nolan_Holiday_List.addHoliday(holiday2)
Nolan_Holiday_List.addHoliday(holiday3)
Nolan_Holiday_List.removeHoliday(holiday1)
Nolan_Holiday_List.read_json('holidays.json')
print(Nolan_Holiday_List.innerHolidays)


# Tom_Holiday_List = HolidayList()
# Tom_Holiday_List.addHoliday(holiday1)
Nolan_Holiday_List.findHoliday('My Birthday','2022-09-01')


  
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

#     def save_to_json(filelocation):
#         # Write out json file to selected file.
        
#     def scrapeHolidays():
#         # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
#         # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
#         # Check to see if name and date of holiday is in innerHolidays array
#         # Add non-duplicates to innerHolidays
#         # Handle any exceptions.     

#     def numHolidays():
#         # Return the total number of holidays in innerHolidays
    
#     def filter_holidays_by_week(year, week_number):
#         # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
#         # Week number is part of the the Datetime object
#         # Cast filter results as list
#         # return your holidays

#     def displayHolidaysInWeek(holidayList):
#         # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
#         # Output formated holidays in the week. 
#         # * Remember to use the holiday __str__ method.

#     def getWeather(weekNum):
#         # Convert weekNum to range between two days
#         # Use Try / Except to catch problems
#         # Query API for weather in that week range
#         # Format weather information and return weather string.

#     def viewCurrentWeek():
#         # Use the Datetime Module to look up current week and year
#         # Use your filter_holidays_by_week function to get the list of holidays 
#         # for the current week/year
#         # Use your displayHolidaysInWeek function to display the holidays in the week
#         # Ask user if they want to get the weather
#         # If yes, use your getWeather function and display results



# def main():
#     # Large Pseudo Code steps
#     # -------------------------------------
#     # 1. Initialize HolidayList Object
#     # 2. Load JSON file via HolidayList read_json function
#     # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     # 3. Create while loop for user to keep adding or working with the Calender
#     # 4. Display User Menu (Print the menu)
#     # 5. Take user input for their action based on Menu and check the user input for errors
#     # 6. Run appropriate method from the HolidayList object depending on what the user input is
#     # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


# if __name__ == "__main__":
#     main();


# # Additional Hints:
# # ---------------------------------------------
# # You may need additional helper functions both in and out of the classes, add functions as you need to.
# #
# # No one function should be more then 50 lines of code, if you need more then 50 lines of code
# # excluding comments, break the function into multiple functions.
# #
# # You can store your raw menu text, and other blocks of texts as raw text files 
# # and use placeholder values with the format option.
# # Example:
# # In the file test.txt is "My name is {fname}, I'm {age}"
# # Then you later can read the file into a string "filetxt"
# # and substitute the placeholders 
# # for example: filetxt.format(fname = "John", age = 36)
# # This will make your code far more readable, by seperating text from code.





