import datetime
from pytz import timezone
import os


jtl_file_location = os.path.join(os.getcwd(), 'Jmeter_log2.jtl') # log file location



with open(jtl_file_location, "r") as fp: # Reading the log file
    all_lines = fp.readlines()
    column_names = all_lines[0].split(",") # finding column names
    
    for line in all_lines[1:]: # iterating through all the rows excluding first
        values = line.split(",") # splitting the values by ","
        
        if values[3] != "200": # checking if response code is not 200
        
            time = datetime.datetime.fromtimestamp(int(values[0])/1000)  # converting the time stamp
            
            time = time.astimezone(timezone('US/Pacific')) # setting up the time stamp zone
            
            # printing the values
            print("***********************")
            print("label : ", values[2])
            print("response code : ", values[3])
            print("response message : ",values[4])
            print("failure message : ",values[8])
            print("time : ",time.strftime("%Y-%m-%d %H:%M:%S %Z"))
            print("***********************")