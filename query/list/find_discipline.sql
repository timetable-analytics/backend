use local_db
select [Discipline].[name]
from [Discipline]
group by [Discipline].[name] --так как есть повторы
order by [Discipline].[name]