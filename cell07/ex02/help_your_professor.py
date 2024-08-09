#!/usr/bin/env python3
def average(scores_dict):
    
    if not scores_dict:
        return 0
    
    
    total_score = sum(scores_dict.values())
    
    
    number_of_students = len(scores_dict)
    
    
    avg_score = total_score / number_of_students
    
    return avg_score

scores_dict = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'Diana': 92
}

print(f"Average for class 3B: {average(scores_dict)}.")
print(f"Average for class 3C: {average(scores_dict)}.")