from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pywaffle import Waffle
import folium




'''data = {
    'dept':['CSE','CSE','ECE','ECE','MECH','MECH','CIVIL','CIVIL','CSE','CSE','ECE','ECE','MECH','MECH','CIVIL','CIVIL'],
    'gender':['M','F','M','F','M','F','M','F','M','F','M','F','M','F','M','F'],
    'year':[2023,2023,2023,2023,2023,2023,2023,2023,2024,2024,2024,2024,2024,2024,2024,2024],
    'count':[85,45,60,40,50,20,35,15,90,55,65,45,52,25,38,18]
}
df = pd.DataFrame(data)
#  Group by department
dept_counts = df.groupby('dept')['count'].sum()

# Convert to dictionary
data_dict = dept_counts.to_dict()

# Create waffle chart
fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    columns=20,
    values=data_dict,
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
)

plt.show()

df = pd.read_csv("student_feedback.csv",header=None, names=['feedback'])
feedback_text = " ".join(df['feedback'])
wordcloud = WordCloud(background_color='white').generate(feedback_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

df = pd.read_csv("twitter.csv",header=None,names=['tweet'])
tweet_text = " ".join(df['tweet'].dropna().astype(str))
stopwords = set(STOPWORDS)
mask = np.array(Image.open("heart.png").convert('L'))
wordcloud = WordCloud(background_color='white',stopwords=stopwords, mask=mask).generate(tweet_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

df = pd.read_csv("movie_review.csv",header=None,names=['review'])
review_text = " ".join(df['review'].dropna().astype(str))
stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color='white',stopwords=stopwords).generate(review_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()'''