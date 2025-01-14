from datetime import datetime 
# Function to display current date
def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}") #Print out current datetime

def calculate_future_date():
    number_of_days = int(input("Enter the number of days: "))
    current_date_time = datetime.datetime.now()
    days = datetime.timedelta(days=number_of_days)

    future_date = current_date_time + days
    future_date = future_date.strftime("%Y-%M-%D %H:%M:%S")
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()



def main():
    while True:
        display_current_datetime()
        calculate_future_date()


if __name__ == "__main__":
    main()