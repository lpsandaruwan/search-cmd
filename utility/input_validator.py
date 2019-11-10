from config import MODELS


def validate_model_index_and_get_model(model_index):
    converted_index = 0
    try:
        converted_index = int(model_index)
    except(ValueError, Exception):
        return False, []
    filtered_models = [model for model in MODELS if model['index'] == converted_index]
    if len(filtered_models) == 0:
        return False, None
    elif len(filtered_models) == 1:
        return True, filtered_models[0]
    else:
        return False, filtered_models


def validate_field_and_get_field_type(model, field_name):
    for field in model['fields']:
        if field == field_name:
            return field_name, model['fields'][field]
    return None, None
