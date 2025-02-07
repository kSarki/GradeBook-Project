import os

MAX_TEST_SCORES = 5  

def read_data(filename):
    
    names = []
    scores = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if len(data) < 2:
                    continue 
                names.append(data[0])
                scores.append([int(score) for score in data[1:MAX_TEST_SCORES + 1]])  
    except FileNotFoundError:
        print("Error: File not found.")
        return [], []
    return names, scores

def calculate_averages(scores):
    
    averages = []
    for score_list in scores:
        if len(score_list) == 0:
            averages.append(0)
        else:
            averages.append(sum(score_list) / len(score_list))
    return averages

def get_letter_grade(average):
    
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def print_report(names, averages):
   
    print("{:<15} {:<10} {:<10}".format("Name", "Average", "Grade"))
    print("-" * 35)
    for i in range(len(names)):
        print("{:<15} {:<10.2f} {:<10}".format(names[i], averages[i], get_letter_grade(averages[i])))
    print(f"Total students: {len(names)}")  

def main():
    filename = "students.txt"
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist. Please provide the correct file.")
        return

    names, scores = read_data(filename)
    if not names:
        print("No data found in the file.")
        return

    averages = calculate_averages(scores)
    print_report(names, averages)

main()


