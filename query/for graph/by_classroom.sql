select count([Event].[id]), 
	([Address].[address] + ', ' + [Classroom].[name]),  
	--/* day */ (convert(date, [Event].[start]))
	--/* month */ (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
	--/* year */ year([Event].[start])
from [Event],
	[Classroom],
	[Address],
	[EventLocation]
where [Classroom].[address] = [Address].[id]
and [Classroom].[id] = [EventLocation].[classroom]
and [EventLocation].[event] = [Event].[id]
and [Event].[id] in (/* list id in '' separated by , */)
--/* for day */ group by (convert(date, [Event].[start])), ([Address].[address] + ', ' + [Classroom].[name]) 
--/* for month */ group by (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start]))) , ([Address].[address] + ', ' + [Classroom].[name]) 
--/* for year */ group by year([Event].[start]), ([Address].[address] + ', ' + [Classroom].[name])