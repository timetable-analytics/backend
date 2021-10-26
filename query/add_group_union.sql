use local_db
create table Group_union (
	id uniqueidentifier not NULL,
	name nvarchar(max) NULL,
	course nvarchar(100) NULL,
	PRIMARY KEY (id),
);
insert into [local_db].[dbo].[Group_union]([id]) select [timetable-live].[dbo].[ContingentUnit].[Oid] from [timetable-live].[dbo].[ContingentUnit];
update [local_db].[dbo].[Group_union] set name = (select [timetable-live].[dbo].[ContingentUnit].[StudentGroupsString] from [timetable-live].[dbo].[ContingentUnit] where [local_db].[dbo].[Group_union].id = [timetable-live].[dbo].[ContingentUnit].Oid);
update [local_db].[dbo].[Group_union] set course = (select [timetable-live].[dbo].[ContingentUnit].[Course] from [timetable-live].[dbo].[ContingentUnit] where [local_db].[dbo].[Group_union].id = [timetable-live].[dbo].[ContingentUnit].Oid);