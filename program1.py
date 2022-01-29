import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import os

def update(X: int, Y: int):
    """
    updates the DEPART and RETURN in xml file and saves it to a new file.
    
    Parameters:
    X (int): X days from the current date
    Y (int): Y days from the current date
  
    """
    
    xml_location = os.path.join(os.getcwd(), 'test_payload1.xml') # input file 
    output_location = os.path.join(os.getcwd(), 'test_payload1_out.xml') # output file

    current_date = datetime.now()
    
    # getting new depart date 
    new_depart_date = (current_date+timedelta(days = X)).strftime("%Y%m%d")
    
    # getting new return date
    new_return_date = (current_date+timedelta(days = Y)).strftime("%Y%m%d")
    
    with open(xml_location) as fp: # opening the xml file
        tree = ET.parse(fp) # prasing the xml document.
        root = tree.getroot() # getting root elements
        
        for elem in root.iter(): #iterating the elements
            
            if elem.tag == "DEPART" : # checking if tag is DEPART
                elem.text = new_depart_date # updating the DEPART value
                
            elif elem.tag == "RETURN" : # checking if tag is RETURN
                elem.text = new_return_date # updating the RETURN value


        tree.write(output_location) # writing to the output new file.
        
# calling the method
update(2, 3)