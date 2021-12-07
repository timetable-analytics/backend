create view Classroom_view
as
	select [Classroom].[id] as [id], 
		[Address].[address] as [address], 
		[Classroom_kind].[name] as [classroom_kind], 
		[Classroom].[name] as [classroom]
	from [Classroom]
		inner join [Classroom_kind] on [Classroom_kind].[id] = [Classroom].[classroom_kind]
		inner join [Address] on [Address].[id] = [Classroom].[address]