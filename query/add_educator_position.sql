use local_db
create table EducatorPosition (
	id uniqueidentifier not NULL,
	name nvarchar(255) NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[EducatorPosition]([id]) SELECT [timetable-live].[dbo].[EducatorEmploymentPosition].[Oid] from [timetable-live].[dbo].[EducatorEmploymentPosition];
update [local_db].[dbo].[EducatorPosition] set name = (select [timetable-live].[dbo].[EducatorEmploymentPosition].[FullName] from [timetable-live].[dbo].[EducatorEmploymentPosition] where [local_db].[dbo].[EducatorPosition].id = [timetable-live].[dbo].[EducatorEmploymentPosition].Oid)