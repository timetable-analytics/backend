use local_db
create table Discipline (
	id uniqueidentifier not NULL,
	name nvarchar(500) NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[Discipline]([id]) SELECT [timetable-live].[dbo].[Discipline].[Oid] from [timetable-live].[dbo].[Discipline];
update [local_db].[dbo].[Discipline] set name = (select [timetable-live].[dbo].[Discipline].[Name] from [timetable-live].[dbo].[Discipline] where [local_db].[dbo].[Discipline].id = [timetable-live].[dbo].[Discipline].Oid)