from config import MODELS


def validate_model_index_and_get_model(model_index):
    """
    Validates user input for base models stated in config.MODELS
    :param model_index: index number of the base model
    :return: returns True, base_model_object on match found, and False on no match found and multiple matches found
    """
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
    """
    Validates whether field type exists in model for search and returns field type
    :param model: base model structure stated in config.MODELS
    :param field_name: given field_name to check whether it exists in base model
    :return: returns field_name and model data type on match found
    """
    for field in model['fields']:
        if field == field_name:
            return field_name, model['fields'][field]
    return None, None
