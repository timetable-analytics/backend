use local_db
select [Division].[name], [Group_union].[name], [Group_union].[course]
from [Division], [Group_union], [Group_union_Division]
where [Division].[id] = [Group_union_Division].[division]
and [Group_union].[id] = [Group_union_Division].[group_union]
and [Division].[name] like '%%'
and [Group_union].[name] like '%%'
and [Group_union].[course] like '%%'
group by [Division].[name], [Group_union].[name], [Group_union].[course]
order by [Group_union].[name]