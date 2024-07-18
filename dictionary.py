from tabulate import tabulate
#Data in dictionary format
data = [
    {'stdid': 'std01', 'StdName': 'Ashish Kumar', 'standard': '10th', 'Age': 15, 'hindi': 67, 'english': 89, 'math': 87, 'Science': 89, 'Computer': 90, 'Total': 422},
    {'stdid': 'std02', 'StdName': 'Abhishek Kumar', 'standard': '10th', 'Age': 14, 'hindi': 85, 'english': 45, 'math': 48, 'Science': 90, 'Computer': 45, 'Total': 313},
    {'stdid': 'std03', 'StdName': 'Aman', 'standard': '10th', 'Age': 15, 'hindi': 23, 'english': 56, 'math': 78, 'Science': 78, 'Computer': 67, 'Total': 302},
    {'stdid': 'std04', 'StdName': 'Rahul', 'standard': '10th', 'Age': 14, 'hindi': 45, 'english': 67, 'math': 45, 'Science': 45, 'Computer': 56, 'Total': 258},
    {'stdid': 'std05', 'StdName': 'Ruby', 'standard': '10th', 'Age': 13, 'hindi': 89, 'english': 67, 'math': 89, 'Science': 93, 'Computer': 65, 'Total': 403},
    {'stdid': 'std06', 'StdName': 'Suman', 'standard': '10th', 'Age': 13, 'hindi': 90, 'english': 46, 'math': 67, 'Science': 67, 'Computer': 67, 'Total': 337},
    {'stdid': 'std07', 'StdName': 'Saurabh', 'standard': '10th', 'Age': 15, 'hindi': 45, 'english': 23, 'math': 34, 'Science': 45, 'Computer': 34, 'Total': 181},
    {'stdid': 'std08', 'StdName': 'Sumit', 'standard': '10th', 'Age': 14, 'hindi': 23, 'english': 45, 'math': 67, 'Science': 78, 'Computer': 90, 'Total': 303},
    {'stdid': 'std09', 'StdName': 'Kamlesh', 'standard': '10th', 'Age': 15, 'hindi': 45, 'english': 56, 'math': 78, 'Science': 99, 'Computer': 67, 'Total': 303},
    {'stdid': 'std10', 'StdName': 'Rohan', 'standard': '10th', 'Age': 15, 'hindi': 34, 'english': 12, 'math': 24, 'Science': 45, 'Computer': 56, 'Total': 171},
]
# Filter students with English marks greater than 50
print(tabulate(data[1:], tablefmt= 'grid'))
for student in data:
    if student["english"] > 50:
        print(student['StdName'])
      
# Sort data based on 'Total' marks in descending order
sorted_data = sorted(data, key=lambda x: x['Total'], reverse=True)

# Display names and ages of top 4 scorers
print("Top 4 scorers:")
for i, student in enumerate(sorted_data[:4], 1):
    print(f"{i}. Name: {student['StdName']}, Age: {student['Age']}")