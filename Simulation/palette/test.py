from importlib import import_module
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
feature_func = 'packets_per_slot'
fun = import_module('FeatureExtraction.' + feature_func)