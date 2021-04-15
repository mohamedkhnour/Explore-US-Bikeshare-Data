import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
    

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_selection = input('to view available BS data, kindly type: \n The letter(ch) for Chicago \n The letter (ny) for New York City \n The letter (W) for Washington \n').lower()

    while city_selection not in {'ch','ny','w'}:
        print('that is invalid input .')
        city_selection = input('to view available BS data, kindly type: \n The letter(ch) for Chicago \n The letter (ny) for New York City \n The letter (W) for Washington \n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    monthes=['january','february','march','april','may','june','all']
    month_selection = input('select month \n January \n February\n  March\n  April\n  May\n  June\n ALL\n').lower()

    while month_selection not in monthes:
        print('that is invalid input .')
        month_selection = input('select month \nJA January \nFE February\n MA March\n AP April\n MA May\n JU June\n ALL\n').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_selection =input('select Day \nMonday \nTuesday\nWednesday\n Thursday\nFriday\n Saturday\n Sunday\n ALL').lower()
    days=['monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday','all']
    while day_selection not in days:
        print('that is invalid input .')
        day_selection = input('select Day \nMonday \nTuesday\nWednesday\n Thursday\nFriday\n Saturday\n Sunday\n ALL').lower()
 

    print('-'*40)
    return city_selection, month_selection, day_selection



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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
    


    return df

def time_stats(df1):
    """Displays statistics on the most frequent times of travel."""
    df = df1
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    popular_day = df['day'].mode()[0]
    print('Most Popular Start month:', popular_day)
    
    
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return(time.time() - start_time)


def station_stats(df1):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df = df1
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most  start station from  data is: " + common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most end station  is: " + common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The moststart station and end station trip is : " + str(frequent_combination.split("||")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given fitered data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    gender = df['Gender'].value_counts()
    print("The count of user gender from the given fitered data is: \n" + str(gender))

    # TO DO: Display counts of gender
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
    print('Most recent birth from the given fitered data is: {}\n'.format(most_recent_birth))
    print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth) )


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



'''def main():
    city,month,day=get_filters()
    df=load_data(city,month,day)
    #print(df.head())
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    if city=='ch':
        user_stats(df)'''

def display_raw_data(df):
    
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city=='ch':
            user_stats(df)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        


if __name__ == "__main__":
	main()
