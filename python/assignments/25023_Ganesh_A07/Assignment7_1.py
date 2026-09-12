
"""
Assignment 1: Structured CSV & JSON Data Processor
Scenario
An academic registrar stores student course registrations in a CSV file. You need to read this file, 
compute overall statistics, and export a summarized JSON report.

Problem Description
Create a function process_student_records(input_csv_path, output_json_path):
Reads an input_csv_path containing columns: student_id, name, course, score.
Uses csv.DictReader inside a context manager to parse all rows.
Computes:
total_students: Total number of students processed.
average_score: Arithmetic mean of all student scores (rounded to 2 decimal places).
top_scorer: The dictionary {"name": <name>, "score": <score>} of the highest scoring student.
course_counts: A dictionary mapping each course name to the count of enrolled students.
Writes the summary dictionary into output_json_path formatted with an indentation of 4 spaces using json.dump().
Example Walkthrough
# Given input CSV:
# student_id,name,course,score
# 101,Arham,AI,88.5
# 102,Lisa,BDA,94.0
# 103,Vinod,AI,96.5

process_student_records("students.csv", "summary.json")

# Expected summary.json output:
# {
#     "total_students": 3,
#     "average_score": 93.0,
#     "top_scorer": {
#         "name": "Vinod",
#         "score": 96.5
#     },
#     "course_counts": {
#         "AI": 2,
#         "BDA": 1
#     }
# }


"""
import csv
import json

def process_student_records(input_csv_path, output_json_path):

    with open(input_csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        total_students = 0
        total_score = 0.0
        highest_score = -1.0
        top_scorer = {"name": "", "score": 0.0}
        course_counts = {}
        
        for row in reader:
            name = row['name']
            course = row['course']
            score = float(row['score'])
        
            total_students += 1
            total_score += score
    
            if score > highest_score:
                highest_score = score
                top_scorer = {
                    "name": name,
                    "score": score
                }
            
            if course in course_counts:
                course_counts[course] += 1
            else:
                course_counts[course] = 1
                
    if total_students == 0:
        average_score = 0.0
        top_scorer = {}
    else:   
        average_score = round(total_score / total_students, 2)
    
    summary_data = {
        "total_students": total_students,
        "average_score": average_score,
        "top_scorer": top_scorer,
        "course_counts": course_counts
    }
    
    with open(output_json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(summary_data, json_file, indent=4)
        


process_student_records("c:\Users\DBDA19\Downloads\Ganesh\25023_Ganesh_A07\students.csv", "summary.json")
