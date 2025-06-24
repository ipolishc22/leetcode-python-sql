-- 1280 Students and Examinations
SELECT Students.student_id, student_name, Subjects.subject_name, COUNT(Examinations.subject_name) AS attended_exams
FROM Students
JOIN Subjects
LEFT JOIN Examinations ON Students.student_id = Examinations.student_id 
AND Subjects.subject_name = Examinations.subject_name
GROUP BY 1, 2, 3
ORDER BY 1, 3