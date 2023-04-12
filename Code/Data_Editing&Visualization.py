# -*- coding: utf-8 -*-
# Data_editing


#mounting drive

from google.colab import drive
drive.mount('/content/my_drive')

!pip install langdetect
!pip install regex

import pandas as pd
import numpy as np
from langdetect import detect
import regex as re

#Loading the data

tweets_query_1 = pd.read_csv("my_drive/MyDrive/twitter/data/Safe/Query_1_data.csv")
tweets_query_1b = pd.read_csv("my_drive/MyDrive/twitter/data/Query_1b_data.csv")
tweets_query_1c = pd.read_csv("my_drive/MyDrive/twitter/data/Query_1c_data.csv")
tweets_query_2 = pd.read_csv("my_drive/MyDrive/twitter/data/Query_2_data.csv")
tweets_query_3 = pd.read_csv("my_drive/MyDrive/twitter/data/Query_3_data.csv")
tweets_query_4 = pd.read_csv("my_drive/MyDrive/twitter/data/Query_4_data.csv")

# Concatenating the datasets

tweets_conca = pd.concat([tweets_query_1,tweets_query_1b,tweets_query_1c,tweets_query_2,tweets_query_3,tweets_query_4], axis=0)

#Did it work? 
tweets_conca

#Dropping dublicates and comparing the lenghs of the dataset before and after to see whether it worked
len(tweets_conca)
tweets_conca.drop_duplicates(subset=['text'], inplace=True)
len(tweets_conca)

#export as csv
tweets_conca.to_csv('./my_drive/MyDrive/twitter/data/total_tweets_-duplicate.csv')

##Dropping the tweets that have less then 5 retweets

#Define the condition for dropping rows
condition = (tweets_conca['retweet_count'] < 5)

# Filter the DataFrame based on the condition
total_tweets_filtered = tweets_conca[condition]

# Drop the rows from the original DataFrame
total_conca_rel = tweets_conca.drop(total_tweets_filtered.index)

len(total_conca_rel)

#export as csv
total_conca_rel.to_csv('./my_drive/MyDrive/twitter/data/total_tweets_final.csv')

#cleaning the data from: other languages, etc.

total_conca_rel["text"].replace('\n', " ",regex=True, inplace=True) # replacing line breaks
language = []
for i in total_conca_rel.text: #tja das musst du mir mal nochmal erklären
  try:
    lang = detect(i)
    language.append(lang)
  except:
    langNaN = np.NaN
    language.append(langNaN)
    
total_conca_rel["lang"] = language
total_conca_rel_clean = total_conca_rel.loc[total_conca_rel["lang"] == "de"]

"""For work with the classifier, some more cleaning is done, as the classifier does not seem to handle tweets with large urls or many special characters very well. Some relevant special characters are kept as they seem relevant for the classification."""

ds = total_conca_rel_clean

# Replace relevant special characters
replacements = {"🇷🇺":" RUflag ", "🇺🇦":" UAflag ", "🇩🇪":" DEflag "}
ds['text_clean'] = ds['text'].str.replace("|".join(replacements.keys()), lambda m: replacements[m.group()], regex=True)

# Set text to lower-case
ds["text_clean"] = ds["text_clean"].str.lower()

# Remove URLs
ds['text_clean'] = ds['text_clean'].str.replace(r'http(\S)+', r'')
ds['text_clean'] = ds['text_clean'].str.replace(r'http ...', r'')
ds['text_clean'] = ds['text_clean'].str.replace(r'http', r'')
ds[ds['text_clean'].str.contains(r'http')]

# Remove retweets, @
ds['text_clean'] = ds['text_clean'].str.replace(r'(RT|rt)[ ]*@[ ]*[\S]+',r'')
ds[ds['text_clean'].str.contains(r'RT[ ]?@')]
ds['text_clean'] = ds['text_clean'].str.replace(r'@[\S]+',r'')

# Remove non-ascii words and characters
ds['text_clean'] = ds["text_clean"].astype(str).apply(lambda x: re.sub('[^a-zA-ZäöüÄÖÜß#]', ' ', x))

#  Remove unnecessary white spaces
ds['text_clean'] = ds['text_clean'].str.replace("  "," ")
ds['text_clean'] = ds['text_clean'].str.strip()

# Test the results
ds[["text_clean"]].values

"""## Export for annotation"""

#getting tweets for annotation
tweets_for_annotation = ds.iloc[::35] # takes every 35th tweet from the dataset over the whole time span

# checking
len(tweets_for_annotation)

#export as csv
tweets_for_annotation.to_csv('./my_drive/MyDrive/twitter/data/tweets_for_annotation.csv')

"""## Create Visualization of the saliency over time in the BT, on Twitter and compare them with actual policy changes"""

# Import qualitatively created List of BRT 
ds_d = pd.read_excel("/content/drive/MyDrive/decision_timeline.xlsx")
# Reimport Bundestag data
ds_b = pd.read_excel("/content/drive/MyDrive/BT_final.xlsx")
# Reimport the final twitter data
ds_t = pd.read_excel("//content/drive/MyDrive/final_t.xlsx")

# Normalizing twitter and BT data to be able to plot it in the same graph
normalized_t=(ds_t["count"]-ds_t["count"].min())/(ds_t["count"].max()-ds_t["count"].min())
ds_t["count"] = normalized_t

normalized_b=(ds_b["sum"]-ds_b["sum"].min())/(ds_b["sum"].max()-ds_b["sum"].min())
ds_b["sum"] = normalized_b

# Create Datetime values
ds_d.date = pd.to_datetime(ds_d.date)
ds_b.date = pd.to_datetime(ds_b.date)
ds_t.date = pd.to_datetime(ds_t.date)

# Create graph
plt.figure(figsize=(13,5))
plt.xlabel("Date")
plt.ylabel("Salience")
plt.title("German Weapons Deliveries and Saliency in Discussion, Bundestag and Twitter")
plt.xticks(ds_d.date, ds_d.event, rotation=90)
sns.lineplot(x=ds_b.date, y=ds_b["sum"], color="indianred")
sns.lineplot(x=ds_t.date, y= ds_t["count"])
plt.grid(axis="x", lw=4, alpha=0.2)
plt.show()

# Export in high Quality
plt.savefig("/mnt/ramdisk/bundestag_gaph.png", dpi=300, bbox_inches='tight')
