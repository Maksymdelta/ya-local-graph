# -*- coding: utf-8 -*-

import logging
import pickle
import os

import igraph

from app.config import SHORT_GRAPH_FILE, SHORT_GRAPH_PLOT_FILE, FULL_GRAPH_FILE, FULL_GRAPH_PLOT_FILE


def cache_name(name):
    return '%s.cache' % name


def clear_cache(name):
    cache_path = cache_name(name)
    if os.path.exists(cache_path):
        os.remove(cache_path)


def read_cache(name):
    cache_path = cache_name(name)
    l = None
    try:
        with open(cache_path, 'rb') as f:
            l = pickle.load(f)
    except:
        pass
    return l


def save_cache(name, l):
    cache_path = cache_name(name)
    f = open(cache_path, 'wb')
    pickle.dump(l, f)


def plot(g, name, name_g):
    kwargs = dict(bbox=(10000, 10000), edge_arrow_size=0.3, edge_arrow_width=0.9, edge_width=0.3, vertex_frame_width=0.4)

    l = read_cache(name_g)
    if not l:
        l = g.layout('fr')
        save_cache(name_g, l)

    logging.info('compute layout')

    igraph.plot(g, name % '1', vertex_size=3, vertex_label_size=7, layout=l, **kwargs)
    logging.info('plot graph base')

    g.vs['label'] = ['']
    igraph.plot(g, name % 2, vertex_size=7, layout=l, **kwargs)
    logging.info('plot graph w/ labels')


def task():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('start')

    g = igraph.Graph.Read_GML(SHORT_GRAPH_FILE)
    logging.info('load short %d %d', g.vcount(), g.ecount())
    plot(g, SHORT_GRAPH_PLOT_FILE, SHORT_GRAPH_FILE)
    logging.info('plot short')

    g = igraph.Graph.Read_GML(FULL_GRAPH_FILE)
    logging.info('load full %d %d', g.vcount(), g.ecount())
    plot(g, FULL_GRAPH_PLOT_FILE, FULL_GRAPH_FILE)
    logging.info('plot full')


