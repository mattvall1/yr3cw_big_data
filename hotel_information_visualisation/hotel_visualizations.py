import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from math import ceil

# Read the CSV file into a DataFrame
hotel_data = pd.read_csv('data/hotel_data.csv', parse_dates=['reservation_date'])

# Seaborn plots - To discover correlations within the data (Not used within report)
seaborn_pairs = sns.pairplot(hotel_data)
seaborn_pairs.savefig("outputs/seaborn_pairplot.svg", format="svg", transparent=False)


# Plot the number of reservations per day on a line chart with relevant averages
# Get a resampled dataset per week
averaged_data_5D = hotel_data.resample('5D', on='reservation_date').mean().reset_index()
average_reservation_count = hotel_data['reservation_count'].mean()

plt.figure(figsize=(25, 5), tight_layout=True)
plt.plot(hotel_data['reservation_date'], hotel_data['reservation_count'], color="#80CEFF", label="Daily reservations")
plt.gca().set_prop_cycle(None)
plt.plot(averaged_data_5D['reservation_date'], averaged_data_5D['reservation_count'], color="red", linestyle='dashed', label="5-day average")
plt.axhline(y=average_reservation_count, color="#F908D1", linestyle='dashed', label="Overall average")
plt.title('Reservations over time', fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Number of Reservations', fontsize=15)
plt.legend(fontsize=15)
plt.grid(True)
plt.xticks(hotel_data['reservation_date'][::5], rotation=90)
plt.xlim(hotel_data['reservation_date'].min(), hotel_data['reservation_date'].max()) # Set the x-axis limits to the min and max dates (keeps chart tight)
plt.savefig("outputs/reservations.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Plot a pie chart of the number of adults and children in the dataset
labels = ['Adults', 'Children']
sizes = [hotel_data['adults'].sum(), hotel_data['children'].sum()]
colors = ['#80CEFF', '#ACFF80']
plt.figure(figsize=(5, 5), tight_layout=True)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90)
plt.axis('equal')
plt.title('Proportion of adults to children')
plt.savefig("outputs/adults_vs_children.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Create a scatter plot of total special requests against the total number of children
plt.figure(figsize=(5, 5), tight_layout=True)
plt.scatter(hotel_data['children'], hotel_data['total_of_special_requests'], color="#ACFF80", zorder=2)
plt.title('Impact of number of children on special requests')
plt.xlabel('Total children')
plt.ylabel('Total special requests')
plt.grid(True, zorder=0)
plt.savefig("outputs/special_requests_vs_children.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Create a scatter plot of special requests against booking changes
plt.figure(figsize=(5, 5), tight_layout=True)
plt.scatter(hotel_data['total_of_special_requests'], hotel_data['booking_changes'], color="#FF80FF", zorder=2)
plt.title('Impact of booking changes on special requests')
plt.ylabel('Total booking changes')
plt.xlabel('Total special requests')
plt.grid(True, zorder=0)
plt.savefig("outputs/special_requests_vs_booking_changes.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Create a bar chart with the distributions (groups of 25) of the reservations
# Group data into bins of 25
maximum_group = int(ceil(hotel_data['reservation_count'].max() / 25) * 25 + 1) # Get maximum group value and round up to the nearest 25
labels = [f'{i}-{i+25}' for i in range(0, maximum_group-25, 25)] # Create sensible labels for the groups
grouped_data = hotel_data.groupby(pd.cut(hotel_data['reservation_count'], bins=range(0, maximum_group, 25), labels=labels), observed=False).size()

plt.figure(figsize=(10, 5), tight_layout=True)
grouped_data.plot(kind='bar', color="#80CEFF", zorder=2)
plt.title('Distribution of reservations')
plt.xlabel('Number of reservations')
plt.ylabel('Number of days')
plt.xticks(rotation=0)
plt.grid(True, zorder=0)
plt.savefig("outputs/reservation_distribution.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

