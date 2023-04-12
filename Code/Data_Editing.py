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
