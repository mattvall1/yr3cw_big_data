import networkx
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable

# Initialize a graph
social_graph = networkx.Graph()

# Import nodes (people) from CSV
with open('data/people.csv', 'r') as file:
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        if row_count > 0: # Skip first line (CSV header)
            social_graph.add_node(int(row[0]), name=row[1])
        row_count += 1

# Import edges (friendships) from CSV
with open('data/friendships.csv', 'r') as file:
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        if row_count > 0: # Skip first line (CSV header)
            social_graph.add_edge(int(row[0]), int(row[1]))
        row_count += 1

# Print graph overview
print(social_graph)

# Extract node names
labels = {node: data['name'] for node, data in social_graph.nodes(data=True)}
pos = networkx.spring_layout(social_graph, seed=25, k=0.3)
plt.figure(figsize=(15, 9))
networkx.draw(social_graph, pos, labels=labels, node_size=500, node_color="#80CEFF", edge_color="#FF5733", font_color="#000000", with_labels=True)
plt.axis("off")
plt.savefig("outputs/social_graph.svg", format="svg", transparent=False)
plt.clf()

# Get the diameter of the graph
diameter = networkx.diameter(social_graph)
print("Diameter: " + str(diameter))

# Analyze the degree distribution
# Get degrees of all nodes with their corresponding names (display as a table)
ordered_degrees = sorted([(social_graph.degree(node), social_graph.nodes[node]['name']) for node in social_graph.nodes()], reverse=True)
degree_dict = {}
degree_table = PrettyTable(["Degree", "Names"])
for degree, name in ordered_degrees:
    degree_dict.setdefault(degree, []).append(name)
for degree, names in degree_dict.items():
    degree_table.add_row([degree, ', '.join(names)])
print(degree_table)

# Create degree distribution bar chart
x = ["Degree 1", "Degree 2", "Degree 3", "Degree 4", "Degree 5", "Degree >5"]
y = []
degrees = [social_graph.degree(node) for node in social_graph.nodes()]
# Degrees 1 thru 5
for i in range(5):
    y.append(len([degree for degree in degrees if degree == i+1])/social_graph.number_of_nodes())
# Degrees >5
y.append(len([degree for degree in degrees if degree > 5])/social_graph.number_of_nodes())
plt.bar(x, y, color="#80CEFF")
plt.xlabel("Degree")
plt.ylabel("Percentage of nodes")
plt.title("Degree distribution of the Social Graph")
# Save the degree distribution plot
plt.savefig("outputs/degree_distribution.svg", format="svg", transparent=False)
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

# Analyze clustering coefficient
clustering_coefficient = networkx.clustering(social_graph)
# Plot clustering coefficient
plt.hist(clustering_coefficient.values(), bins=20, color="#01039B")
plt.title("Clustering coefficient histogram")
plt.xlabel("Clustering coefficient")
plt.ylabel("Number of nodes")
# Save the clustering coefficient plot
plt.savefig("outputs/clustering_coefficient.svg", format="svg", transparent=False)

# Plot clustering coefficient CDF
sns.ecdfplot(x=networkx.clustering(social_graph).values())
plt.title("Clustering Coefficient CDF", fontdict={"size": 15}, loc="center")
plt.xlabel("Clustering Coefficient", fontdict={"size": 10})
plt.ylabel("proportion", fontdict={"size": 10})
# Save the clustering coefficient CDF plot
plt.savefig("outputs/clustering_coefficient_cdf.svg", format="svg", transparent=False)
# Clear the plot
plt.clf()







