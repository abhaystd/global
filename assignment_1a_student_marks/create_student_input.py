import pandas as pd

# Creates 'student.xlsx' with the sample data specified in the assignment.
def main():
    data = {
        "StudentID": [101, 102, 103, 104, 105, 106, 107],
        "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace"],
        "Math": [95, 72, 88, 55, 80, 99, 68],
        "Physics": [89, 65, 91, 62, 77, 95, 72],
        "Chemistry": [92, 70, 85, 58, 79, 97, 74],
        "Biology": [88, 60, 90, 61, 83, 96, 70],
    }
    df = pd.DataFrame(data)
    df.to_excel("student.xlsx", index=False)
    print("student.xlsx created")

if __name__ == "__main__":
    main()