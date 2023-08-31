# services/real_time.py

import time

def real_time_data_updater(data_source_func, update_interval=10):
    while True:
        updated_data = data_source_func()
        print("Updated Data: ", updated_data)
        
        time.sleep(update_interval)
