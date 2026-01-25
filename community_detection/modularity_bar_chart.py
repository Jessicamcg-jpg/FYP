import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

full_df = pd.read_csv("General_Election_2020_full.csv")

consti_list = list(full_df["Constituency Name"].unique())
#print(consti_list)
modularity_list = []
for c in consti_list:
    constituency_df = full_df[full_df["Constituency Name"]==c]
    G = graph_of_data(constituency_df)
    communities = nx.community.louvain_communities(G)
    #print(f"Communities produced by Louvain algorithm for {c} dataset:\n")
    #for c in communities:
    #    print(f"{c}\n")
    m = nx.community.modularity(G, communities)
    #print(m)
    modularity_list.append(m)

plt.figure(figsize=(6, 4))
plt.scatter(consti_list, modularity_list, color='red', zorder=5, label='Points')  # Highlight points

plt.xticks(rotation=90)
plt.xlabel("Constituency")
plt.ylabel("Modularity")
plt.title("Modularity in each consituency")
plt.legend()
plt.grid(True)
