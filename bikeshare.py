import time
import pandas as pd
import numpy as np
import random as rn


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january', 'february', 'march', 'april', 'may', 'june']
week_days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = CITY_DATA
    city = ''
    while city not in cities:
        city = input("Enter a city chicago, new york city, or washington: ").lower()
    #print(city)

    # get user input for month (all, january, february, ... , june)
    month = ''
    while month not in months:
        month = input("Enter a month all, january, february, march, april, may, june: ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in week_days:
        day = input("Enter a day or all: ").lower()

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
    file_name = CITY_DATA.get(city)
    df = pd.read_csv(file_name)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        # months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
         df = df[df['week_day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_column = df['month']
    common_month = find_commons(month_column)
    print('Most Common Month: {}'.format(common_month))

    # display the most common day of week
    day_column = df['week_day']
    common_day = find_commons(day_column)
    print('Most Common Day of Week: {}'.format(common_day))

    # display the most common start hour
    hour_column = df['hour']
    common_hour = find_commons(hour_column)
    print('Most Common Start Hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Common Start Station: {}'.format(common_start_station))


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Common End Station: {}'.format(common_end_station))


    # display most frequent combination of start station and end station trip
    df['fcs'] = df['Start Station'] + " >>> " + df['End Station']
    fcs = df['fcs'].mode()[0]

    print("Frequent Combination: {}".format(fcs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['time_diff'] = df['End Time'] - df['Start Time']
    travel_time = df['time_diff'].sum()

    print('Total Travel Time: {}'.format(travel_time))


    # display mean travel time
    df['mtt'] = df['End Time'] - df['Start Time']
    avg_time = df['mtt'].mean()
    print('Mean Travel Time: {}'.format(avg_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of User Types: \n{}\n".format(user_types))

    # Display counts of gender
    t = df['Gender']
    gender = t.value_counts()
    print("Count of Gender: \n{}".format(gender))

    # Display earliest, most recent, and most common year of birth
    year_birth = df['Birth Year']
    earliest = year_birth.min()
    recent = year_birth.max()
    common_year = year_birth.mode()[0]

    print("\nThe birth stats are {} earliest, {} most recent, and {} common year".
        format(int(earliest),int(recent),int(common_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def find_commons(data_column):
    #Find the most common month, day, & week by cycling through DataFrame
    counter = {}
    for spinner in data_column:
        counter[spinner] = counter.get(spinner,0) + 1

    data_column = max(counter, key = lambda d: counter[d])

    return data_column


def user_type_count(df):
    # Display the User Type counts
    cust_type = df['User Type']
    cust, cnt = np.unique(cust_type, return_counts=1)
    results = pd.DataFrame(np.c_[cust, cnt], columns = (('User_Type', 'Counts')))

    print("Counts of User Type: \n{}".format(results))


def five_lines(df):
    #Script displays 5 lines of raw data after user answers 'yes'
    while True:
        ans = input('Display 5 lines of raw data enter yes or no: ').lower()

        if ans == 'yes':
            df = df.rename(columns={'Unnamed: 0': 'id'})
            rays = np.array(df)
            id_num = np.random.choice(len(rays),5)

            i = 0
            while i <= 4:
                print(df.iloc[[id_num[i]]])
                i += 1
        else:
            ans == 'no'
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_type_count(df)
        five_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
