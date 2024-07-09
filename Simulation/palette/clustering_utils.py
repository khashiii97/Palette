# a set of functions that can be used for different clustering algorithms and even visualizations
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
#The next three functions are used for drawing the boxplots
def calculate_intra_cluster_distances_from_matrix(distance_matrix, clusters, k):
    intra_distances = []
    for cluster_idx in range(k):
        cluster_points = np.where(clusters == cluster_idx)[0]
        
        if len(cluster_points) > 1:
            dists = distance_matrix[np.ix_(cluster_points, cluster_points)]
            #The np.ix_ function takes multiple sequences (typically 1D arrays or lists) and returns a tuple of arrays. 
            # Each array in the tuple can be used to index a specific dimension of a multidimensional array.


            intra_distances.append(np.mean(dists[np.triu_indices_from(dists, k=1)]))
            #np.triu_indices_from is a function that returns the indices of the upper triangular part of a matrix.
            # The argument k=1 specifies that we want the upper triangular part excluding the diagonal. 
            # If k=0, it would include the diagonal, and if k is positive, it excludes the first k diagonals above the main diagonal.
        else:
            intra_distances.append(0)
    
    return intra_distances

def calculate_inter_cluster_distances_from_matrix(distance_matrix, clusters, k):
    inter_distances = [[] for _ in range(k)]
    
    for i in range(k):
        for j in range(k):
            if i != j:
                # Find points in clusters i and j
                cluster_i_points = np.where(clusters == i)[0]
                cluster_j_points = np.where(clusters == j)[0]
                
                # Extract distances between points in cluster i and cluster j
                dists = distance_matrix[np.ix_(cluster_i_points, cluster_j_points)]
                
                # Calculate the mean distance
                mean_dist = np.mean(dists)
                
                # Append the mean distance to the corresponding cluster's list
                inter_distances[i].append(mean_dist)
    
    
    return inter_distances

def plot_clusters_with_distance_matrix(distance_matrix, clusters, k, dir_path = None, text_title = None, sampling = False):
    intra_distances = calculate_intra_cluster_distances_from_matrix(distance_matrix, clusters, k)
    inter_distances = calculate_inter_cluster_distances_from_matrix(distance_matrix, clusters, k)
    
    
    plt.figure(figsize=(12, 6))
    
    # Create boxplot for inter-cluster distances
    plt.boxplot(inter_distances, positions=range(1, k+1), widths=0.6, showfliers=False)
    
    # Overlay intra-cluster distances
    plt.scatter(range(1, k+1), intra_distances, color='blue', label='Intra-cluster Distance', zorder=3)
    
    plt.xlabel('Cluster Index')
    plt.ylabel('Distance')
    if text_title:
        plt.title(text_title)
    else:
        plt.title('Similarity Measure Among Clusters')
    plt.legend()
    if dir_path:
        filename = 'boxplots-sampling.png' # the distances have been computed through smapling
        if not sampling:
            filename = 'boxplots-representatives.png'
        # save_file(dir_path= dir_path, file_name= filename)
    else:
        plt.show()
