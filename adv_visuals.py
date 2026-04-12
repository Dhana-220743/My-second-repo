#data visulazation:
#1.Word Cloud (Basic)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """Teaching is excellent and very clear
Labs are well organized and very helpful
The faculty explains machine learning clearly
Python lab sessions are very interesting"""

wc = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()

#2.Waffle Chart (Student Data)
from pywaffle import Waffle
import matplotlib.pyplot as plt

data = {
    'CSE Male': 85,
    'CSE Female': 45,
    'ECE Male': 60,
    'ECE Female': 40
}

fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data,
    figsize=(10,5),
    legend={'loc': 'upper left', 'bbox_to_anchor': (1,1)}
)

plt.show()

#3.Department-wise Student Count (Bar Chart)
import pandas as pd
import matplotlib.pyplot as plt

data = {
'Department': ['CSE','ECE','MECH','CIVIL'],
'Count': [130,100,70,50]
}

df = pd.DataFrame(data)

plt.bar(df['Department'], df['Count'])
plt.title("Department-wise Student Count")
plt.xlabel("Department")
plt.ylabel("Students")
plt.show()

#4.Word Cloud with Stopwords Removed
from wordcloud import WordCloud, STOPWORDS

text = "Teaching is excellent and very clear and very helpful"

stopwords = set(STOPWORDS)

wc = WordCloud(stopwords=stopwords).generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()

#5.India Map (Folium)
import folium

india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

india_map

#6. Multiple Cities Map
cities = [
    ("Hyderabad", 17.38, 78.48),
    ("Delhi", 28.70, 77.10),
    ("Mumbai", 19.07, 72.87)
]

m = folium.Map(location=[20,78], zoom_start=5)

for city, lat, lon in cities:
    folium.Marker([lat, lon], popup=city).add_to(m)

m
#7. Heatmap (Pollution)

from folium.plugins import HeatMap

data = [
    [17.38, 78.48, 70],
    [19.07, 72.87, 90],
    [28.70, 77.10, 85]
]

m = folium.Map(location=[20,78], zoom_start=5)

HeatMap(data).add_to(m)

m
#8.8. Circle Markers (Population)
cities = [
    ("Hyderabad", 17.38, 78.48, 10),
    ("Mumbai", 19.07, 72.87, 20)
]

m = folium.Map(location=[20,78], zoom_start=5)

for city, lat, lon, pop in cities:
    folium.CircleMarker(
        location=[lat, lon],
        radius=pop,
        popup=city,
        color='blue'
    ).add_to(m)

m

#9.Sunburst Plot (Plotly)
import plotly.express as px

data = dict(
    Department=['CSE','CSE','ECE','ECE'],
    Gender=['Male','Female','Male','Female'],
    Count=[80,40,50,30]
)

fig = px.sunburst(
    data,
    path=['Department','Gender'],
    values='Count'
)

fig.show()

#10. Treemap (Plotly)
fig = px.treemap(
    data,
    path=['Department','Gender'],
    values='Count'
)

fig.show()

#11.Year-wise Waffle Chart
data_2022 = {'A':50,'B':30,'C':20}
data_2023 = {'A':40,'B':35,'C':25}

fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data_2022,
    title="2022 Market Share"
)
plt.show()

fig = plt.figure(
    FigureClass=Waffle,
    rows=5,
    values=data_2023,
    title="2023 Market Share"
)
plt.show()

#12.Year-wise Waffle Chart
positive = "Excellent teaching good faculty"
negative = "Poor infrastructure bad labs"
neutral = "Average course difficulty"

for text in [positive, negative, neutral]:
    wc = WordCloud().generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

#13.Marker Clustering
from folium.plugins import MarkerCluster

m = folium.Map(location=[17.38,78.48], zoom_start=12)

cluster = MarkerCluster().add_to(m)

locations = [
    [17.3850,78.4867],
    [17.3900,78.4800],
    [17.3950,78.5000]
]

for loc in locations:
    folium.Marker(loc).add_to(cluster)

m

#14. Route Visualization
route1 = [
    [17.3850,78.4867],
    [17.3920,78.4980],
    [17.4000,78.5100]
]

m = folium.Map(location=[17.38,78.48], zoom_start=12)

folium.PolyLine(route1, color="blue").add_to(m)

m