# -*- coding: utf-8 -*-


# Import dependencies
import pandas as pd
import random
from google.colab import drive
drive.mount('/content/my_drive')


## Classification with XLMRoberta

#Uninstalling the current torch version and numpy version to install the most recent ones, since this apparently caused an error we got when running the model. 
!pip uninstall torch torchvision torchaudio sympy tensorflow torchtext fastai --yes
!pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu --ignore-installed
!pip uninstall numpy --yes
!pip install "numpy == 1.15.0"

#getting and installing the AugmentedSocialScientist package
!git clone https://github.com/rubingshen/AugmentedSocialScientist.git
!pip install ./AugmentedSocialScientist/package/

import pandas as pd
import numpy as np
import torch

from AugmentedSocialScientist import xlmroberta

#load our data
tweets = pd.read_csv("/content/my_drive/MyDrive/tweets_annoted.csv")
tweets.loc[tweets["annotation"]  == 99] = 2

#change to int and str
tweets['text'] = tweets['text'].astype(str)
tweets['annotation'] = tweets['annotation'].astype(int)

#shuffle rows 
tweets=tweets.sample(frac=1)

#separate the data in two sets: training (80%) and testing data (20%)
tweets['set']=['training']*int(len(tweets)*.8) + ['testing']*(len(tweets)-int(len(tweets)*.8))

tweets_training=tweets[tweets['set']=='training']
tweets_testing=tweets[tweets['set']=='testing']

training_loader = xlmroberta.encode(tweets_training.text.values, tweets_training.annotation.values)
testing_loader = xlmroberta.encode(tweets_testing.text.values, tweets_testing.annotation.values)

#import torch, setting the runtime on cpu instead of gpu
#device = torch.device("cpu")
#import tensorflow
#with tensorflow.device('/cpu:0'):

# Validation of the performance
score = xlmroberta.run_training(training_loader, 
                          testing_loader, 
                          n_epochs=2, 
                          lr=5e-5, 
                          seed_val=42,
                          save_model_as='tweets')
# -> result worse than expected


## Classification attempt with German-Sentiment-Bert

!pip install transformers
from transformers import pipeline
classifier_s = pipeline("text-classification", "oliverguhr/german-sentiment-bert")

# df = pd.read_csv("/content/my_drive/MyDrive/DDPS-Project (1)/twitter/data/annotated/annotated_concat_final.csv")
# df["text_clean"].head(10).values


random.seed(123)
df_sample = df.sample(200)

a = []
for i in df_sample["text"]:
  a.append(classifier_s(i))

df_sample["predict"] = a
df_sample


## Classification attempt with model pretrained on German Twitter data
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

model_name = "joh-ga/german-tweetstance-bert-uncased-russiaukrainewar"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)


# Create Training df
training_df = df[["annotation","text_clean"]]

#this will shuffle rows 
training_df=training_df.sample(frac=1)

#let's separate the data in two sets: training (80%) and testing data (20%)
training_df['set']=['train']*int(len(df)*.8) + ['test']*(len(df)-int(len(df)*.8))

# Tokenize the dataset
model_name = "joh-ga/german-tweetstance-bert-uncased-russiaukrainewar"
tokenizer = AutoTokenizer.from_pretrained(model_name)
def tokenize_function(examples):
    return tokenizer(examples["text_clean"], padding="max_length", truncation=True)

tokenized_datasets = training_df.map(tokenize_function, batched=True)

# Create tokenized training and evaluation data set
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(1000

# Training hyperparameters
from transformers import TrainingArguments
training_args = TrainingArguments(output_dir="test_trainer")

# Define metrics function
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=training_df.loc[training_df["set"] == "train],
    eval_dataset=training_df.loc[training_df["set"] == "test],
    compute_metrics=compute_metrics,
)
trainer.train()

!pip install evaluate
import numpy as np
import evaluate

metric = evaluate.load("accuracy")

import random
import pandas as pd
random.seed(321)
sample_df = df.sample(30)
a = []
for i in sample_df["text"]:
  a.append((i))

sample_df["predicton"] = a
test[["text_clean","annotation","predicton"]]

training_df = df[["text_clean", "annotation"]]
training_df

