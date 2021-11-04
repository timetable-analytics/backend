use local_db
create table Division (
	id uniqueidentifier not NULL,
	name nvarchar(100) NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[Division]([id]) SELECT [timetable-live].[dbo].[Division].[Oid] from [timetable-live].[dbo].[Division];
update [local_db].[dbo].[Division] set name = (select [timetable-live].[dbo].[Division].[Name] from [timetable-live].[dbo].[Division] where [local_db].[dbo].[Division].id = [timetable-live].[dbo].[Division].Oid)
