import os
import csv
import json

BASE_DIR = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path = f'{BASE_DIR}/third_party_lib/PowerLog3.0.exe'
new_path  = os.path.normpath(path)

def run_powerLog3(sleep):
    os.system(f"{new_path} -file power.csv -cmd sleep {sleep}")


def make_json(csvFilePath, jsonFilePath, sleep):
    # generate the system cpu power using the intel power gadget log3 application
    run_powerLog3(sleep)
    '''
        Function to convert a CSV to JSON
        Takes the file paths as arguments
    '''
    # create a dictionary
    data = []

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            if rows['Processor Power_0(Watt)'] == None:
                break
            data.append(rows)

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def get_process_power(sleep = 2):
    make_json("power.csv", "power.json", sleep)
    with open("power.json") as json_file:
        power_details = json.load(json_file)
    average_cpu_process_power = sum([float(power_detail['Processor Power_0(Watt)']) for power_detail in power_details])/ len(power_details)
    return average_cpu_process_power

