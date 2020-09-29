# Angry Text Detector 

#### Description 
The goal was create an angry text detector that would predict if the text was angry or not. I used topic modeling on Reddit posts to figure out what makes people angry with TF-IDF and NMF. For my model, I built a sequential deep learning model using a Bidirectional LSTM with word embeddings. I also created a Streamlit app where you can put in a text and it will give you the probability of how angry the text seems to be. 

#### Data Sources
- [Emotion Stimulus](http://www.site.uottawa.ca/~diana/resources/emotion_stimulus_data/)
- [ISEAR](https://www.researchgate.net/figure/Characteristics-of-the-ISEAR-Dataset_tbl1_313407834)
- [WASSA-2017](http://saifmohammad.com/WebPages/EmotionIntensity-SharedTask.html)

#### File Contents
- `Data Cleaning and Topic Modeling` contains all loading and cleaning of movie scripts and sentiment analysis. 
- `Merge Datasets and Modeling.ipynb` contains topic modeling using TFIDF and NMF. Also contains PCA and visualization. 
- `app_file.py` contains code used to create Streamlit app. 
