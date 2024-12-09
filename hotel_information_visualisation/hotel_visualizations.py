import csv
import pandas as pd
import datetime
from matplotlib import pyplot as plt

# Read the CSV file into a DataFrame
hotel_data = pd.read_csv('data/hotel_data.csv', parse_dates=['reservation_date'])


# Plot the number of reservations per day on a line chart with relevant averages
# Get a resampled dataset per week
averaged_data_5D = hotel_data.resample('5D', on='reservation_date').mean().reset_index()
average_reservation_count = hotel_data['reservation_count'].mean()

plt.figure(figsize=(25, 5))
plt.plot(hotel_data['reservation_date'], hotel_data['reservation_count'], color="#80CEFF", label="Daily reservations")
plt.gca().set_prop_cycle(None)
plt.plot(averaged_data_5D['reservation_date'], averaged_data_5D['reservation_count'], color="red", linestyle='dashed', label="5-day average")
plt.axhline(y=average_reservation_count, color="#F908D1", linestyle='dashed', label="Overall average")
plt.title('Reservations over time')
plt.xlabel('Date')
plt.ylabel('Number of Reservations')
plt.legend()
plt.subplots_adjust(left=0.03, right=0.99, bottom=0.25)
plt.grid(True)
plt.xticks(hotel_data['reservation_date'][::5], rotation=90)
plt.xlim(hotel_data['reservation_date'].min(), hotel_data['reservation_date'].max()) # Set the x-axis limits to the min and max dates (keeps chart tight)
plt.savefig("outputs/reservations.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()


