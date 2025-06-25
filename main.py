# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 2: Load data
df = pd.read_csv('Metro_Interstate_Traffic_Volume.csv') 
print(df.head())
print(df.info())


#Step 3 : Data pre-processing
# Convert date_time to hour
df['date_time'] = pd.to_datetime(df['date_time'])
df['hour'] = df['date_time'].dt.hour

# Select features for clustering
features = df[['traffic_volume', 'temp', 'rain_1h', 'snow_1h', 'hour']]

# Handle missing values
features = features.fillna(0)

# Normalize data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

#Step 4:  Elbow Method to determine best k
inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, 'bo-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()

# Step 5 - Apply K-Means with k=4 (Clustering)
kmeans = KMeans(n_clusters=4, random_state=0)
df['cluster'] = kmeans.fit_predict(scaled_features)


# Step 6 Plot clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='hour', y='traffic_volume', hue='cluster', palette='tab10')
plt.title('Traffic Clustering by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Traffic Volume')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()
