"""
Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)
Scenario
A server records raw access events as unformatted plain-text log lines. You need to parse the log lines into structured records and export
them to both CSV and JSON formats.

Problem Description
Create a function convert_log_file(input_log_path, output_csv_path, output_json_path):

Each line in input_log_path follows the format: "<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>" (e.g., "2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200").
Parses each line into a dictionary containing keys: timestamp, user_id, endpoint, status_code (as integer).
Writes all parsed records to output_csv_path with a header row using csv.DictWriter.
Writes the list of records to output_json_path with an indentation of 2 spaces using json.dump().
Example Walkthrough
convert_log_file("server_access.log", "access_records.csv", "access_records.json")
"""

import csv
import json

def convert_log_file(input_log_path, output_csv_path, output_json_path):
    records = []

    with open(input_log_path, 'r', encoding='utf-8') as log_file:
        for line in log_file:
            stripped_line = line.strip()
            if not stripped_line:
                continue
        
            parts = [p.strip() for p in stripped_line.split('|')]
            
            if len(parts) == 4:
                record = {
                    'timestamp': parts[0],
                    'user_id': parts[1],
                    'endpoint': parts[2],
                    'status_code': int(parts[3])
                }
                records.append(record)
                
    fieldnames = ['timestamp', 'user_id', 'endpoint', 'status_code']
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(records, json_file, indent=2)

# Using relative paths for easy directory usage
convert_log_file("c:\Users\DBDA19\Downloads\Ganesh\25023_Ganesh_A07\server_access.txt", "access_records.json")
