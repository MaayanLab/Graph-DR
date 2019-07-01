FROM jupyter/tensorflow-notebook:5811dcb711ba

MAINTAINER Zichen Wang <zichen.wang@mssm.edu>

# Copy the application folder inside the container
ADD . /home/jovyan

# Install additional python packages
RUN pip install py2cytoscape \
	umap-learn==0.2.1 \
	python-igraph==0.7.1.post6

# Change the permissions for all notebooks
USER root
RUN chmod 777 *.ipynb

# Switch back the notebook user
USER $NB_UID
