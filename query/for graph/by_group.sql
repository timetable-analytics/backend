select count([Event].[id]), 
	[Group_union].[name],  
	--/* day */ (convert(date, [Event].[start]))
	--/* month */ (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
	--/* year */ year([Event].[start])
from [Event],
	[Group_union]
where [Group_union].[id] = [Event].[group_union]
and [Event].[id] in (/* list id in '' separated by , */)
--/* for day */ group by (convert(date, [Event].[start])), [Group_union].[name]
--/* for month */ group by (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start]))) , [Group_union].[name] 
--/* for year */ group by year([Event].[start]), [Group_union].[name]
--/* for day */ order by [Group_union].[name], (convert(date, [Event].[start]))
--/* for month */ order by [Group_union].[name], (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
--/* for year */ order by [Group_union].[name], year([Event].[start])