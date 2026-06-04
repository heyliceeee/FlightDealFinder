from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from a sheet
pprint(sheet_data) # pretty print