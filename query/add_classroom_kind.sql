use local_db
create table Classroom_kind (
	id uniqueidentifier not NULL,
	name nvarchar(100) NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[Classroom_kind]([id]) SELECT [timetable-live].[dbo].[ClassroomKind].[Oid] from [timetable-live].[dbo].[ClassroomKind];
update [local_db].[dbo].[Classroom_kind] set name = (select [timetable-live].[dbo].[ClassroomKind].[Name] from [timetable-live].[dbo].[ClassroomKind] where [local_db].[dbo].[Classroom_kind].id = [timetable-live].[dbo].[ClassroomKind].Oid)