select count([Event].[id]), 
	[Discipline].[name],  
	--/* day */ (convert(date, [Event].[start]))
	--/* month */ (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
	--/* year */ year([Event].[start])
from [Event],
	[Discipline]
where [Discipline].[id] = [Event].[discipline]
and [Event].[id] in (/* list id in '' separated by , */)
--/* for day */ group by (convert(date, [Event].[start])), [Discipline].[name]
--/* for month */ group by (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start]))) , [Discipline].[name] 
--/* for year */ group by year([Event].[start]), [Discipline].[name]
--/* for day */ order by [Discipline].[name], (convert(date, [Event].[start]))
--/* for month */ order by [Discipline].[name], (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
--/* for year */ order by [Discipline].[name], year([Event].[start])