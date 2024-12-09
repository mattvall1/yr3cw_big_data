import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.pyplot import tight_layout

# Read the CSV file into a DataFrame
hotel_data = pd.read_csv('data/hotel_data.csv', parse_dates=['reservation_date'])

# Seaborn plots - To discover correlations within the data (Not used within report)
seaborn_pairs = sns.pairplot(hotel_data)
seaborn_pairs.savefig("outputs/seaborn_pairplot.svg", format="svg", transparent=False)


# Plot the number of reservations per day on a line chart with relevant averages
# Get a resampled dataset per week
averaged_data_5D = hotel_data.resample('5D', on='reservation_date').mean().reset_index()
average_reservation_count = hotel_data['reservation_count'].mean()

plt.figure(figsize=(25, 5))
plt.plot(hotel_data['reservation_date'], hotel_data['reservation_count'], color="#80CEFF", label="Daily reservations")
plt.gca().set_prop_cycle(None)
plt.plot(averaged_data_5D['reservation_date'], averaged_data_5D['reservation_count'], color="red", linestyle='dashed', label="5-day average")
plt.axhline(y=average_reservation_count, color="#F908D1", linestyle='dashed', label="Overall average")
plt.title('Reservations over time', fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Number of Reservations', fontsize=15)
plt.legend(fontsize=15)
plt.subplots_adjust(left=0.03, right=0.99, bottom=0.25)
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


