FROM jupyter/tensorflow-notebook:5811dcb711ba

MAINTAINER Zichen Wang <zichen.wang@mssm.edu>

# Copy the application folder inside the container
ADD . /home/jovyan

# Install additional python packages
RUN pip install py2cytoscape \
	umap-learn==0.2.1 

