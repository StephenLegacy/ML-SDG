
````markdown
# 🚦 Traffic Clustering for Sustainable Cities (SDG 11)

This project uses machine learning to address urban traffic congestion, a major challenge under **UN Sustainable Development Goal 11: Sustainable Cities and Communities**. By clustering traffic patterns using K-Means, we can help city planners and transport authorities **optimize bus routes, reduce emissions**, and improve public transportation efficiency.

---

## 📌 Project Overview

- **SDG Target**: Reduce traffic congestion and improve access to sustainable transport systems.
- **ML Approach**: Unsupervised Learning (K-Means Clustering)
- **Dataset**: [Metro Interstate Traffic Volume](https://www.kaggle.com/datasets/pooriamst/metro-interstate-traffic-volume?)
- **Goal**: Identify traffic patterns to support smarter, greener transportation planning.

---

## 🧠 Machine Learning Workflow

1. **Data Preprocessing**:
   - Extracted features: `traffic_volume`, `temperature`, `rain_1h`, `snow_1h`, `hour of day`
   - Cleaned and normalized the dataset

2. **Clustering**:
   - Applied **K-Means Clustering**
   - Determined optimal clusters using the **elbow method**

3. **Visualization**:
   - Plotted traffic volume vs hour by cluster
   - Revealed peak hours and outlier conditions

---

## 📸 Screenshots

### 📊 Elbow Method Graph
_This graph shows the optimal number of clusters for the dataset._

![Elbow Method Screenshot](/Elbow.png)

---

### 🧭 Clustered Traffic Visualization
_Traffic volume by hour of day colored by cluster for interpretation._

![Clustered Traffic Screenshot](/cluster.png)

---

## 📊 Results

- **Cluster 0**: Low traffic (late-night hours)
- **Cluster 1**: High congestion (morning/evening rush)
- **Cluster 2**: Steady midday flow
- **Cluster 3**: Weather-related outliers

The insights from clustering can guide **public transport route adjustments**, **bus frequency changes**, or **infrastructure planning**.

---

## 🔍 Ethical Considerations

- Potential **bias** due to limited city data or missing weather records
- Model promotes **fairer access** to mobility by identifying underserved or over-congested areas
- Supports **environmental sustainability** by targeting high-pollution time slots

---

## ⚙️ How to Run

1. Clone this repo or download the files
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
````

3. Run the script:

   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
SDG11_Traffic_Clustering/
├── main.py
├── Metro_Interstate_Traffic_Volume.csv
├── clustered_traffic_data.csv
├── requirements.txt
├── screenshots/
│   ├── elbow_method.png
│   └── cluster_visualization.png
├── README.md
└── report.txt
```

---

## 🙌 Author

**Stephen Oloo**
Aspiring AWS Solutions Architect | Cloud & Cybersecurity Enthusiast
[LinkedIn Profile](https://www.linkedin.com/in/stephenoloolegacyio)

---

## 🌍 License

This project is open for educational and research purposes under the **MIT License**.

```

---


