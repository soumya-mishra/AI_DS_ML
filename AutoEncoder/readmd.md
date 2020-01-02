
AutoEncoder:- Unsupervised learning | Does not need label
------------------
* Dimensioanlity reduction by ignoring the noise 
* Reconstruction is learn generate the output close to input

2 components:
1.an encoder that maps the input into the code, 
2.Code
3.and a decoder that maps the code to a reconstruction of the original input.

input layer--> Code -->Output layer

encoder = input + code
decoder = code + output

h= activationfunction(W*x+b)
 h = hidden layer
 W = weight
 x = input
 b= bias
 
 weights and biases are intilized randomly and updated iteratively during backpropagation
 
 decoded stage of autoencoder maps h 
 x' is same shape as x
  
 x' = Another Activation function (W'*h +b')
 
 loss can be calculated as  L(x,x') = ||x - x'||^2
 This is squared error
  The output is compressed version of input.
 
 Types of Autoencoder:-
 -----------------------------
 1.Sparce Autoencoder :
 -------------------
	* sparicity improves performance
	* small no of hidden unit are allowed active at once
	* sparcity activation can be acieved by 
		 * Kullback - Elibler divergence 
		 * L1 and L2 regurization
	
2.Denoising autoencoder :DAE
------------------
		* DAE takes partially corrupted input and trined to recover original distorted input
		* denoising 

3.Contractive Encoder : CAE
------------------
	* adds an explicit regularizer in their objective function so the output 
	* would be slight variation from input

4.Variational AutoEncoder: VAE
---------------
	* like Genrative Adversial Network
	* generative model
	* directed probabilistic graphical model
	* generative model tries to simulate how the data is generated - 
	  inorder to understand underlying causal relation.
	* VAE learn - distribution of latent variable (Hidden variable generated during process)
	  Latent variables learning  + loss +estimator  process is called 
	  stochastic Gradient Variantional Bayes
	
Application of AE:-
---------------
* Dimensioanlity Reduction
* Relation to PCA
	* Linear Activation  + single sigmoid hidden layer behave as PCA
* Information retrival
	* through hashing  
* Anomaly Detection 
	* replicate  most salient features in training data 
	* generally anomaly is small error in. so genric model can not capture small variation
* Image processing 	
		
 Examaple Code: [Autoencoder](https://github.com/soumya-mishra/Python-ML/blob/master/Autoencoder.ipynb)
