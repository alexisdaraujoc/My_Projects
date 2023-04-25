from datetime import date
from nsepy import get_history

# Define the start and end dates for the historical data
start_date = date(2023, 1, 1)
end_date = date(2023, 1, 6)

# Retrive historical data for a particular company
company = input("Enter Stock Name: ")
data = get_history(company, start=start_date, end=end_date)

# Print the first few rows of data
print(data.head())


