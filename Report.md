Title: Optimizing Urban Mobility through Traffic Clustering (SDG 11)

1. SDG Problem Addressed

This project addresses Sustainable Development Goal 11: Sustainable Cities and Communities.
Urban areas often suffer from traffic congestion, leading to increased air pollution, fuel waste, and commuter delays. Our goal is to use machine learning to analyze traffic patterns and help city planners optimize public transport routes to reduce congestion and environmental impact.

2. ML Approach Used

We implemented an unsupervised learning approach using K-Means Clustering.
The model was trained on a real-world dataset — Metro Interstate Traffic Volume — which includes:

    Traffic volume

    Temperature

    Rainfall

    Snowfall

    Hour of day

After cleaning and normalizing the data, K-Means grouped traffic conditions into clusters based on similarities in patterns.

3. Results

The elbow method suggested 4 optimal clusters:

    Cluster 0: Very low traffic – late-night hours

    Cluster 1: Rush hour peaks – morning and evening

    Cluster 2: Moderate flow – midday traffic

    Cluster 3: Irregular patterns, likely due to weather disruptions

By visualizing traffic volume versus hour, we gained actionable insights for adjusting bus schedules and optimizing route timings.

4. Ethical Considerations

    Bias Risk: Data may not cover weekends or all city zones, skewing the model.

    Fairness: Models should be extended to underserved areas to ensure equitable service.

    Sustainability: Reducing congestion means fewer emissions and more efficient transport — directly supporting SDG 11.

Conclusion

Clustering offers a powerful, interpretable approach for identifying traffic trends. It enables smarter urban transport design, helping build cleaner, more efficient, and inclusive cities.

Tools Used: Python, Jupyter Notebook, Scikit-learn, Pandas, Seaborn
Dataset: Kaggle – Metro Interstate Traffic Volume
