** Unsupervised Learning
* Gaussian Mixture Model
  * GaussianMixture 
    * probabilistic model
    * Implements expectation-maximization 
    * param: n_components=1, covariance_type='full' 
  * BayesianGaussianMixture
  * The Dirichlet Process
* Manifold Learning
  * non-linear dimensionality reduction.
    * Isomap
      * Nearest neighbor search
      * Shortest-path graph search
      * Partial eigenvalue decomposition
      * n_neighbors=5, n_components=2, eigen_solver='auto',
      * path_method = ‘auto’ |FW’ : Floyd-Warshall algorithm.|‘D’ : Dijkstra’s algorithm.
    * Locally Linear Embedding
      * preserves distances within local neighborhoods
      * n_neighbors=5, n_components=2,
    * Spactral Embedding
    * MDS(Multi Dimensional Scaling)
    * t-SNE
      * t-SNE is computationally expensive, and can take several hours on million-sample datasets where 
        PCA will finish in seconds or minutes
* Clustering 
  * K-Means
    * referred to as Lloyd’s algorithm
    * choose centroids that minimise the inertia
    * Voronoi diagrams.
    * Mini Batch K-Means
    
  * Affinity Propagation
  * Mean Shift
  * Spectral Clustering
  * Heirarchical clustering
  * DBSCAN
  * Optics
  * Bircch
  * Performance Evaluation 
    * Adjusted Rand index
    * Mutual Information
    * homogeneity_score
    * completeness_score
    * V-measure
    * Fowlkes-Mallows scores
    * Silhouette Coefficient
    * Calinski-Harabasz Index
    * Contingency Matrix
* Biclustering
   * Spectral Co-clustering
   * Spectral Bi clustering
* Decomposing Signals
   * PCA
   * Truncated SVD  
   * Factor Analysis
   * ICA
* 

_________

    
  
