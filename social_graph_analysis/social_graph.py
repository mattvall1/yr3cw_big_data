import networkx
import csv
import matplotlib.pyplot as plt
import numpy as np

# Initialize a graph
social_graph = networkx.Graph()

# Import nodes (people) from CSV
with open('data/people.csv', 'r') as file:
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        if row_count > 1: # Skip first line (CSV header)
            social_graph.add_node(int(row[0]), name=row[1])
        row_count += 1

# Import edges (friendships) from CSV
with open('data/friendships.csv', 'r') as file:
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        if row_count > 1: # Skip first line (CSV header)
            social_graph.add_edge(int(row[0]), int(row[1]))
        row_count += 1

# Print graph overview
print(social_graph)

# Create overview visualisation of the graph
pos = networkx.spring_layout(social_graph, iterations=50, seed=4)
fig, ax = plt.subplots(figsize=(15, 9))
plot_options = {"node_size": 500, "with_labels": True, "width": 1, "node_color": "#01039B", "font_color": "#FFFFFF"}
ax.axis("off")
networkx.draw_networkx(social_graph, pos=pos, ax=ax, **plot_options)
plt.savefig("outputs/social_graph.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Create degree distribution of the graph
x = ["Degree 1", "Degree 2", "Degree 3", "Degree 4", "Degree 5", "Degree >5"]
y = []
degrees = [social_graph.degree(node) for node in social_graph.nodes()]
# Degrees 1 thru 5
for i in range(1, 6):
    y.append(len([degree for degree in degrees if degree == i])/social_graph.number_of_nodes())
# Degrees >5
y.append(len([degree for degree in degrees if degree > 5])/social_graph.number_of_nodes())
plt.bar(x, y, color="#01039B")
plt.xlabel("Degree")
plt.ylabel("Percentage of nodes")
plt.title("Degree distribution of the social graph")
# Save the degree distribution plot
plt.savefig("outputs/degree_distribution.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Analyze betweenness centrality
betweenness_centrality = networkx.betweenness_centrality(social_graph)
# Plot betweenness centrality
plt.hist(betweenness_centrality.values(), bins=100, color="#01039B")
plt.title("Betweenness centrality histogram")
plt.xlabel("Betweenness centrality")
plt.ylabel("Number of nodes")
# Save the betweenness centrality plot
plt.savefig("outputs/betweenness_centrality.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()

# Analyze closeness centrality
closeness_centrality = networkx.closeness_centrality(social_graph)
# Plot closeness centrality
plt.hist(closeness_centrality.values(), bins=100, color="#01039B")
plt.title("Closeness centrality histogram")
plt.xlabel("Closeness centrality")
plt.ylabel("Number of nodes")
# Save the closeness centrality plot
plt.savefig("outputs/closeness_centrality.svg", format="svg", transparent=False)








