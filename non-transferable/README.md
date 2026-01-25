# Study of non-transferable votes

Purpose:
To develop a model that predicts the result of an election (i.e. predict where votes go), we need to know what 'amount' of votes become non-transferable as the election progresses.

File contains:
- avg_propn_per_count.py : calculate the normalised proportion of non-transferables of each active constituency and take average, at each count. cumulative.
- non_cumul_propn.py : treat the valid polls of each constituency as one big valid poll, at each count.
- . Contains implementation for analysing national and constituency-level trend.
- summarise_by_count.py : program to produce a dataframe and bar charts summarising trends, by count.
