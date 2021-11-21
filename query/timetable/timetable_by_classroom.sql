use local_db
select 	[Address].[address], 
		[Classroom].[name], 
		[Educator].[full_name], 
		[Discipline].[name], 
		[Group_union].[name], 
		(convert(nvarchar, [Event].[start]) + ' - ' + ltrim(right(convert(varchar(20), [Event].[end], 100), 7)))
from	[Address], 
		[Classroom], 
		[Educator], 
		[Discipline], 
		[Group_union], 
		[Event], 
		[EducatorEmployment],
		[EducatorAssigmentUnit],
		[EventLocation]
where [Address].[id] = [Classroom].[address]
and [Classroom].[id] = [EventLocation].[classroom]
and [EventLocation].[event] = [Event].[id]
and [EducatorEmployment].[educator] = [Educator].[id]
and [EducatorEmployment].[id] = [EducatorAssigmentUnit].[educator_employment]
and [Event].[educator_assigment] = [EducatorAssigmentUnit].[educator_assigment]
and [Event].[discipline] = [Discipline].[id]
and [Group_union].[id] = [Event].[group_union]
and [Classroom].[id] in (/* list id in '' separated by , (for example '1', '2')*/)
and convert(date, [Event].[start]) >= /*'yyy-mm-dd'*/
and convert(date, [Event].[end]) <= /*'yyyy-mm-dd'*/
