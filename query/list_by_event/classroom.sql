select [Classroom].[id], 
	[Address].[address] + ', ' + [Classroom].[name], 
	[Classroom_kind].[name]
from [Address], 
	[Classroom], 
	[Classroom_kind], 
	[Event], 
	[EventLocation]
where [Classroom].[classroom_kind] = [Classroom_kind].[id]
and [Classroom].[address] = [Address].[id]
and [Event].[id] = [EventLocation].[event]
and [EventLocation].[classroom] = [Classroom].[id]
and [Event].[id] in (/* list id in '' separated by , */)
group by [Classroom].[id], [Address].[address] + ', ' + [Classroom].[name], [Classroom_kind].[name]
order by [Address].[address] + ', ' + [Classroom].[name]