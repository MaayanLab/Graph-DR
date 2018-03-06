Graph-DR: Benchmarking of dimensionality reduction algorithms
==============

A series of Jupyter Notebooks experimenting on different dimensionality reduction algorithms and their performance on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). 

Installation
------------

The recommended way to run these notebooks live is to set up a isolated Python envrionment using [virtualenv](https://virtualenv.pypa.io/en/stable/), after cloning this repository:

    git clone https://github.com/MaayanLab/Graph-DR.git
    cd Graph-DR/

Run the following to set up a Python virtural environment:

    virtualenv venv

Then activate the virtural environment and install the required Python packages:

    source venv/bin/activate
    pip install -r requirements.txt

Next, you can start a Jupyter server:

    jupyter notebook

Other dependencies
------------

Some code blocks in the notebooks require [Cytoscape](http://www.cytoscape.org/) (>3.5.1) to be running as the background. 


References
------------

+ [Making sense of principal component analysis, eigenvectors & eigenvalues](https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues)
+ [MNIST For ML Beginners](https://www.tensorflow.org/get_started/mnist/beginners)
+ [Visualizing MNIST: An Exploration of Dimensionality Reduction](http://colah.github.io/posts/2014-10-Visualizing-MNIST/)
+ [Tensorflow Embedding Projector](http://projector.tensorflow.org/)
+ [van der Maaten's t-SNE page](http://lvdmaaten.github.io/tsne/)
+ [van der Maaten et al.: Dimensionality Reduction: A Comparative Review](https://www.tilburguniversity.edu/upload/59afb3b8-21a5-4c78-8eb3-6510597382db_TR2009005.pdf)
+ [van der Maaten: Learning a Parametric Embedding by Preserving Local Structure](http://lvdmaaten.github.io/publications/papers/AISTATS_2009.pdf)
+ [Kokiopoulou and Saad: Enhanced graph-based dimensionality reduction with repulsion Laplaceans](http://www.sciencedirect.com/science/article/pii/S0031320309001460)
+ [UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction](https://arxiv.org/abs/1802.03426)
