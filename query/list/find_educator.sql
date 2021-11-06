use local_db
select [Educator].[id], [Division].[name], [Educator].[full_name], [EducatorPosition].[name], [EducatorGroup].[name]
from [Division], [Educator], [EducatorPosition], [EducatorGroup], [EducatorEmployment], [EducatorDivision]
where [Division].[id] = [EducatorDivision].[division]
and [Educator].[id] = [EducatorEmployment].[educator]
and [EducatorPosition].[id] = [EducatorEmployment].[position]
and [EducatorGroup].[id] = [EducatorEmployment].[educator_group]
and [EducatorEmployment].[id] = [EducatorDivision].[educator_employment]
and [EducatorEmployment].[is_active] = 1
and [Division].[name] like '%%'
and [Educator].[full_name] like '%%'
and [EducatorPosition].[name] like '%%'
and [EducatorGroup].[name] like '%%'
group by [Division].[name], [Educator].[full_name], [EducatorPosition].[name], [EducatorGroup].[name], [Educator].[id]
order by [Educator].[full_name]