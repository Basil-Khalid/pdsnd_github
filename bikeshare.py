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
    Display statistics on the most frequent travel times.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Most common month
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"Most Common Month: {months[df['Start Time'].dt.month.mode()[0] - 1]}")
    
    # Most common day of the week
    print(f"Most Common Day: {df['Start Time'].dt.day_name().mode()[0]}")
    
    # Most common start hour
    hour = df['Start Time'].dt.hour.mode()[0]
    time_period = "Morning" if hour < 12 else "Afternoon" if hour < 18 else "Evening"
    print(f"Most Common Start Hour: {hour} ({time_period})")
    print('-' * 60)

def station_stats(df):
    """
    Display statistics on the most popular stations and trips.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print(f"Most Common Start Station: {df['Start Station'].mode()[0]}")
    print(f"Most Common End Station: {df['End Station'].mode()[0]}")
    print(f"Most Common Trip: {(df['Start Station'] + ' to ' + df['End Station']).mode()[0]}")
    print('-' * 60)

def trip_duration_stats(df):
    """
    Display total and average travel time.
    """
    total_seconds = df['Trip Duration'].sum()
    print(f"Total Travel Time: {total_seconds} seconds ({total_seconds / 3600:.2f} hours)")
    avg_seconds = df['Trip Duration'].mean()
    print(f"Average Travel Time: {avg_seconds:.2f} seconds ({avg_seconds / 3600:.2f} hours)")
    print('-' * 60)

def user_stats(df):
    """
    Display bikeshare user statistics.
    """
    print('\nCalculating User Stats...\n')
    print("User Type Counts:")
    print(df['User Type'].value_counts().to_string())
    if 'Gender' in df:
        print("\nGender Counts:")
        print(df['Gender'].value_counts().to_string())
    if 'Birth Year' in df:
        print("\nBirth Year Statistics:")
        print(f"Earliest: {int(df['Birth Year'].min())}")
        print(f"Most Recent: {int(df['Birth Year'].max())}")
        print(f"Most Common: {int(df['Birth Year'].mode()[0])}")
    print('-' * 60)

def display_raw_data(df):
    """
    Display raw data upon user request.
    """
    row_index = 0
    while row_index < len(df):
        print(df.iloc[row_index: row_index + 5])
        row_index += 5
        if input("\nSee 5 more lines? ('yes' to continue): ").lower() != 'yes':
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
