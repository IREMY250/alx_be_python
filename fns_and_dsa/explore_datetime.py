from datetime import datetime, timedelta,date

def display_current_datetime():
    date=datetime.now()
    current_date= date.strftime("%y-%m-%d %H:%M:%S")
    print(f"Current date and time:{current_date}")


def calculate_future_date():
    number_of_days= int(input("Enter the number of days to add to the current date:")) 
    duration= datetime.timedelta(days=number_of_days)
    today = datetime.today()
    future_date=duration+today
    print(f"Future date:{future_date}")


display_current_datetime()
calculate_future_date()