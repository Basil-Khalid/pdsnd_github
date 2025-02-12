import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def choose_city():
    """
    Prompt user to select a city for analysis.
    Returns:
        str: Selected city name.
    """
    city_options = {'1': 'chicago', '2': 'new york city', '3': 'washington'}
    while True:
        choice = input("\nChoose a city to analyze:\n1. Chicago\n2. New York City\n3. Washington\nEnter the number: ").strip()
        if choice in city_options:
            return city_options[choice]
        print("Invalid choice. Please select 1, 2, or 3.")

def load_data(city):
    """
    Load data for the specified city into a DataFrame.
    Args:
        city (str): The name of the city.
    Returns:
        pd.DataFrame: City data.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent travel times.
    
    Args:
        df (pd.DataFrame): The bikeshare dataset.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    1
    # Most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"Most Common Month: {months[most_common_month - 1]}")
    
    # Most common day of the week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f"Most Common Day of Week: {most_common_day}")
    
    # Most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    time_of_day = "Morning" if most_common_hour < 12 else "Afternoon" if most_common_hour < 17 else "Evening"
    print(f"Most Common Start Hour: {most_common_hour} ({time_of_day})")
    print('-'*60)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trips.
    
    Args:
        df (pd.DataFrame): The bikeshare dataset.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    print(f"Most Common Start Station: {df['Start Station'].mode()[0]}")
    print(f"Most Common End Station: {df['End Station'].mode()[0]}")
    df['start_to_end'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most Common Trip: {df['start_to_end'].mode()[0]}")
    print('-' * 60)

def trip_duration_stats(df):
    """
    Displays statistics on total and average trip duration.
    
    Args:
        df (pd.DataFrame): The bikeshare dataset.
    """
    total_travel_time = df['Trip Duration'].sum()
    average_travel_time = df['Trip Duration'].mean()
    print(f"Total Travel Time: {total_travel_time} seconds ({total_travel_time / 3600:.2f} hours)")
    print(f"Average Travel Time: {average_travel_time:.2f} seconds ({average_travel_time / 3600:.2f} hours)")
    print('-' * 60)

def user_stats(df):
    """
    Displays statistics on bikeshare users, including user types, gender, and birth year.
    
    Args:
        df (pd.DataFrame): The bikeshare dataset.
    """
    print('\nCalculating User Stats...\n')
    print("User Type Counts:")
    print(df['User Type'].value_counts())
    
    if 'Gender' in df:
        print("\nGender Counts:")
        print(df['Gender'].value_counts())
    else:
        print("\nGender data not available for this city.")
    
    if 'Birth Year' in df:
        print("\nBirth Year Statistics:")
        print(f"Earliest Birth Year: {int(df['Birth Year'].min())}")
        print(f"Most Recent Birth Year: {int(df['Birth Year'].max())}")
        print(f"Most Common Birth Year: {int(df['Birth Year'].mode()[0])}")
    else:
        print("\nBirth year data not available for this city.")
    print('-' * 60)

def display_raw_data(df):
    """
    Displays raw data 5 rows at a time upon user request.
    
    Args:
        df (pd.DataFrame): The bikeshare dataset.
    """
    row_index = 0
    while True:
        print(df.iloc[row_index: row_index + 5])
        row_index += 5
        more_data = input("\nDo you want to see 5 more lines of raw data? Enter 'yes' or 'no': ").lower()
        if more_data != 'yes' or row_index >= len(df):
            break

def main():
    while True:
        df = load_data(choose_city())
        while True:
            choice = input("\nChoose an analysis:\n1. Travel Times\n2. Stations\n3. Trip Duration\n4. User Info\n5. Raw Data\n6. Exit\nEnter number: ").strip()
            if choice == '1':
                time_stats(df)
            elif choice == '2':
                station_stats(df)
            elif choice == '3':
                trip_duration_stats(df)
            elif choice == '4':
                user_stats(df)
            elif choice == '5':
                display_raw_data(df)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Try again.")
        if input("\nRestart? ('yes' to continue): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()