use [local_db]
select [dbo].[Classroom_view].[id], 
	[dbo].[Classroom_view].[address], 
	[dbo].[Classroom_view].[classroom_kind], 
	[dbo].[Classroom_view].[classroom]
from [dbo].[Classroom_view]
where [dbo].[Classroom_view].[address] like '%%'
and [dbo].[Classroom_view].[classroom] like '%%'
and [dbo].[Classroom_view].[classroom_kind] like '%%'
