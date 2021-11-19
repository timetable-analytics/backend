use local_db
select [Discipline].[id], [Discipline].[name]
from [Discipline]
where [Discipline].[name] like '%%'
order by [Discipline].[name]
