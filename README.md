# sentiment-analysis-py

Goal is to use VADER to proccess sentiment analysis of a person's journaling. 

VADER is a useful proxy NLP tool for this project because people already use social media to express their feelings, this project aims to use it to proccess user journaling.

1. Journal will have preset meaningful jounraling questions that assess 4 main catagories: 
    - Daily Reflection
    - Personal Growth 
    - Goal-Oriented Reflection
    - Mindfulness and Presence
2. User will answer questions about each. The tool will then proccess those answers giving us the following sets of data: 
    - Compound
    - Positive
    - Neutral
    - Negative
3. Proccess and save that information behind the scenes to track, plot and estimate ebs and flows of the mental state
    - In response project will give user things they should thing about to respond with


# Important Texts
- https://github.com/totalgood/nlpia/blob/master/src/nlpia/data/hutto_ICWSM_2014/vader_icwsm2014_final.pdf
- https://github.com/HenriqueAssumpcao/SentiMentalHealth
- https://www.sciencedirect.com/science/article/abs/pii/S0167739X21002764?dgcid=author
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9368160/
- https://pkg.go.dev/github.com/cdipaolo/sentiment#section-readme
- https://github.com/cdipaolo/sentiment
- https://chirag-sehra.medium.com/sentiment-analysis-in-go-efa0ae62cea1
- https://github.com/drankou/go-vader
- https://github.com/cjhutto/vaderSentiment

# Active Questions
- Could we use the baseline sentiment of the questions to better asses person's answer values to the questions?
- Should we consider expected resonse ranges for said questions and analyze them? 
    - example: What made me smile today? {'neg': 0.0, 'neu': 0.615, 'pos': 0.385, 'compound': 0.3612} -> this should elicit a fairly positive score responding with a neutral score isnt nessicarily neutral. Should probaly formulate the question to request additional information such as (what made you smile today, how did it make you feel )
- Will eventually use [NLTK](https://github.com/nltk/nltk) to proccess longform information.