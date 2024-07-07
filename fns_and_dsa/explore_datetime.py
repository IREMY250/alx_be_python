from datetime import datetime, timedelta
current_datetime = datetime.now()
print("Current date and time:", current_datetime.strftime("%y-%m-%d %H:%M:%S"))
def calculate_future_date():
     days_to_add = int(input("Enter the number of days to add to the current date:"))
     future_date = current_datetime + timedelta(days=days_to_add)
     result = future_date.strftime("%y-%m-%d %H:%M:%S")
     print("Future date and time:", result)

if __name__ == "__main__":
     calculate_future_date()
