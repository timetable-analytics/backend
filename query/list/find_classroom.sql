use [local_db]
select [Classroom].[id], [Address].[address], [Classroom_kind].[name], [Classroom].[name]
from [Address], [Classroom], [Classroom_kind]
where [Classroom].[classroom_kind] = [Classroom_kind].[id]
and [Classroom].[address] = [Address].[id]
and [Address].[address] like '%%'
and [Classroom].[name] like '%%'
and [Classroom_kind].[name] like '%%'