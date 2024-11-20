import networkx
import csv
import matplotlib.pyplot as plt

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
plt.savefig("outputs/social_graph.svg", format="svg", transparent=True)
