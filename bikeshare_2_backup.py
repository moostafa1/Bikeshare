import sys
import time
import numpy as np
import pandas as pd
#import datetime




CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


cities = list(CITY_DATA.keys())
months = ['January', 'February', 'March', 'April', 'May', 'June']
days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']




def space(fun_name='what'):
    print("\n\n", end='-'*120)
    print('#'*120, '\t'*7+f'{fun_name}\n', end='#'*120)
    #print('#'*120, '\t'*7+'SPACE\n', end='#'*120)
    print('-'*120, end="\n\n")





# used to determine the input city
def chooseCity(lst, dictionary):
    """
    used to take city either by its name or number that represents its order
    Args:
        city_names_lst
    Returns:
        city_name
        df related to that city
    """
    city = input("Would you like to see data for Chicago, New York City, or Washington?\n")
    city = city.lower()
    if city in cities:
        print(f"you choosed: {city}")
        #return city
    elif city.isdigit():
        city = int(city)-1
        if city < len(cities):
            city = cities[city]
            print(f"you choosed: {city}")
        else:
            print(f"city number should be in range: (1:{len(cities)})")
            restart = input("invalid city number, input again?   (y/n)\n")
            if restart != 'y':
                sys.exit()
            else:
                city = chooseCity(lst, dictionary)
    else:
        restart = input("invalid city name, input again?   (y/n)\n")
        if restart != 'y':
            sys.exit()
        else:
            city = chooseCity(lst, dictionary)
    return city





def showCityData(city, dictionary):
    city_file = dictionary.get(city)
    data = pd.read_csv(city_file)
    df = pd.DataFrame(data)
    print('\t'*7, city, '\n')
    print(df)
    return df





def chooseMonth(lst, used="month"):
    """
    used to take month either by its name or number that represents its order
    Args:
        month_names_lst
    Returns:
        month as int value from 1:6
    """
    month = input(f"\n\nPlease enter the {used} you want, or you can use all to get all {used+'s'}:\n")
    month = month.title()
    value_idx = []
    for i, v in enumerate(lst):
        value_idx.append(i+1)
    #print(value_idx)

    if month in lst:
        month = lst.index(month)+1
        print(f"you choosed: {lst[month-1]}")

    elif month.isdigit():
        #print(type(month))    # str
        month = int(month)
        if month in value_idx:
            print(f"you choosed: {lst[month-1]}")
        else:
            print(f"\n{used} number must be in range of: (1:{len(lst)})")
            restart = input("invalid month name, input again?   (y/n)\n")
            if restart != 'y':
                sys.exit()
            else:
                month = chooseMonth(lst)

    else:
        month = month.lower()
        if month == 'all':
            print(f"you choosed: {month}")
            #return value
        else:
            restart = input("invalid month name, input again?   (y/n)\n")
            if restart != 'y':
                sys.exit()
            else:
                month = chooseMonth(lst)
    return month





def chooseDay(lst, month, used="day"):
    """
    used to take day either by its name or number that represents its order in the month
    Args:
        day_names_lst
    Returns:
        day name in the week or day order in the month according to the given input
    """
    day = input(f"\n\nPlease enter the {used} you want, or you can use all to get all {used+'s'}:\n")
    day = day.title()

    if day in lst:
        print(f"you choosed: {day}")
        #return day

    elif day.isdigit():
        # months that ends with 30 , 31, 28
        # 1-31, 2-28, 3-31, 4-30, 5-31, 6-30, 7-31, 8-31, 9-30, 10-31, 11-30, 12-31
        month_start = 1
        month_end = 31
        normal_end = 30
        february_end = 28
        months_31 = [1, 3, 5]
        months_30 = [4, 6]
        day = int(day)
        if month == 2:
            if day in range(month_start, february_end+1):
                print(f"you choosed: {day}")
            else:
                print(f"Month {month} is {february_end} days")
                print(f"please check that your day in range: ({month_start}, {february_end})")
                restart = input("invalid day number, input again?   (y/n)\n")
                if restart != 'y':
                    sys.exit()
                else:
                    day = chooseDay(lst, month)

        elif month in months_31:#== 1 or month == 3 or month == 1 or month == 5:
            if day in range(month_start, month_end+1):
                print(f"you choosed: {day}")
            else:
                print(f"Month {month} is {month_end} days")
                print(f"please check that your day in range: ({month_start}, {month_end})")
                restart = input("invalid day number, input again?   (y/n)\n")
                if restart != 'y':
                    sys.exit()
                else:
                    day = chooseDay(lst, month)

        elif month in months_30:#== 4 or month == 6:
            if day in range(month_start, normal_end+1):
                print(f"you choosed: {day}")
            else:
                print(f"Month {month} is {normal_end} days")
                print(f"please check that your day in range: ({month_start}, {month_end})")
                restart = input("invalid day number, input again?   (y/n)\n")
                if restart != 'y':
                    sys.exit()
                else:
                    day = chooseDay(lst, month)

    else:
        day = day.lower()
        if day.lower() == 'all':
            print(f"you choosed: {day}")
            #return day
        else:
            print(f"Please make sure that the day name is one of: {lst}")
            restart = input("invalid day name, input again?   (y/n)\n")
            if restart != 'y':
                sys.exit()
            else:
                day = chooseDay(lst, month)
    return day





def get_filters(dictionary):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = chooseCity(cities, CITY_DATA)
    # get user input for month (all, january, february, ... , june)
    month = chooseMonth(months)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = chooseDay(days, month)
    print(f"{city}:  ({day}/{month})")
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    if month == 'all':
        df['month'] = df['Start Time'].dt.month
    else:
        df['month'] = df['Start Time'].dt.month[df['Start Time'].dt.month == month]


    str_day = isinstance(day, str)
    int_day = isinstance(day, int)
    if day == 'all':
        df['day_of_week'] = df['Start Time'].dt.day
    elif str_day:
        df['day_of_week'] = df['Start Time'].dt.day_name()[df['Start Time'].dt.day_name() == day]
    elif int_day:
        df['day_of_week'] = df['Start Time'].dt.day[df['Start Time'].dt.day == day]

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    filtered_df = df.dropna(subset=['month', 'day_of_week'])

    return filtered_df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # display the most common month
    popular_month = df['month'].mode()[0]
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print(f"most common month: {popular_month}")
    print(f"most common day: {popular_day}")
    print(f"most common hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    return df




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    start_station_count = df['Start Station'].value_counts()[0]
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    end_station_count = df['End Station'].value_counts()[0]
    # display most frequent combination of start station and end station trip
    popular_Start_End_stations = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    Start_End_stations_counts = (df['Start Station'] + " - " + df['End Station']).value_counts()[0]

    print(f"most commonly used start station: {popular_start_station}, times: {start_station_count}")
    print(f"most commonly used end station:   {popular_end_station}, times: {end_station_count}")
    print(f"most frequent combination of start station and end station trip: {popular_Start_End_stations}, times: {Start_End_stations_counts}")

    print("\nThis took %s seconds." % (time.time() - start_time))




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    day = total_travel_time // (24*60*60)
    hour = (total_travel_time % (24*60*60)) // (60*60)
    minute = ((total_travel_time % (24*60*60)) % (60*60)) // 60
    second = ((total_travel_time % (24*60*60)) % (60*60)) % 60
    print(f"For the selected filters, the total travel time is : {day} day, {hour} hour, {minute} minute, {second} second")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    d = mean_travel_time // (24*60*60)
    hr = (mean_travel_time % (24*60*60)) // (60*60)
    min = ((mean_travel_time % (24*60*60)) % (60*60)) // 60
    sec = ((mean_travel_time % (24*60*60)) % (60*60)) % 60
    print(f"For the selected filters, the mean travel time is : {d} day, {hr} hour, {min} minute, {sec} second")

    print("\nThis took %s seconds." % (time.time() - start_time))




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"Types of users:\n\n{user_types}\n\n")

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(f"Types of gender:\n\n{gender}\n\n\n")

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()

    most_recent_birth_year = df['Birth Year'].max()

    popular_birth_year = df['Birth Year'].mode()[0]

    print(f"earliest year of birth: {earliest_birth_year}")
    print(f"most recent year of birth: {most_recent_birth_year}")
    print(f"most common year of birth: {popular_birth_year}")
    print("\nThis took %s seconds." % (time.time() - start_time))





def main():
    while True:
        space('get_filters')
        city, month, day = get_filters(CITY_DATA)
        space('END')

        space('load_data')
        filtered_df = load_data(city, month, day)
        print(filtered_df)
        space('END')

        space('showCityData')
        df = showCityData(city, CITY_DATA)
        space('END')

        space('time_stats')
        filtered_df = time_stats(filtered_df)
        space('END')

        space('station_stats')
        station_stats(filtered_df)
        space('END')

        space('trip_duration_stats')
        trip_duration_stats(filtered_df)
        space('END')

        space('user_stats')
        user_stats(filtered_df)
        space('END')

        restart = input('\nWould you like to restart? (y/n).\n')
        if restart.lower() != 'y':
            break
        space('AGAIN')



if __name__ == "__main__":
    main()
