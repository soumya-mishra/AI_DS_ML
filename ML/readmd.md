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
  
