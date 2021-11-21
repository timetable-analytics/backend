select count([Event].[id]), 
	[Educator].[full_name],  
	--/* day */ (convert(date, [Event].[start]))
	--/* month */ (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
	--/* year */ year([Event].[start])
from [Event],
	[Educator],
	[EducatorAssigmentUnit],
	[EducatorEmployment]
where [Educator].[id] = [EducatorEmployment].[educator]
and [EducatorEmployment].[id] = [EducatorAssigmentUnit].[educator_employment]
and [EducatorAssigmentUnit].[educator_assigment] = [Event].[educator_assigment]
and [Event].[id] in (/* list id in '' separated by , (for example '1', '2')*/)
--/* for day */ group by (convert(date, [Event].[start])), [Educator].[full_name]
--/* for month */ group by (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start]))) , [Educator].[full_name] 
--/* for year */ group by year([Event].[start]), [Educator].[full_name]
--/* for day */ order by [Educator].[full_name], (convert(date, [Event].[start]))
--/* for month */ order by [Educator].[full_name], (convert(varchar,year([Event].[start])) + '-' + convert(varchar,month([Event].[start])))
--/* for year */ order by [Educator].[full_name], year([Event].[start])
