from graphviz import Digraph
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
import textwrap


def wrap_labels(labels, width=20):
    return ['\n'.join(textwrap.wrap(label, width)) for label in labels]

dot = Digraph(comment='PERT Analyse IT Transitie', graph_attr={'rankdir': 'LR', 'ranksep': '1', 'nodesep': '1'})

# Nodes
dot.node('A', 'Start - A')
dot.node('B', 'Ontmantelen oude servers - B')
dot.node('C', 'Nieuwe servers in datacenter - C')
dot.node('D', 'Veilige datamigratie - D')
dot.node('E', 'Vernieuwing laptops/pc’s - E')
dot.node('F', 'Aankoop tablets dienstvoertuigen - F')
dot.node('G', 'VoIP-implementatie - G')
dot.node('H', 'Vernieuwing/leasing netwerk - H')
dot.node('I', 'Migratie Gmail -> Office 365 - I')
dot.node('J', 'Security maatregelen (MFA, encryptie) - J')
dot.node('K', 'Beveiligingsaudits & pentesten - K')

# Edges with durations
dot.edge('A', 'B')
dot.edge('A', 'E')
dot.edge('A', 'F')
dot.edge('A', 'H')
dot.edge('B', 'C', label='1 maand')
dot.edge('C', 'D', label='2 maanden')
dot.edge('D', 'I', label='3 maanden')
dot.edge('E', 'G', label='2 maanden')
dot.edge('F', 'G', label='1 maand')
dot.edge('H', 'G', label='3 maanden')
dot.edge('G', 'J', label='2 maanden')
dot.edge('I', 'J', label='2 maanden')
dot.edge('J', 'K', label='1 maand')

dot.render('pert_analyse', format='png', cleanup=False)

# Gantt Chart (max 12 maanden)

data = {
    'Task': [
        'Ontmantelen oude servers - A',
        'Nieuwe servers in datacenter - B',
        'Veilige datamigratie - C',
        'Vernieuwing laptops/pc’s - D',
        'Aankoop tablets dienstvoertuigen - E',
        'VoIP-implementatie - F',
        'Vernieuwing/leasing netwerk - G',
        'Migratie Gmail -> Office 365 - H',
        'Security maatregelen (MFA, encryptie) - I',
        'Beveiligingsaudits & pentesten - J'
    ],
    'Start': [0, 1, 3, 2, 4, 5, 3, 5, 7, 9],
    'Duration': [1, 2, 2, 1, 1, 2, 2, 2, 2, 1]
}

df = pd.DataFrame(data)

def plot_gantt(df):
    fig, ax = plt.subplots(figsize=(16, 6))
    y_labels = np.arange(len(df))
    ax.barh(y_labels, df['Duration'], left=df['Start'], color='skyblue')
    ax.set_yticks(y_labels)

    df['Wrapped Task'] = wrap_labels(df['Task'])  # Pas de labels aan
    ax.set_yticklabels(df['Wrapped Task'])  # Gebruik de aangepaste labels
    
    ax.set_xlabel('Tijd (maanden)')
    ax.set_title('Gantt Chart IT Transitie (max 12 maanden)')
    plt.xticks([0, 3, 6, 9, 12], ['Start', '3', '6', '9', '12'])
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

plot_gantt(df)

# Kritieke pad analyse
G = nx.DiGraph()

tasks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
durations = [1, 2, 2, 1, 1, 2, 2, 2, 2, 1]
edges = [('A', 'B', 1), ('B', 'C', 2), ('C', 'I', 2), ('C', 'H', 2), ('D', 'F', 1), ('E', 'F', 1), ('G', 'F', 2), ('F', 'I', 2), ('H', 'I', 2), ('I', 'J', 1)]

for task, duration in zip(tasks, durations):
    G.add_node(task, duration=duration)

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

critical_path = nx.dag_longest_path(G, weight='weight')
print("Kritieke pad:", ' -> '.join(critical_path))