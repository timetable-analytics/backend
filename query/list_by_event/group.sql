select [Group_union].[id], [Division].[name], [Group_union].[name], [Group_union].[course]
from [Division], [Group_union], [Group_union_Division], [Event]
where [Division].[id] = [Group_union_Division].[division]
and [Group_union].[id] = [Group_union_Division].[group_union]
and [Event].[group_union] = [Group_union].[id]
and [Event].[id] in (/* list id in '' separated by , (for example '1', '2')*/)
group by [Group_union].[id], [Division].[name], [Group_union].[name], [Group_union].[course]
order by [Group_union].[name]
