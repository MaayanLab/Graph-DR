# modules to interact with CyREST, the API of Cytoscape
import json
import requests
from py2cytoscape.data.cyrest_client import CyRestClient
import py2cytoscape.cytoscapejs as renderer


# Params for CyREST
IP = 'localhost'
PORT = 1234
BASE_URL = 'http://%s:%s/v1' % (IP, PORT)
HEADERS = {'Content-Type': 'application/json'}

def network_force_directed_layout(G):
    '''POST the network to CyREST, then run layout algorithm, 
    finally return the coordinates and the cy_network.
    '''
    # Create Py2cytoscape client
    cy = CyRestClient(ip=IP, port=PORT)
    # Reset session
    cy.session.delete()
    # POST the graph to CyREST
    G_cy = cy.network.create_from_networkx(G)

    # Change the layout params
    layout_parameters = [
        {"name": "numIterations", "value": 500}, 
        {"name":"numIterationsEdgeRepulsive", "value":500}
    ]
    resp = requests.put(BASE_URL+ '/apply/layouts/force-directed-cl/parameters', 
                 data=json.dumps(layout_parameters),
                 headers=HEADERS)
    cy.layout.apply(name='force-directed-cl', network=G_cy)

    # Get current view
    view = G_cy.get_first_view()
    nodes = view['elements']['nodes']
    # Get a coord matrix ordered by id_original
    ids_original = np.array([n['data']['id_original'] for n in nodes]).astype(np.int32)
    xs = [n['position']['x'] for n in nodes]
    ys = [n['position']['y'] for n in nodes]
    coords = np.array([xs, ys]).T
    return coords[ids_original], G_cy
    

def network_firework_layout(G):
    '''POST the network to CyREST, then run layout algorithm, 
    finally return the coordinates and the cy_network.
    '''
    # Create Py2cytoscape client
    cy = CyRestClient(ip=IP, port=PORT)
    # Reset session
    cy.session.delete()
    # POST the graph to CyREST
    G_cy = cy.network.create_from_networkx(G)

    # Change the layout params
    layout_parameters = [
        {"name": "numIterations", "value": 10}, 
        {"name":"numIterationsEdgeRepulsive", "value":10}
    ]
    resp = requests.put(BASE_URL+ '/apply/layouts/force-directed-cl/parameters', 
                 data=json.dumps(layout_parameters),
                 headers=HEADERS)
    cy.layout.apply(name='force-directed-cl', network=G_cy)


    layout_parameters = [
        {"name": "maxIterations", "value": 10000}, 
        {"name":"randomize", "value":True},
    ]
    resp = requests.put(BASE_URL+ '/apply/layouts/allegro-edge-repulsive-strong-clustering/parameters', 
                 data=json.dumps(layout_parameters),
                 headers=HEADERS)
    cy.layout.apply(name='allegro-edge-repulsive-strong-clustering', network=G_cy)
    # Get current view
    view = G_cy.get_first_view()
    nodes = view['elements']['nodes']
    # Get a coord matrix ordered by id_original
    ids_original = np.array([n['data']['id_original'] for n in nodes]).astype(np.int32)
    xs = [n['position']['x'] for n in nodes]
    ys = [n['position']['y'] for n in nodes]
    coords = np.array([xs, ys]).T
    return coords[ids_original], G_cy
    