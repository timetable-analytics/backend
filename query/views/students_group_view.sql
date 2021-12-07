create view Students_group_view
as
	select [Group_union].[id] as [id], 
		[Division].[name] as [division], 
		[Group_union].[name] as [group], 
		[Group_union].[course] as [course]
	from [Group_union]
	inner join [Group_union_Division] on [Group_union].[id] = [Group_union_Division].[group_union]
	inner join [Division] on [Division].[id] = [Group_union_Division].[division]