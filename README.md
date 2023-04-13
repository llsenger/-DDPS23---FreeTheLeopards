![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/9481ad2e00e5ba94bc5fac17fa77833bd6ec2dfa/%23freetheleopards_image.png?raw=true)

***The Discourse Around the Shift of  Germany’s Arms Supply Policy***

_April 13, 2023_

This repository summarizes the findings and provides the code of our project for the CIVICA course "Diving in the Digital Public Space" taught by Prof. Jean-Philippe Cointet (_Sciences Po_), Prof. Marton Karsai (_Central European University_), and Armin Pournaki (_Sciences Po_).

Team Members: ***Felix Walther***, candidate for the _Master in Public Policy_ in the Policy Stream _xxxx_ and ***Leon Senger***, candidate for the _Master in Public Policy_ in the Policy Stream _Politics and Public Policy_, both at _Sciences Po, Paris_ at the _School of Public Affairs_.


***Research Question***: *How did the Twitter and parliamentary discourses about supplying weapons interact with each other and with the decisions to supply them?*

# Background
On 27 February 2022, only three days after the invasion of Ukraine by Russia, German Chancellor Olaf Scholz announced a major shift in Germany's security and defence policy, which he labelled as _Zeitenwende_, a historic turning point: _

_"We are living through a watershed era. And that means that the world afterwards will no longer be the same as the world before. The issue at the heart of this is whether power is allowed to prevail over the law. Whether we permit Putin to turn back the clock to the nineteenth century and the age of the great powers. Or whether we have it in us to keep warmongers like Putin in check. That requires strength of our own."_

As a consequence, he announced massive investments in the German military. At the same time, he overthrew the decades-old German foreign policy rule, reading: *no armaments to war zones*, by sending 1,000 anti-tank weapons and 500 Stinger missiles to Ukraine. This was the starting point for an increasing engagement of the German government in terms of weapons supply to Ukraine, leading to the delivery of more serious weapons over time: in April, Germany sent flak tanks as defensive weapons, in Mai howitzers were delivered and in June, Scholz announced the supply of the state-of-the-art air defense system Iris-T SLM. Despite this engagement, Scholz was criticized for being too hesitant in supporting Ukraine, too slow with his decisions on delivering weapons, and particularly combat tanks. The Chair of the Committee on European Union Affairs, Anton Hofreiter, for instance, already called for a supply of combat tanks in April 2022: 

/Picture of Tweet.

Similarly, Annalena Baerbock, the German Foreign Minister, publicly called for the supply of Leopard II combat tanks in mid-september (XX). These prominent figures were backed by an ongoing and rich discussion in the news, but importantly also on Twitter. Yet, it took until January 2023 that Scholz decided, after having convinced the US to supply tanks on their part, to free the way for German Leopard II tanks delivery to Ukraine. With this decision, the last taboo regarding supplying armaments to war zones was overcome and the major shift in the German Defence and Security Policy had come to a preliminary peak. 

In this project, we were interested in how different public discourses - namely the discourse on Twitter and the discourse in the German Bundestag - are related to the decisions: did the two discourses precedent or follow the decisions? And did Twitter or the German Bundestag set the direction of the discussion? These are the questions which we tried to answer in this project, summarized in the above mentioned research question. 

This report is structured as follows: First, we are going to give a brief overview of the theory in this field to then use it to derive three hypotheses which we want to test. Second, we describe the data we used, to then move on to the methods we deployed. After that we present the results and discuss the limitations, also sketching what future research could investigate in this question. The report ends with a conclusion. 
/Picture of Tweet.


# Theory
<ins>**Drawing on Agenda Setting . . .**<ins>

Our research questions is building on the literature about the political agenda and social media: what influences what? Political agenda setting is described as a "process by which some issues, but not others, attract political attention" (XX). While in older research agenda setting was mainly discussed with regard to traditional news media, the rise of social media has fundamentally changed the attention dynamics in the political sphere, actively playing an important role for the setting of the agenda: "political information cycles [nowadays] may involve greater numbers and a more diverse range of actors and interactions". For our field of interest, the issue mentioned in the definition is the supply of certain weapons to Ukraine, such that we are interested in how the discourses around supplying weapons on Twitter are related to the discourse in the German Bundestag and the actual decisions taken by the government. 

<ins>**. . . and Discursive Institutionalism**<ins>

A second strand of literature informing our project and complementing the literature on agenda setting is discursive institutionalism. It stresses two crucial ideas: first, that exogenous shocks may create a window of opportunity for path-breaking policy change (see also XX); and second that this policy change depends on the construction of public discussion (XX), which leads right back to the literature on agenda setting. We furthermore use discursive institutionalism's distinction between coordinative discourse, the horizontal discourse among political actors, and communicative discourse, the vertical discourse between political actors and citizens. The theory suggests that in simple polities, like the United Kingdom, communicative discourse is prevalent, while in compound polities, like Germany, coordinative discourse is stronger. Since our interest is on Germany, we derive the importance of the German coordinative discourse, i.e. the discourse of the main political actors with regard to the supply of weapons. 

# Hypotheses
From the theory outlined above and drawing on vote-seeking theories and the finding by Barbera et al that "legislators are more likely to follow, than to lead, discussion of public issues" (XX) we derive the following three hypotheses: 

> *H1: The supply of weapons is precedented by an increase in salience of the topic in the Bundestag.*
 
> *H2: The supply of weapons is precedented by an increase of approval of the delivery on Twitter.*

Furthermore, we are also interested in the dynamics between the discourse on Twitter and the discourse in the German Bundestag. 

> *H3: The increase in salience of the supply of weapons in the German Bundestag is precedented by the approval of the delivery on Twitter.*

# Data
To test our hypotheses, we used three main sources as data: renowned newspaper article's information on the German governmental decisions to supply weapons to Ukraine, Twitter and the plenary debates for the German Bundestag. 

<ins>**Weapons supply decisions by the German government**<ins>

To identify the decisions with regard to the supply of different weapons, we performed a qualitative news paper research, reconstructing the timeline of decisions from the beginning of the war until March 26, 2023. The data is depicted on the following graph. 

/graph

<ins>**Twitter**<ins>

For the collection of the relevant tweets we used the twitter explorer, created by Armin Pournaki, which accesses Twitter via Twitter's v2-API. To identify the relevant terms that should be included in our search query, we qualitatively analyzed German newspaper articles as well as tweets over the period February 2022 until March 2023, generating an encompassing list of terms that are commonly used to refer to the arms supply by Germany. We complemented this list by spelling errors and abbreviations, such that in total we came up with 106 terms. Since the maximum length of a search query is limited to 1024 characters, this resulted in four separate search queries, which had the following structure, also restricting the tweets to German tweets: (((<*term 1* > OR < *term 2* > OR ... OR < *term n-1*> OR < *term n* >) AND Ukraine) lang:de). We limited the period of time from 01. January 2022 (to also see how the discussion developed before the invasion on February 24, 2022) to March 26, 2023. In total, this resulted in the download of 2,098,252 tweets. 

We concatenated the four objects to one panda object. We dropped all tweets that were duplicates, which reduced the number to 820,028 and then limited our dataset to tweets that had more than 4 (i.e., at least 5) retweets, following the from discursive institutionalism theoretically derived focus on the coordinative discourse by the main political actors. This left us with 23,210 tweets (the reason why we did not directly limit the search query for tweets with retweet > 4 is that we wanted to the full data, with the potential to later derive different subsets (which we did not do in the end). Since despite the limitation to lang:de the dataset encompassed non-German tweets, we dropped all those, which resulted in a total of 19,318 tweets. We then cleaned the tweet's texts by excluding ASCII-characters, tabs and URLs, since we expected this to improve the performance of the classifier.  

# Methods
To be able to classify the tweets as taking a positive or negative stand, or being neutral (news tweets for instance), we trained a classifier based on *xlmroberta*, a multi-language model that is also suited for German. To this end we annotated around 1500 tweets as 0 (negative), 1 (positive) or 2 (neutral). There were several borderline cases for which we defined the following two coding specifications: 

1. If someone's opinion (whether positive or negative) is reported by a third party, we labeled it as neutral: 
/Example picture

2. If someone is against the war in general, we labeled it as negative. 
/example picture 


Given limited ressources, we were not able to do a reliability test for the whole dataset, yet a brief interpersonal test showed that the annotation done by one of us was sufficiently reliable and comprehensible. 

The annotated data was then split into one training and one testing dataset, which was then used to train and test the classifier. Since we ran into a cuda error when using google colab, we adjusted several things for (FELIX). 

# Results

As a workaround, instead of using the amount of tweets with a positive stand towards the supply of weapons, we used the development of the total amount of tweets to proxy for the intensity of the discourse on Twitter, assuming that a stronger discussion, that is, higher salience, increases the public pressure on decision-makers. Consequently, our second hypothesis changed to: 

*H2': The supply of weapons is precedented by an increase in salience of the topic on Twitter.*

We start with testing the first hypothesis, stating that "the supply of weapons is precedented by an increase in salience of the topic in the Bundestag" (H1). To do so, we plot the graph indicating the salience of the topic in the German Bundestag on the timeline on the decisions. As we can see on the following graph, especially in the first months of the war the four out of six decisions taken by the government were indeed *precedented* by a peak in discourse. This would back 






