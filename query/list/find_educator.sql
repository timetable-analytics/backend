use local_db
select [Educator_view].[id], [Educator_view].[division], [Educator_view].[full_name], [Educator_view].[position], [Educator_view].[educator_group]
from [Educator_view]
where [Educator_view].[is_active] = 1
and [Educator_view].[division] like '%%'
and [Educator_view].[full_name] like '%%'
and [Educator_view].[position] like '%%'
and [Educator_view].[educator_group] like '%%'
order by [Educator_view].[full_name]
