result = [
    {student_id: {name: grade}}
    for student_id, name, grade in zip(
        student_ids, student_names, student_grades
    )
]
print(result)
