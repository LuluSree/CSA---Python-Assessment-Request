import os
import json


def update_json(key_word : str):
    """
    Removes the given element in the json file and saves it to a new file.
    
    Parameters:
    key_word: str
    
    """

    json_input_location = os.path.join(os.getcwd(), 'test_payload.json') # input json file
    json_output_location = os.path.join(os.getcwd(), 'test_payload_out.json') # output json file
    
    
    with open(json_input_location, 'r') as data_file: # reading input json file
        data = json.load(data_file) # converting to dictionary 
    
    
    for k ,v in list(data.items()): # iterating dictionary objects
        if key_word == k : # checking if dictionary key is a key_word
            del data[key_word] # deleting the element
            
        if type(v) is dict and key_word in v.keys(): # cheking if dictionary value as the key_word
            del v[key_word] # deleting the element
            data[k] = v # reassigning the value
            
    with open(json_output_location, 'w') as data_file: # writing to a new json file
        data = json.dump(data, data_file)


element = "outParams"

# calling the method
update_json(element)


