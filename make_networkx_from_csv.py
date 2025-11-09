### make_networkx_from_csv.py
# DM and JMcG 30 Oct 2025

def graph_of_data(df):
    #--Merge these columns, will be labels of the nodes
    df["Name"] = df["Candidate surname"].astype("str") +" " + df["Candidate First Name"].astype("str")
    #--Create the DiGraph
    G = nx.DiGraph()
    count_lst = list(df["Count Number"].unique())
    count_lst.remove(1)
    #--Filter by count
    for count in count_lst:
        filtered_df1 = df[df["Count Number"]==count]
        #--get names of those whose votes are transferred
        src_cands = filtered_df1[filtered_df1["Transfers"]<0]
        #--get names of those who receive these transfers
        to_cands =filtered_df1[filtered_df1["Transfers"]>0]
        src_names = list(src_cands["Name"].values)
        to_names = list(to_cands["Name"].values)

        #--add edge weights as the proportion of the src_cand's transfers the to_cand received.       
        wgts = []
        src_wgts = list(src_cands["Transfers"].values)
        to_wgts = list(to_cands["Transfers"].values)

        #--if there's more than one src_cand per count, measure the importance of the edge against the average of the src_cand's transfers
        total=0
        for src_wgt in src_wgts:
            total+=src_wgt
        total=np.abs(total)/len(src_wgts)

        for i in range(len(to_wgts)):
            proportion = to_wgts[i] / total
            wgts.append(round(proportion,2))
            
        #--Create a weighted edge between each source candidate and each target candidate
        for i in range(len(src_names)):
            for j in range(len(to_names)):
                G.add_edge(src_names[i],to_names[j],weight=wgts[j])
    return G

def plot_G(G):
    #--Draw the graph
    plt.figure(figsize=(12, 12))
    #pos = nx.spring_layout(G, seed=42,k=1, iterations=100)
    #pos=nx.get_node_attributes(G,'pos')
    opts = {"with_labels":True,"node_size":600}
    nx.draw_circular(G,**opts)

    #nx.draw_networkx_labels(G, label_pos, font_size=10, font_color='black')
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=edge_labels)
    plt.title("Vote Transfers Graph")
    plt.savefig("filename1.png")
    plt.show()
