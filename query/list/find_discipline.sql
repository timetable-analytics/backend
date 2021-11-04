use local_db
select [Discipline].[name]
from [Discipline]
group by [Discipline].[name] --because there are repetitions
order by [Discipline].[name]