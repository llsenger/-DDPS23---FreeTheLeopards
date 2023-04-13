![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/1a6433ebb18898fa2f9e840e54a4fcc3bc2128bb/Pictures/%23freetheleopards_image.png?raw=true)

# ***The Discourse Around the Shift of  Germany’s Arms Supply Policy***

_April 13, 2023_

This repository summarizes the findings and provides the code of our project for the CIVICA course "Diving in the Digital Public Space" taught by Prof. Jean-Philippe Cointet (_Sciences Po_), Prof. Marton Karsai (_Central European University_), and Armin Pournaki (_Sciences Po_).

Team Members: ***Felix Walther***, candidate for the _Master in Public Policy_ in the Policy Stream _Energy, Environment and Sustainability_ and ***Leon Senger***, candidate for the _Master in Public Policy_ in the Policy Stream _Politics and Public Policy_, both at _Sciences Po, Paris_ at the _School of Public Affairs_.


***Research Question***: *How did the Twitter and parliamentary discourses about supplying weapons interact with each other and with the decisions to supply them?*

# Background
On 27 February 2022, only three days after the invasion of Ukraine by Russia, German Chancellor Olaf Scholz announced a major shift in Germany's security and defence policy, which he labelled as _Zeitenwende_, a historic turning point:

_"We are living through a watershed era. And that means that the world afterwards will no longer be the same as the world before. The issue at the heart of this is whether power is allowed to prevail over the law. Whether we permit Putin to turn back the clock to the nineteenth century and the age of the great powers. Or whether we have it in us to keep warmongers like Putin in check. That requires strength of our own."_ (Scholz, 2022)

As a consequence, he announced massive investments in the German military. At the same time, he overthrew the decades-old German foreign policy rule, reading: *no armaments to war zones*, by sending 1,000 anti-tank weapons and 500 Stinger missiles to Ukraine. This was the starting point for an increasing engagement of the German government in terms of weapons supply to Ukraine, leading to the delivery of more serious weapons over time: in April, Germany sent flak tanks as defensive weapons, in Mai howitzers were delivered and in June, Scholz announced the supply of the state-of-the-art air defense system Iris-T SLM. Despite this engagement, Scholz was criticized for being too hesitant in supporting Ukraine, too slow with his decisions on delivering weapons, and particularly combat tanks. The Chair of the Committee on European Union Affairs, Anton Hofreiter, for instance, already called for a supply of combat tanks in April 2022: 

![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/1a6433ebb18898fa2f9e840e54a4fcc3bc2128bb/Pictures/Hofreiter.png??raw=true)

Similarly, Annalena Baerbock, the German Foreign Minister, publicly called for the supply of Leopard II combat tanks in mid-september (Pausch and Stark, 2023). These prominent figures were backed by an ongoing and rich discussion in the news, but importantly also on Twitter. Yet, it took until January 2023 that Scholz decided, after having convinced the US to supply tanks on their part, to free the way for German Leopard II tanks delivery to Ukraine. With this decision, the last taboo regarding supplying armaments to war zones was overcome and the major shift in the German Defence and Security Policy had come to a preliminary peak. 

In this project, we were interested in how different public discourses - namely the discourse on Twitter and the discourse in the German Bundestag - are related to the decisions: did the two discourses precedent or follow the decisions? And did Twitter or the German Bundestag set the direction of the discussion? These are the questions which we tried to answer in this project, summarized in the above mentioned research question. 

This report is structured as follows: First, we are going to give a brief overview of the theory in this field to then use it to derive three hypotheses which we want to test. Second, we describe the data we used, to then move on to the methods we deployed. After that we present the results and discuss the limitations, also sketching what future research could investigate in this question. The report ends with a conclusion. 


# Theory
<ins>**Drawing on Agenda Setting . . .**<ins>

Our research questions is building on the literature about the political agenda and social media: what influences what? Political agenda setting is described as a "process by which some issues, but not others, attract political attention" (Gilardi et al., 2022). While in older research agenda setting was mainly discussed with regard to traditional news media, the rise of social media has fundamentally changed the attention dynamics in the political sphere, actively playing an important role for the setting of the agenda: "political information cycles [nowadays] may involve greater numbers and a more diverse range of actors and interactions" (Chadwick, 2010). For our field of interest, the issue mentioned in the definition is the supply of certain weapons to Ukraine, such that we are interested in how the discourses around supplying weapons on Twitter are related to the discourse in the German Bundestag and the actual decisions taken by the government. 

<ins>**. . . and Discursive Institutionalism**<ins>

A second strand of literature informing our project and complementing the literature on agenda setting is discursive institutionalism. It stresses two crucial ideas: first, that exogenous shocks may create a window of opportunity for path-breaking policy change (see also Widmaier et al. 2007) and second that this policy change depends on the construction of public discussion (Hagelund, 2020), which leads right back to the literature on agenda setting. We furthermore use discursive institutionalism's distinction between coordinative discourse, the horizontal discourse among political actors, and communicative discourse, the vertical discourse between political actors and citizens. The theory suggests that in simple polities, like the United Kingdom, communicative discourse is prevalent, while in compound polities, like Germany, coordinative discourse is stronger (Schmidt, 2008). Since our interest is on Germany, we derive the importance of the German coordinative discourse, i.e. the discourse of the main political actors with regard to the supply of weapons. 

# Hypotheses
From the theory outlined above and drawing on vote-seeking theories and the finding by Barbera et al that "legislators are more likely to follow, than to lead, discussion of public issues" (Barberá, 2019) we derive the following three hypotheses: 

> *H1: The supply of weapons is precedented by an increase in salience of the topic in the Bundestag.*
 
> *H2: The supply of weapons is precedented by an increase of approval of the delivery on Twitter.*

Furthermore, we are also interested in the dynamics between the discourse on Twitter and the discourse in the German Bundestag. 

> *H3: The increase in salience of the supply of weapons in the German Bundestag is precedented by the approval of the delivery on Twitter.*

# Data
To test our hypotheses, we used three main sources as data: renowned newspaper article's information on the German governmental decisions to supply weapons to Ukraine, Twitter and the plenary debates for the German Bundestag. 

<ins>**Weapons supply decisions by the German government**<ins>

To identify the decisions with regard to the supply of different weapons, we performed a qualitative news paper research, reconstructing the timeline of decisions from the beginning of the war until March 26, 2023. The data is depicted on the following graph. 

![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/7ef2bde8d35140241f4eafc69c483e517814c95b/Pictures/Timegraph.png?raw=true)

<ins>**Twitter**<ins>

For the collection of the relevant tweets we used the twitter explorer, created by Armin Pournaki, which accesses Twitter via Twitter's v2-API. To identify the relevant terms that should be included in our search query, we qualitatively analyzed German newspaper articles as well as tweets over the period February 2022 until March 2023, generating an encompassing list of terms that are commonly used to refer to the arms supply by Germany. We complemented this list by spelling errors and abbreviations, such that in total we came up with 106 terms. Since the maximum length of a search query is limited to 1024 characters, this resulted in four separate search queries, which had the following structure, also restricting the tweets to German tweets: (((<*term 1* > OR < *term 2* > OR ... OR < *term n-1*> OR < *term n* >) AND Ukraine) lang:de). We limited the period of time from 01. January 2022 (to also see how the discussion developed before the invasion on February 24, 2022) to March 26, 2023. In total, this resulted in the download of 2,098,252 tweets. 

We concatenated the four objects to one panda object. We dropped all tweets that were duplicates, which reduced the number to 820,028 and then limited our dataset to tweets that had more than 4 (i.e., at least 5) retweets, following the from discursive institutionalism theoretically derived focus on the coordinative discourse by the main political actors. This left us with 23,210 tweets (the reason why we did not directly limit the search query for tweets with retweet > 4 is that we wanted to the full data, with the potential to later derive different subsets (which we did not do in the end). Since despite the limitation to lang:de the dataset encompassed non-German tweets, we dropped all those, which resulted in a total of 19,318 tweets. We then cleaned the tweet's texts by excluding ASCII-characters, tabs and URLs, since our tests showed a particulary bad performance of the classifier for tweets with a large share of URLs and special characters.  
 
<ins>**Bundestag**<ins>

As the Bundestag is a working parliament (“Arbeitsparlament”), thus, most work happens in the non-public committees. For this reason, the speeches in the general assembly are specifically geared towards the public (Geuß, 2021). We thus decided that these speeches would be a good source to examine the parliamentary discourse.
While the Bundestag offers a REST-API, it only allows for a full-text search on its website. Hence, we decided not to use the API as such, but scrape all plenary speeches of the 20th election period (since 2021). Unfortunately, these are only available as .pdf or .xml files, which prevents direct automated analysis. To get the speeches in a usable format, we were luckily able to build on the “Open-Discourse” project (Richter et al., 2021). 

# Methods
To be able to classify the tweets as taking a positive or negative stand, or being neutral (news tweets for instance), we trained a classifier based on *xlmroberta*, a multi-language model that is also suited for German. To this end we annotated around 1500 tweets as 0 (negative), 1 (positive) or 2 (neutral). There were several borderline cases for which we defined the following two coding specifications: 

1. If someone's opinion (whether positive or negative) is reported by a third party, we labeled it as neutral: 

![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/1a6433ebb18898fa2f9e840e54a4fcc3bc2128bb/Pictures/Zitat_Beispiel_neutral.png?raw=true)


2. If someone is against the war in general, we labeled it as negative. 

![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/82429056541162d2a39fc7a96a0195db6df61270/Pictures/Zitat_Beispiel_negativ.png?raw=true)

Given limited ressources, we were not able to do a reliability test for the whole dataset, yet a brief interpersonal test showed that the annotation done by one of us was sufficiently reliable and comprehensible. 

The annotated data was then split into one training and one testing dataset, which was then used to train and test the classifier. Since we ran into a cuda error when using google colab, we adjusted several factors, including using a CPU-based runtime and different combinations of versions of different packages.
 
For the Bundestag data, we opted for a simple frequency count. After extracting and cleaning all speeches, they were grouped together for each day. The same queries used to scrape the Twitter data were than used to create a matrix that contains the frequency of every category of keywords (e.g. ["iris", "irist", "iristslm", "tslm", "patriot", "flugabwehrsystem"] for the IRIS-SLM anti-air system) for every day.
This gives us the opportunity to trace the salience of single decisions for weapon systems for future research. For the graphs shown below the sum of all keywords was used, as this corresponds to the frequency count used for the Twitter data.

# Results
 
We planned on using XLM-RoBERTa model (Conneau et al., 2020) which is based on Facebook’s RoBERTa model, which itself is an improved version of the original BERT model. XLM-RoBERTa is a multilingual model, which was necessary due to using only German-speaking tweets. It additionally has significantly higher performance than the original model (ibid.). 
The best score the model could achieve after training and testing it on different subsections of our 1500 manually annotated tweets and further cleaning the data is the following:
 
                            precision    recall  f1-score   support
            
                       0       0.00      0.00      0.00        26
                       1       0.67      1.00      0.80        52
                       2       1.00      1.00      1.00        38
            
                accuracy                           0.78       116
               macro avg       0.56      0.67      0.60       116
            weighted avg       0.63      0.78      0.69       116
 
The model had a heavy bias for classifying tweets as having no position on deliveries (2), while having a meager performance for supportive positions (1) and not classifying any tweets as opposing to the deliveries (0).
 
As we could not achieve further improvements without annotating significantly more tweets, we turned to two alternative models, the first being “German Sentiment Bert” (Guhr et al., 2020). This model was pre-trained on German-speaking data from social media for sentiment analysis. We trained the model with our data, but the classification results were too inaccurate for further use. as the model - in most instances somewhat accurately - classified almost all tweets as having a negative sentiment. As this is quite pertinent in our data for both sides, this attempt proved to be a cul de sac.
 
Second, we found a model pre-trained on stances in the Ukraine war (Gahrte, 2023). However, after fine tuning on our data, the classifier had a very heavy bias on classifying tweets as supportive while almost never detecting opposing stands. Again, these results were deemed to be unusable for further analysis.

As a workaround, instead of using the amount of tweets with a positive stand towards the supply of weapons, we used the development of the total amount of tweets to proxy for the intensity of the discourse on Twitter, assuming that a stronger discussion, that is, higher salience, increases the public pressure on decision-makers. Consequently, our second hypothesis changed to: 

> *H2': The supply of weapons is precedented by an increase in salience of the topic on Twitter.*

To test our hypotheses, we plot the graphs indicating the salience of the topic in the German Bundestag (red line) and the salience of the topic on Twitter (blue line) on the timeline on the decisions (grey bars in the background). 

![alt text](https://github.com/llsenger/-DDPS23---FreeTheLeopards/blob/0d5ace0a4000c1a0c57e521cd0f9c23adb4e6fad/Pictures/Graph%20Final.png?raw=true)

We start with testing the first hypothesis, which states that "the supply of weapons is precedented by an increase in salience of the topic in the Bundestag" (H1).  As we can see on the graph, especially in the first months of the war four out of six decisions taken by the government were indeed *precedented* by a peak in discourse in the Bundestag. This backs H1. However, especially for the decisions in January 2023 there was no peak before the decisions but the discussion rather coincided with the decisions (the peaks are on the grey bars) and consequently it is more likely that the discussions in the Bundestag were part of the decision process instead of influencing it. 

To test hypothesis H2' we take the same approach as for the first hypothesis. The graph shows a very similar picture as for Hypothesis 1. Four out of six decisions in 2022 were precedented by an increase of the salience on Twitter. This is especially visible for the ring exchange in May and the supply of flak tanks in June: here we see two very clear peaks of the discussion on Twitter. For the remaining decisions, including those in 2023 on the delivery of combat tanks (Leopard II), the salience peak coincided with the day of the decision, hence rather indicating a reaction than an independent increase in public pressure. 

Finally we test Hypothesis 3 by comparing the peaks of the discourse on Twitter with those of the discourse on the Bundestag. While on the graph also no cristal clear picture arises, it seems safe to say that generally the Twitter discourse happend to peak before the discourse in the Bundestag, suggesting an influence of the discourse on Twitter's salience on the topics the Bundestag discusses, which is in line with the finding by Barbera et al. (2019). 

To summarize our results, despite imperfect patterns, we found some support for all our hypotheses, indicating that indeed there is a tendency of the decisions to be precedented by an increase in salience on both Twitter and in the German Bundestag with regard to the topic of weapons supply, and a remarkable impact of the Twitter discourse on the German Bundestag's discussions. However, obviously, these findings derived from a graph cannot be seen as very robust. In the following section we therefore briefly discuss our limitations and outline what future research dealing with exactly this topic could pursue. 
 
# Limitations and Future Research
 
The are a few limitations that have to be taken into account. First of all, the annotation of the data was not interpersonal. Second, our classifier did not work, independent of the models used, which was most likely due to a too low number of annotated tweets which in turn was caused by our limited ressources. This resulted in a quite unspecific data, summarizing all discourse around weapons supply without distinguishing between positive and negative attitudes. That the major limitation of our project lies in the fact that our graphical approach does not allow for any causality claims: the correlation we found does not allow for deeper interpretation, such that we cannot claim that public discourse decisively influenced the decisions of the German government. A statistical investigation based on vector autoregression models, which would have been suitable in that regard, was not possible because of the low number of decisions. 

Next to adressing these limitations, there are several further paths for future research that might be worth exploring. 

First of all, the data could be subdivided according to the different discourses around different weapons, which could potentially unearth patterns that are not visible in the unspecified data: potentially there could be certain weapons supply decision that are indeed clearly precedented by the weapon specific discourse on Twitter and in the German Bundestag. 

Second, an interesting option to enrich the data would be to scrape newspaper opinion pieces and to train a classifier (of course, next to getting our Twitter classifier to work) to label them as supportive of or cautioning against weapons delivery. This would allow to investigate the in our project so far neglected dimension of the impact of traditional media, which is usually deemed to be crucial for agenda setting.

Finally, a network analysis, starting from Twitter but from there also taking the speakers of the Bundestag into account, could be very fruitful. Potential questions to be answered could be: Which actors push the agenda on Twitter and in the German Bundestag? Are there clear connections between the actors on Twitter and the politicians in the German Bundestag? This could provide insight into how social media is impacting political discourse in Germany and further shed light on the question who actually sets the agenda and potentially generates public pressure.
 
# Conclusion 
 
This project was formed around the major policy shift in German Defense and Security policy and aimed at answering the question how the discourses on Twitter and in the German parliament interacted with each other and particularly with the decisions by the German government under Chancellor Scholz to supply weapons to Ukraine. Based on agenda setting theory and discursive institutionalism, we hypothesized that the discourses on twitter influenced the discourse in the German Bundestag, while both discourses precedented the decisions taken by the German government. We indeed found patterns in favor of these hypotheses, yet without a clear-directional trend. This, however, could be a function of the aggregate level at which we analyzed the data, such that there is room for promising future research, taking advantage of higher segregation the data would theoretically allow. Our project has shown that the question around who set the agenda for one of the greatest policy shifts in German policy in the past years is worth to be investigated. 


# Bibliography
 
- Barberá, P., Casas, A., Nagler, J., Egan, P. J., Bonneau, R., Jost, J. T., & Tucker, J. A. (2019). Who leads? Who follows? Measuring issue attention and agenda setting by legislators and the mass public using social media data. American Political Science Review, 113(4), 883-901.
- Chadwick, A. (2011). The political information cycle in a hybrid news system: The British prime minister and the “Bullygate” affair. The International Journal of Press/Politics, 16(1), 3-29.
- Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E., Ott, M., Zettlemoyer, L., & Stoyanov, V. (2020). Unsupervised Cross-lingual Representation Learning at Scale (arXiv:1911.02116). arXiv. https://doi.org/10.48550/arXiv.1911.02116  
Gahrte, J. (2023, March). Joh-ga/german-tweetstance-bert-uncased-russiaukrainewar · Hugging Face. https://huggingface.co/joh-ga/german-tweetstance-bert-uncased-russiaukrainewar  
- Geuß, A. (2021). Das Parlament als Kommunikationsarena: Öffentlichkeitsebenen und Kommunikationsmuster in Plenardebatten des Deutschen Bundestags. https://doi.org/10.20378/irb-51447  
- Guhr, O., Bahrmann, F., Schumann, A.-K., & Böhme, H.-J. (2020, May 15). Training a Broad-Coverage German Sentiment Classification Model for Dialog Systems. http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.202.pdf  
- Gilardi, F., Gessler, T., Kubli, M., & Müller, S. (2022). Social media and political agenda setting. Political Communication, 39(1), 39-60.
- Hagelund, A. (2020). After the refugee crisis: public discourse and policy change in Denmark, Norway and Sweden. Comparative Migration Studies, 8(1), 1-17.
- Pausch, R., and Stark, H., (2023). Die Vertrauensfrage. Zeit Online. Online available at: https://www.zeit.de/2023/07/panzer-lieferungen-annalena-baerbock-olaf-scholz-differenzen/komplettansicht
- Richter, F., Koch, P., Franke, O., Kraus, J., Kuruc, F., Thiem, A., Högerl, J., Heine, S., & Schöps, K. (2021). Open Discourse [Data set]. https://doi.org/10.7910/DVN/FIKIBO  
- Schmidt, V. A. (2008). Discursive institutionalism: The explanatory power of ideas and discourse. Annu. Rev. Polit. Sci., 11, 303-326.
- Scholz, O., (2022)."Resolutely committed to peace and security". Policy statement by Olaf Scholz, Chancellor of the Federal Republic of Germany and Member of the German Bundestag, 27 February 2022 in Berlin. Bundesregierung. Online available at: https://www.bundesregierung.de/breg-en/news/policy-statement-by-olaf-scholz-chancellor-of-the-federal-republic-of-germany-and-member-of-the-german-bundestag-27-february-2022-in-berlin-2008378
- Widmaier, W. W., Blyth, M., & Seabrooke, L. (2007). Exogenous shocks or endogenous constructions? The meanings of wars and crises. International studies quarterly, 51(4), 747-759.

