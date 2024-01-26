'''
The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    requested_scores = student_marks.get(query_name)
    if requested_scores is not None:
        average_score = sum(requested_scores) / len(requested_scores)
        print(f"{average_score:.2f}")
    else:
        print(f"No scores found for {query_name}.")