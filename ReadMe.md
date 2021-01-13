The Stock analysis is done to understand the effect of US China relationship. The 2 apporaches are as follows
1. The Data Analysis based on date wise analysis of stocks and studying the trend pattern for the tariff announcement dates (Final_Python_Project.ipynb)
2. The Dynamic Time Warping approach. The signal processing technique is used in the Machine Learning Context to cluster the similar patterns occuring in the stock market data for better clustering of trends using Hierachical clustering. (DTWClustering.ipynb)

The metrics for unsupervised cluster quality checking: Please reference the blog - https://medium.com/@haataa/how-to-measure-clustering-performances-when-there-are-no-ground-truth-db027e9a871c

1. silhouette_score - a: The mean distance between a sample and all other points in the same class. This score measure the closeness of points in the same cluster.
b: The mean distance between a sample and all other points in the next nearest cluster. This score measure the distance of points of different clusters. 

2. calinski_harabasz_score - the ratio of the sum of between-clusters dispersion and of inter-cluster dispersion for all clusters, the higher the score , the better the performances.

3. davies_bouldin_score - This index signifies the average ‘similarity’ between clusters, where the similarity is a measure that compares the distance between clusters with the size of the clusters themselves. 

