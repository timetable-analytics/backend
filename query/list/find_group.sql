use local_db
select [dbo].[Students_group_view].[id],
	[dbo].[Students_group_view].[division],
	[dbo].[Students_group_view].[group],
	[dbo].[Students_group_view].[course]
from [dbo].[Students_group_view]
where [dbo].[Students_group_view].[division] like '%%'
and [dbo].[Students_group_view].[group] like '%%'
and [dbo].[Students_group_view].[course] like '%%'
order by [dbo].[Students_group_view].[group]
