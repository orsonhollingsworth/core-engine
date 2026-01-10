# utils.py

import os
import logging
import pickle
import json

logger = logging.getLogger('core-engine.utils')

def load_json(file_path):
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist")
        return None
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {file_path}: {e}")
        return None

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def load_pickle(file_path):
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist")
        return None
    
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except pickle.UnpicklingError as e:
        logger.error(f"Failed to unpickle from {file_path}: {e}")
        return None

def save_pickle(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)