Graph-DR: Benchmarking of dimensionality reduction algorithms
==============

A series of Jupyter Notebooks experimenting on different dimensionality reduction algorithms and their performance on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). 

Get started
------------

There are two options to run the notebooks in this repository:

### 1. Docker

First find the IP address of the Docker machine by:
    
    docker-machine ip

Then, start to run the docker image:

    docker run -it -p 80:8888 --add-host="localhost:10.0.2.2" maayanlab/graph-dr

Next, you can open a browser and go to the IP address of your Docker machine, which is usually http://192.168.99.100. You can find the token in the terminal running the Docker image.


### 2. virtualenv

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

To run the firework layout, you will also need to install the a Cytoscape app [AllegroLayout](https://www.dropbox.com/s/uwcpjes6vv212fm/allegrolayout-2.2.2.jar?dl=0). Once the jar file is downloaded, go to `Apps` -> `Install from File` -> open the jar file.


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
