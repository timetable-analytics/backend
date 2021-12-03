select [Educator].[id], [Division].[name], [Educator].[full_name], [EducatorPosition].[name], [EducatorGroup].[name]
from [Division], [Educator], [EducatorPosition], [EducatorGroup], [EducatorEmployment], [EducatorDivision], [Event], [EducatorAssigmentUnit]
where [Division].[id] = [EducatorDivision].[division]
and [Educator].[id] = [EducatorEmployment].[educator]
and [EducatorPosition].[id] = [EducatorEmployment].[position]
and [EducatorGroup].[id] = [EducatorEmployment].[educator_group]
and [EducatorEmployment].[id] = [EducatorDivision].[educator_employment]
and [Event].[educator_assigment] = [EducatorAssigmentUnit].[educator_assigment]
and [EducatorAssigmentUnit].[educator_employment] = [EducatorEmployment].[id]
and [Event].[id] in (/* list id in '' separated by , */)
group by [Division].[name], [Educator].[full_name], [EducatorPosition].[name], [EducatorGroup].[name], [Educator].[id]
order by [Educator].[full_name]