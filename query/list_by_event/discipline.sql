select [Discipline].[id], [Discipline].[name]
from [Discipline], [Event]
where [Event].[discipline] = [Discipline].[id]
and [Event].[id] in (/* list id in '' separated by , (for example '1', '2')*/)
group by [Discipline].[id], [Discipline].[name]
order by [Discipline].[name]
