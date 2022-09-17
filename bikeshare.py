import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        print("Available cites : Chicago - New York City - Washington")
        city = input("Enter city name : ").lower()
        if city not in CITY_DATA.keys() :
            print("Sorry, You entered invalid data. Please try again!! ")
        else :
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ["All", "January", "February", "March", "April", "May" , "June"]
    
    while True :
        print("Available months : All - January - February - March - April - May - June")
        month = input("Enter month : ").title()
        if month not in months :
            print("Sorry, You entered invalid data. Please try again!! ")
        else :
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    while True :
        print("Available days : All - Monday - Tuesday - Wednesday - Thursday - Friday - Saturday - Sunday")
        day = input("Enter day : ").title()
        if day not in days :
            print("Sorry, You entered invalid data. Please try again!! ")
        else :
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert format to datetime
    df['Month'] = df['Start Time'].dt.month # extract month and day from "start time" column
    df['Day'] = df['Start Time'].dt.weekday_name
    
    if month != "All" : # exclude choice " all "
        months = ["January", "February", "March", "April", "May", "June"]
        month = months.index(month) + 1
        df = df[df['Month'] == month] # filter by month
    if day != "All": # exclude choice " all "
        df = df[df['Day'] == day.title()] # filter by day
        


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print("Most common month is {}".format(common_month))


    # TO DO: display the most common day of week
    common_day = df['Day'].mode()[0]
    print("Most common day is {}".format(common_day))


    # TO DO: display the most common start hour
    
    df['Hour'] = df['Start Time'].dt.hour # extract hour first
    common_hour = df['Hour'].mode()[0]
    print("Most common start hour is {}".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most common start station is {} ".format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most common end station is {} ".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Track'] = df['Start Station'] + " to " + df['End Station']
    common_track = df['Track'].mode()[0]
    print("Most common track is from {} ".format(common_track))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time equals {}".format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel time equals {}".format(mean_travel_time))
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
     # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()
    print("Types of users and their counts : \n",count_users)
    print("")
    
    if city == 'washington' :
        
        print("No data about gender or birth year is available")

    else :
    # TO DO: Display counts of gender
        count_genders = df['Gender'].value_counts()
        print("Genders and their counts : \n",count_genders)   
        print("")


    # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = int(df['Birth Year'].mode()[0])
        print("Year Of Birth : ")
        print("Earliest : ",earliest,"\nMost Recent : ",most_recent,"\nMost Common : ",most_common)        
        



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display(df) :
    
    print("Data is available to check")
    i = 0
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes-no :').lower()
    if view_data not in ['no','yes'] :
        print("Wrong input please try again")
        print("")
        view_data = input('Would you like to view 5 rows of individual trip data? Enter yes-no :').lower()
        
    elif view_data != 'yes' : 
        print("Great, Thank You ")
    else :
        while i+5 < df.shape[0] :
            print(df.iloc[i:i+5])
            i+=5
            view_data = input('Do you wish to continue ? yes or no?').lower()
            if view_data != 'yes':
                print("Great, Thank You ")
                break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
