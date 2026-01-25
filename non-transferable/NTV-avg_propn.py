import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def all_counts_bar_chart(ct_lst, vals_lst):
    """
    Plots a plt bar chart of count vs non-transferable votes.
    """
    plt.figure(figsize=(10, 5))
    plt.ylim(0,0.035)
    
    bars = plt.bar(ct_lst, vals_lst, color='skyblue',width=0.4,align = "center")
    
    plt.title(f'National Per Count Avg of Non-transferable Votes as Proportions of Valid Poll')
    plt.xlabel('Count')
    plt.ylabel('Proportion')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .001, yval)
    
    #save_results_to = "C:/Users/22358313/Desktop/University/BSc Fourth Year/FYP/figures/non_transfer-bar_charts-labels/"
    #file_name = "national-avg-cumul-non-t"
    #plt.savefig(save_results_to + file_name)
    plt.show()

def national_avg_propn_per_count(df):

    """
    At each count, for the active constituencies, computes the average of the proportions (non-transferable votes as a proportion of valid poll).
    Computes a cumulative average proportion of each count, nationally.
    Plots a bar chart.
    """
  
    count_lst = list(df["Count Number"].unique())
    
    propn_lst = []
    avg_propn = 0
    
    for count in count_lst:
        
        count_df = df[df["Count Number"]==count]
        
        consti_list = list(count_df["Constituency Name"].unique())
        
        total_propn = 0
        
        for c in consti_list:
            
            consti_df = count_df[count_df["Constituency Name"]==c]
            valid_c = consti_df["Valid Poll"].iloc[0]
            non_t = -(np.sum(list(consti_df["Transfers"].values)))
            propn = non_t/valid_c
            
            total_propn +=propn
        avg_propn += total_propn/len(consti_list)
        
        propn_lst.append(round(avg_propn,3))
        
    all_counts_bar_chart(count_lst, propn_lst)
    
