import time
import pandas as pd
import numpy as np

# Dictionary mapping city names to data files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def choose_city():
    """
    Asks the user to select a city for analysis.
    Returns:
        str: Name of the city to analyze.
    """
    while True:
        print("\nChoose a city to analyze:")
        print("1. Chicago")
        print("2. New York City")
        print("3. Washington")
        choice = input("Enter the number corresponding to your choice: ").strip()
        
        if choice == '1':
            return 'chicago'
        elif choice == '2':
            return 'new york city'
        elif choice == '3':
            return 'washington'
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def load_data(city):
    """
    Loads bikeshare data for the specified city into a Pandas DataFrame.
    Args:
        city (str): The name of the city.
    Returns:
        DataFrame: Data for the selected city.
    """
    return pd.read_csv(CITY_DATA[city])

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    # Ensure 'Start Time' is in datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"Most Common Month: {most_common_month} ({months[most_common_month - 1]})")
    
    # Most common day of the week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f"Most Common Day of the Week: {most_common_day}")
    
    # Most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    
    # Categorizing the hour into time of day
    time_of_day = "Morning" if most_common_hour < 12 else "Afternoon" if most_common_hour < 17 else "Evening"
    print(f"Most Common Start Hour: {most_common_hour} ({time_of_day})")
    print('-' * 60)

def station_stats(df):
    """
    Displays statistics on the most popular start and end stations, as well as the most frequent trip.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    print(f"Most Common Start Station: {df['Start Station'].mode()[0]}")
    print(f"Most Common End Station: {df['End Station'].mode()[0]}")
    
    df['Trip Route'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most Common Trip: {df['Trip Route'].mode()[0]}")
    print('-' * 60)

def trip_duration_stats(df):
    """
    Displays statistics on trip durations, including total and average duration.
    """
    total_travel_time = df['Trip Duration'].sum()
    average_travel_time = df['Trip Duration'].mean()
    
    print(f"Total Travel Time: {total_travel_time} seconds ({total_travel_time / 3600:.2f} hours)")
    print(f"Average Travel Time: {average_travel_time:.2f} seconds ({average_travel_time / 3600:.2f} hours)")
    print('-' * 60)

def user_stats(df):
    """
    Displays statistics on bikeshare users, including counts of user types, gender, and birth year data.
    """
    print('\nCalculating User Stats...\n')
    print(df['User Type'].value_counts().to_string())
    
    if 'Gender' in df:
        print("\nGender Distribution:")
        print(df['Gender'].value_counts().to_string())
    else:
        print("\nGender data is not available for this city.")
    
    if 'Birth Year' in df:
        print("\nBirth Year Stats:")
        print(f"Earliest: {int(df['Birth Year'].min())}")
        print(f"Most Recent: {int(df['Birth Year'].max())}")
        print(f"Most Common: {int(df['Birth Year'].mode()[0])}")
    else:
        print("\nBirth year data is not available for this city.")
    print('-' * 60)

def display_raw_data(df):
    """
    Displays raw data in increments of 5 rows upon user request.
    """
    index = 0
    while True:
        print(df.iloc[index: index + 5])
        index += 5
        more_data = input("\nWould you like to see more data? Enter 'yes' or 'no': ").strip().lower()
        if more_data != 'yes':
            break
        if index >= len(df):
            print("\nNo more data to display.")
            break

def main():
    """
    Main function to run the bikeshare analysis program.
    """
    while True:
        city = choose_city()
        df = load_data(city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        
        while True:
            print("\nChoose an analysis:")
            print("1. Popular Times of Travel")
            print("2. Popular Stations and Trip")
            print("3. Trip Duration")
            print("4. User Info")
            print("5. Display Raw Data")
            print("6. Exit to Main Menu")
            
            choice = input("Enter the number corresponding to your choice: ").strip()
            
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
                print("Invalid choice. Please select a valid option.")

        restart = input("\nWould you like to restart the program? Enter 'yes' or 'no': ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
