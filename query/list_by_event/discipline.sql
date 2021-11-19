select [Discipline].[id], [Discipline].[name]
from [Discipline], [Event]
where [Event].[discipline] = [Discipline].[id]
and [Event].[id] in (/* list id in '' separated by , */)
group by [Discipline].[id], [Discipline].[name]
order by [Discipline].[name]