"""
Assignment 6: Server Log Analyzer & Traffic Classifier (Advanced RegEx)
Scenario
An automated server monitor analyzes web traffic logs to detect security issues. The monitor extracts HTTP details from log strings and filters out requests originating from local network IP addresses.

Problem Description
Write a function analyze_server_logs(logs_text) that parses web logs:

logs_text is a multi-line string containing server logs. Each log line matches this exact format: "<IP> - - [<timestamp>] \"<HTTP_METHOD> <URL> <HTTP_VERSION>\" <STATUS_CODE> <BYTES>" Example: "192.168.1.5 - - [28/Aug/2026:10:00:00] \"GET /index.html HTTP/1.1\" 200 1024"
The function must perform the following:
Compile a single regular expression using named capture groups to extract:
ip: The source IP address.
time: The timestamp value inside the brackets [].
method: The HTTP method (GET, POST, PUT, DELETE).
resource: The URL route value (e.g., /index.html).
status: The integer status code.
bytes: The integer bytes sent.
Parse the input logs_text line-by-line using your regex. If a line does not match the format, print a warning: "Warning: Could not parse line: '<line>'. Skipping." and continue to the next line.
Local IP Address Filtering:
Check the extracted IP address. If the IP starts with "192.168." or "10.", it is classified as a local network request.
Filter out and ignore local network requests; do not include them in the final list.
For external request logs, compile a dictionary containing: {"ip": ip, "time": time, "method": method, "resource": resource, "status": status_code, "bytes": bytes_sent} (Note: status and bytes must be stored as integers).
Return a list of these dictionaries.
Sample Input
"""
"""
log_data =""" """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""

import re
import pprint 
def analyze_server_logs(logs_text):
    
   pattern = re.compile(
        r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+'
        r'\[(?P<time>[^\]]+)\]\s+'
        r'(?P<method>GET|POST|PUT|DELETE)\s+'
        r'(?P<resource>\S+)\s+'
        r'HTTP/\d\.\d\s+'
        r'(?P<status>\d+)\s+'
        r'(?P<bytes>\d+)$'
    )
    
   results = []
    
   for line in logs_text.strip().splitlines():
      match = pattern.match(line)
      if not match:
         print(f"Warning: Could not parse line: {line}. Skipping.")
         continue
            
      data = match.groupdict()
      ip = data['ip']
        
      if ip.startswith('192.168.') or ip.startswith('10.'):
         continue
            
      results.append({
            'ip': ip,
            'time': data['time'],
            'method': data['method'],
            'resource': data['resource'],
            'status': int(data['status']),
            'bytes': int(data['bytes'])
        })
        
   return results

log_data = """
192.168.1.5 - - [28/Aug/2026:10:00:00] GET /index.html HTTP/1.1 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] GET /api/v1/users HTTP/1.1 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] POST /submit_data HTTP/1.1 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] POST /login HTTP/1.1 401 256
"""
output = analyze_server_logs(log_data)

pprint.pprint(output)