#--File summary:
#summarise num counts in each constituency; 
#produce bar charts of constituencies having each num counts; 
#calculate most common number of counts

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

full_df = pd.read_csv("General_Election_2020_full.csv")

#--create a dataframe summary of num counts and num candidates
result_df = (
    full_df.groupby("Constituency Name")["Count Number"]
    .max()
    .reset_index()
    .rename(columns={"Count Number": "Num Counts"})
)
candidate_counts = (
    full_df.groupby("Constituency Name")["Candidate surname"]
    .nunique()
    .reset_index()
    .rename(columns={"Candidate surname": "Num Candidates"})
)
result_df = result_df.merge(candidate_counts, on="Constituency Name")

result_df=result_df.sort_values(by="Num Counts", ascending=True)
result_df

####

def all_counts_bar_chart(ct_lst, vals_lst, count):
    
    plt.figure(figsize=(10, 5))
    plt.ylim(0,0.035)
    
    bars = plt.bar(ct_lst, vals_lst, color='skyblue',width=0.4,align = "center")
    
    plt.title(f'Non-transferable Votes As A Proportion of Valid Poll for Count {count}')
    plt.xlabel('Count')
    plt.ylabel('Proportion')
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x(), yval + .001, yval)
    
    #save_results_to = "C:/Users/22358313/Desktop/University/4th_Year/FYP/figures/non_transfer-bar_charts-labels/"
    #file_name = f"NTV-{count}_counts"
    #plt.savefig(save_results_to + file_name)
    plt.show()

def non_cumul_propn_per_count(df, count):
    propn_lst = []
    propn=0
    for ct in range(1,count+1):
        
        count_df = df[df["Count Number"]==ct]
        total_valid_per_count = sum(list(count_df["Valid Poll"].unique()))
        print(total_valid_per_count)
        total_non_t_per_count = -(np.sum(list(count_df["Transfers"].values)))
        propn = total_non_t_per_count/total_valid_per_count

        propn_lst.append(round(propn,6))
    print(propn_lst)
    all_counts_bar_chart(list(range(1,count+1)),propn_lst, count)

#--produce bar chart for counts only lasting 8 counts
def filter_by_count(count):
    consti_selected=list(result_df[result_df["Num Counts"]==count]["Constituency Name"].values)
    print(consti_selected)
    filtered_df = full_df.loc[full_df["Constituency Name"].isin(consti_selected)]
    non_cumul_propn_per_count(filtered_df, count)
#call function
filter_by_count(8)

#--constituencies and how long each election was (in lists for later use)
f_df = (result_df[result_df["Num Counts"]==9])
print(list(f_df["Constituency Name"].values))
constituencies_9 = ['Dublin Mid West', 'Dublin Central', 'Donegal', 'Tipperary', 'Limerick City']
constituencies_10 = ['Longford Westmeath', 'Louth', 'Carlow-Kilkenny', 'Clare']
constituencies_11 = ['Wexford', 'Dublin South West', 'Cavan-Monaghan', 'Laois Offaly']
constituencies_12 = ['Dublin Fingal']
constituencies_13 = ['Galway West']
constituencies_14 = ['Dublin Bay North', 'Cork North Central']
constituencies_15 = ['Sligo Leitrim', 'Wicklow']

#most common number of counts
st.multimode(result_df["Num Counts"].values.tolist())
