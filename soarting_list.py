def soarting_list(custom_list=None, key_comparator=None, default_label=None, **kwargs):
    """
    This custom function is used to "sort" ingested/created containers to different labels by using a custom list in SOAR as a dictionary. The key in the dictionary is what you want to match on (i.e. a unique string in the container name or a field in an artifact) the value being the new label you want to change the container to.
    
    Args:
        custom_list: Input the NAME of the custom list you created that should be 2 columns wide; in the format of key and value pairs. 
            
            The key in the custom list column should be the string you want to match on in the "key comparator" datapath, such as part of a container name or a field in an artifact. The value should be the new label you want the container to change to.
        key_comparator: Input the datapath that the "Key" in your custom list will check against. (I.e. this can be the container name or a field in an artifact)
        default_label (CEF type: phantom container label): Input the default SOAR Label this custom function will output, in case sorting fails. 
    
    Returns a JSON-serializable object that implements the configured data paths:
        new_label (CEF type: phantom container label): This is the new Label that is output as a result of the sorting. If the sorting fails, it will be the default Label you specified as an input.
    """
    ############################ Custom Code Goes Below This Line #################################
    
    # Custom Function written by Jonathan Gavris
    import json
    import phantom.rules as phantom
    
    phantom.debug("---------------------")
    phantom.debug("Custom List:")
    phantom.debug(custom_list)
    phantom.debug("Key Comparator:")
    phantom.debug(key_comparator)
    phantom.debug("---------------------")
    phantom.debug("#####################")
    
    # Grab custom list specified by the <custom_list> input
    custom_list_api_call = phantom.get_list(list_name=custom_list, values=None, column_index=-1, trace=False)
    
    # Convert output to a dict
    key_plus_label_list = custom_list_api_call[2]
    key_plus_label_dict = {key.lower(): value for key, value in key_plus_label_list}
    
    phantom.debug("---------------------")
    phantom.debug("Key + Label in a list:")
    phantom.debug(key_plus_label_list)
    phantom.debug("---------------------")
    phantom.debug("Key + Label converted to a dictionary:")
    phantom.debug(key_plus_label_dict)
    phantom.debug("---------------------")
    phantom.debug("#####################")
    
    # If the provided <key_comparator> matches anything from the list, return it.
    # Otherwise return <default_label>
    if key_comparator:
        key_comparator = key_comparator.lower()


    output_label = None
    for key, label in key_plus_label_dict.items():
        # Match if key is in any part of key_comparator
        if key.lower() in key_comparator:
            output_label = label
            break
    if not output_label:
        output_label = default_label
    
    outputs = {
        'new_label': output_label
    }
    
    # -------------------------------------
    # If you want to let this custom function automatically switch the label without having to use a second custom function in the playbook, uncomment this code:
    phantom.set_label(label=output_label)
    # -------------------------------------
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
