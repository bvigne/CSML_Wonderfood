def handler(event, context):
    """ Append element if not in list or if unique field is False.
    """
    actual_list = event['list']
    elem_to_append = event['elem']
    unique = event.get('unique', False)
    if elem_to_append not in actual_list or not unique:
        actual_list.append(elem_to_append)
    return actual_list
