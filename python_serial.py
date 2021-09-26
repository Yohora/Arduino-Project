from pandas.core.frame import DataFrame
import serial
import csv
import time
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import os.path
 
Arduino = serial.Serial('COM3',9600)
Arduino.close()
Arduino.open()

temp_exists = os.path.isfile('test_temperature_data.csv')

def temp_data():
    while True:
        try:
            data = Arduino.readline()
            b_strip = data.decode('utf-8')
            decoded_bytes = np.array(b_strip.rstrip(), dtype=float)
        except:
            continue


        with open("./Temperature_Project-master/test_temperature_data.csv","a", newline ='') as f:
            headers = ['Time', 'Temperature (\u00B0C)']
            time_index = time.strftime('%H:%M:%S')
            file_is_empty = os.stat('./Temperature_Project-master/test_temperature_data.csv').st_size == 0
            writer = csv.DictWriter(f,delimiter=",", lineterminator = '\n', fieldnames=headers)

            if file_is_empty:
                writer.writerow(headers)
            writer.writerow({'Time': time_index, 'Temperature (\u00B0C)': decoded_bytes})  


temp_data()


