import datetime as date

# Function to display current date
def display_current_date():
    current_date = date.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    current_date_time = date.datetime.now()
    days = date.timedelta(days=int(input("Enter the number of days: ")))

    future_date = current_date_time + days
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")

display_current_date()
calculate_future_date()



