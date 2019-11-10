from utility import db_mediator_instance

Model = db_mediator_instance.Model


def search_records(field, field_type, value, db_file):
    db = db_mediator_instance.get_db(db_file)
    if field_type == 'int':
        try:
            value = int(value)
        except(ValueError, Exception):
            pass
        return db.search(Model[field] == value)
    elif field_type == 'string':
        return db.search(Model[field] == value)
    elif field_type == 'list':
        return db.search(Model[field].any([value]))
    return []
