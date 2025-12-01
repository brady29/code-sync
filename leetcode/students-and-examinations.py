# Write your MySQL query statement b
select s.student_id, s.student_name,e.subject_name,ifnull(count(*),0) as attended_exams
from Examinations E
Join Students S on E.student_id = S.student_id
Group by e.subject_name,s.student_name
ORDER by student_id, subject_name