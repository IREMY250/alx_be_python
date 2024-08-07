from datetime import datetime, timedelta,date

def display_current_datetime():
    current_date=datetime.now()  
    print("current date and time :", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(number_of_days):
     current_date = datetime.now()
     future_date= current_date + timedelta(days=number_of_days)
     print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
def main():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)
if __name__ == "__main__":
    main()