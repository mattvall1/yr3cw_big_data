import networkx
import csv

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

print(social_graph)
