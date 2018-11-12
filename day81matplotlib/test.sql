select a.user_id, a.movie_id, a.ratings, c.gender, b.title
from ratings a inner join movies b
on a.movie_id = b.movie_id
inner join users c
on a.user_id = c.user_id;

select b.title, count(*)
from ratings a inner join movies b
on a.movie_id = b.movie_id
group by b.title


student
(id, name)

teacher
(id, name)

lesson
(id, name)

teacher_lesson
(id, teacher_id, lesson_id)

student_lesson
(id, student_id, lesson_id)

select *
from student  
where id in 
(select student_id from student_lesson where lesson_id in 
  (select lesson_id from teacher_lesson where teacher_id in 
    (select id from teacher where name = '张三')
  )
)

select a.*
from student a inner join student_lesson b
on a.id = b.student_id
inner join teacher_lesson d
on b.lesson_id = d.lesson_id
inner join teacher e
on d.teacher_id = e.id
where e.name = '张三'


##创建查询表
create table temp_ratings select movie_id, ratings from ratings;
##在表存在的情况下插入数据
insert into temp_ratings2 (movie_id,ratings) select movie_id,ratings from ratings where ratings <=3;


create view 
存储过程
触发器