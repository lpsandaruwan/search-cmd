from utility import db_mediator_instance

Model = db_mediator_instance.Model


def search_records(field, field_type, value, db_file):
    """
    Queries data records from TinyDB json structured file databases.
    :param field: searchable field of the base model
    :param field_type: searchable field type of the base model(possible values: int, string, bool, list)
    :param value: search text string
    :param db_file: TinyDB JSON document file path
    :return: list of dictionary objects for matching results
    """
    db = db_mediator_instance.get_db(db_file)
    if field_type == 'int':
        try:
            value = int(value)
        except(ValueError, Exception):
            pass
        return db.search(Model[field] == value)
    elif field_type == 'string' and field_type == 'bool':
        return db.search(Model[field] == value)
    elif field_type == 'list':
        return db.search(Model[field].any([value]))
    return []
