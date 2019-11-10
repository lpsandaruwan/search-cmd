import logging
import os

import ijson

from config import MODELS
from utility.db_mediator import db_mediator_instance


def initialize_query_data():
    """
    Initializes TinyDB document data store files for the given base models using given JSON files.
    :return: None
    """
    logging.debug("Please wait while creating database for querying...")
    for model in MODELS:
        logging.debug("Started indexing %s data for querying" % model['model'])
        if model['data_reset_on_startup']:
            try:
                if os.path.exists(model['query_db_file']):
                    open(model['query_db_file'], 'w').close()
            except (FileNotFoundError, IOError):
                logging.error("File does not exists for cleanup %s" % model['query_db_file'])
                pass
        db = db_mediator_instance.get_db(model['query_db_file'])
        with open(model['init_data_file'], 'rb') as input_json_file:
            json_object_stream = ijson.items(input_json_file, 'item')
            current_chunk_size = 0
            json_objects_chunk = []
            for json_object in json_object_stream:
                if current_chunk_size == 100:
                    db.insert_multiple(json_objects_chunk)
                    json_objects_chunk = []
                    current_chunk_size = 0
                json_objects_chunk.append(json_object)
                current_chunk_size = current_chunk_size + 1
            if len(json_objects_chunk) > 0:
                db.insert_multiple(json_objects_chunk)
        logging.debug("Successfully indexed %s data for querying" % model['model'])
