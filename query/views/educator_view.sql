create view Educator_view
as
	select distinct [Educator].[id] as id, 
		[Division].[name] as division, 
		[Educator].[full_name] as full_name, 
		[EducatorPosition].[name] as position, 
		[EducatorGroup].[name] as educator_group, 
		[EducatorEmployment].[is_active] as is_active
	from [Educator]
		inner join [EducatorEmployment] on [Educator].[id]=[EducatorEmployment].educator
		inner join [EducatorPosition] on [EducatorEmployment].[position]=[EducatorPosition].[id]
		inner join [EducatorGroup] on [EducatorGroup].[id] = [EducatorEmployment].[educator_group]
		inner join [EducatorDivision] on [EducatorEmployment].[id] = [EducatorDivision].[educator_employment]
		inner join [Division] on [Division].[id] = [EducatorDivision].[division]