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
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month (number and name)
    most_common_month = df['Start Time'].dt.month.mode()[0]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"Most Common Month: {most_common_month} ({months[most_common_month - 1]})")

    # Display the most common day of the week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f"Most Common Day of Week: {most_common_day}")

    # Display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    
    # Categorize the time of day
    if most_common_hour < 12:
        time_of_day = "Morning"
    elif most_common_hour == 12:
        time_of_day = "Noon"
    elif most_common_hour < 17:
        time_of_day = "Afternoon"
    else:
        time_of_day = "Evening"
    
    print(f"Most Common Start Hour: {most_common_hour} ({time_of_day})")
  
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    

    # Most common start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most Common Start Station: {most_common_start_station}")

    # Most common end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most Common End Station: {most_common_end_station}")

    # Most frequent combination of start and end stations
    df['start_to_end'] = df['Start Station'] + " to " + df['End Station']
    most_common_trip = df['start_to_end'].mode()[0]
    print(f"Most Common Trip: {most_common_trip}")

    print('-' * 60)

# Calculate trip duration statistics
def trip_duration_stats(df):
    """
    Calculate and print total travel time and average travel time in seconds and hours.
    """
    # Total travel time in seconds
    total_travel_time_seconds = df['Trip Duration'].sum()
    total_travel_time_hours = total_travel_time_seconds / 3600
    
    # Average travel time in seconds
    average_travel_time_seconds = df['Trip Duration'].mean()
    average_travel_time_hours = average_travel_time_seconds / 3600
    
    print(f"Total Travel Time: {total_travel_time_seconds} seconds ({total_travel_time_hours:.2f} hours)")
    print(f"Average Travel Time: {average_travel_time_seconds:.2f} seconds ({average_travel_time_hours:.2f} hours)")
    print('-' * 60)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')

    # Counts of user types 
    print("Counts of each user type:")
    print("User Type      Counts")
    user_types = df['User Type'].value_counts()
    for user_type, count in user_types.items():
        print(f"{user_type:<15}{count}")
    print()

    # Gender counts
    if 'Gender' in df:
        print("Counts of each gender :")
        print("Gender         Counts")
        gender_counts = df['Gender'].value_counts()
        for gender, count in gender_counts.items():
            print(f"{gender:<15}{count}")
        print()
    else:
        print("Gender data is not available for this city.\n")

    # Birth year statistics
    if 'Birth Year' in df:
        print("Birth Year Statistics:")
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest Birth Year: {earliest_birth_year}")
        print(f"Most Recent Birth Year: {most_recent_birth_year}")
        print(f"Most Common Birth Year: {most_common_birth_year}")
    else:
        print("Birth year data is not available for this city.")

    print('-' * 60)


def display_raw_data(df):
    """Displays 5 lines of raw data at a time based on user input."""
    row_index = 0
    while True:
        # Show next 5 rows
        print(df.iloc[row_index: row_index + 5])
        row_index += 5

        # Ask user if they want to see more data
        more_data = input("\nDo you want to see 5 more lines of raw data? Enter 'yes' or 'no': ").lower()
        if more_data != 'yes':
            break
        if row_index >= len(df):
            print("\nNo more data to display.")
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
