import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def all_counts_bar_chart(ct_lst, vals_lst):
    """
    Prints a plt bar chart with labels above each bar.
    """
    plt.figure(figsize=(10, 5))
    plt.ylim(0,0.035)
    
    bars = plt.bar(ct_lst, vals_lst, color='skyblue',width=0.4,align = "center")
    
    plt.title(f'Non-transferable Votes As A Proportion of Valid Poll Per Count')
    plt.xlabel('Count')
    plt.ylabel('Proportion')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .001, yval)
    
    #save_results_to = "C:/Users/22358313/Desktop/University/4th_Year/FYP/figures/non_transfer-bar_charts-labels/"
    #file_name = "national-non-t-per-count"
    #plt.savefig(save_results_to + file_name)
    plt.show()
  
def non_cumul_propn_per_count(df):

    """
    Calculates the proportion of non-transferable votes at each count by pooling the non-transferable votes and valid votes of each active constituency at that count 
    and calculating the pooled NTVs as a proportion of the pooled valid poll.
    Iteratively filters the full election CSV by count; sums over the "Valid Poll" column and "Transfers" column.
    """
    
    propn_lst = []
    for count in range(1,16):
        
        count_df = df[df["Count Number"]==count]
        total_valid_per_count = sum(list(count_df["Valid Poll"].unique()))
        total_non_t_per_count = -(np.sum(list(count_df["Transfers"].values)))
        propn = total_non_t_per_count/total_valid_per_count

        propn_lst.append(round(propn,3))
        
    all_counts_bar_chart(list(range(1,16)),propn_lst)

#--IMPLEMENTATION

#--national trend
full_df = pd.read_csv("General_Election_2020_full.csv")
non_cumul_propn_per_count(full_df)

#--constituency trend
constituency = "Cavan-Monaghan"
constituency_df = full_df.loc[full_df["Constituency Name"]==constituency]

non_cumul_propn_per_count(constituency_df, constituency)
