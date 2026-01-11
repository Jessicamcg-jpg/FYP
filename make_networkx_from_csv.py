def graph_of_data(df):
    """
    Input: an election dataframe for a constitutency.
    Output: a NetworkX weighted digraph representing the transfers between candidates.
    Does this by filtering the inputted dataframe by count, then extracting the values of transfers using Pandas.

    """
    
    #--Merge these columns, will be labels of the nodes
    df["Name"] = df["Candidate surname"].astype("str") +" " + df["Candidate First Name"].astype("str")
    #--Create the DiGraph
    G = nx.DiGraph()
    count_lst = list(df["Count Number"].unique())
    #--There are no transfers on the first count so we will ignore
    count_lst.remove(1)
    #--Filter by count
    for count in count_lst:
        count_df = df[df["Count Number"]==count]
        #--filter by candidates whose votes are transferred
        src_cands = count_df[count_df["Transfers"]<0]
        #--filter by candidates who receive these transfers
        to_cands =count_df[count_df["Transfers"]>0]
        #--get these list of candidates to create the graph below
        src_names = list(src_cands["Name"].values)
        to_names = list(to_cands["Name"].values)

        #--add edge weights as: the amount of votes transferred to a candidate as a proportion of the total votes transferred per count
        src_wgts = list(src_cands["Transfers"].values)
        to_wgts = list(to_cands["Transfers"].values)

            #--if there's more than one src_cand per count, the number of transfers a candidate receives will be
            #--a proportion of this total
        total = np.abs(np.sum(src_wgts))

        wgts = [round(wgt/total, 2) for wgt in to_wgts]
            
        #--Create a weighted edge between each source candidate and each target candidate
        for i in range(len(src_names)):
            for j in range(len(to_names)):
                G.add_edge(src_names[i],to_names[j],weight=wgts[j])
    return G

def plot_G(G):
    """
    Input: a NetworkX weighted DiGraph.
    Each edge in the graph has a 'weight' attribute created in above function, that is used by NetworkX default method get_edge_attributes().
    Output: a circular graph, labelled with transfers between candidates.
    
    """
    
    plt.figure(figsize=(12, 12))
    
    opts = {"with_labels":True,"node_size":600}
    
    nx.draw_circular(G,**opts)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=nx.circular_layout(G), edge_labels=edge_labels)
    
    plt.title("Graph of Transfers between Candidates")
    plt.show()
