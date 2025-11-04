# Write your MySQL query stat
Select w1.id as Id from Weather as w1 join Weather as w2 on w2.recordDate = Date_sub(w1.recordDate,INTERVAL 1 DAY) Where w1.temperature > w2.temperature