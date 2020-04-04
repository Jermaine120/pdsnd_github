# **Bikeshare Python Project**

### Initiate Script
1. Locate bikeshare.py
> This file has code to start application
2. Open GitBash and type python
3. Answer questions provided

### Project Scope
This code allows user(s) to input certain characteristics about Chicago, New York City, and Washington followed by either entering months between January thru June or all months and weekday or all days. The return values will display time stats, station stats, trip duration stats, user stats, user type with counts, and five lives of data values.

#### Function Get Filters
Allows user to input a city, month, and day.

#### Function Load data
Loads data for the specified city and filters by month and day if applicable into a dataframe

#### Function Time Stats
Displays statistics on the most frequent times of travel.

#### Function Station Stats
Displays statistics on the most popular stations and trip.

#### Function Trip Duration Stats
Displays statistics on the total and average trip duration.

#### Function User Stats
Displays statistics on bikeshare users.

#### Function Find Commons
Find the most common month, day, & week by cycling through DataFrame

#### Function User Type counts
Display the User Type counts

#### Function Five Lines
Script displays 5 lines of raw data after user answers *yes*

#### *Output example:*
```js
Hello! Let's explore some US bikeshare data!
Enter a city chicago, new york city, or washington: washington
Enter a month all, january, february, march, april, may, june: march
Enter a day or all: sunday
----------------------------------------

Calculating The Most Frequent Times of Travel...

Most Common Month: 3
Most Common Day of Week: Sunday
Most Common Start Hour: 14

This took 0.0 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

Common Start Station: Jefferson Dr & 14th St SW
Common End Station: Jefferson Dr & 14th St SW
Frequent Combination: Jefferson Dr & 14th St SW >>> Jefferson Dr & 14th St SW

This took 0.00812387466430664 seconds.

```
