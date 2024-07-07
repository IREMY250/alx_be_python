from datetime import datetime, timedelta,date

def display_current_datetime():
    current_date=datetime.now()
    formatted_date=current_date.strftime("%y-%m-%d %H:%M:%S")
    print(f"Current date and time:{formatted_date}")


def calculate_future_date():
    number_of_days= int(input("Enter the number of days to add to the current date:")) 
    delta= datetime.timedelta(days=number_of_days)
    day = datetime.today()
    future_date=delta+day
    result= future_date.strftime("%y-%m-%d %H:%M:%S")
    print(f"Future date:{result}")

display_current_datetime()
calculate_future_date()