use local_db
create table EducatorGroup (
	id uniqueidentifier not NULL,
	name nvarchar(100) NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[EducatorGroup]([id]) SELECT [timetable-live].[dbo].[EducatorEmploymentGroup].[Oid] from [timetable-live].[dbo].[EducatorEmploymentGroup];
update [local_db].[dbo].[EducatorGroup] set name = (select [timetable-live].[dbo].[EducatorEmploymentGroup].[Name] from [timetable-live].[dbo].[EducatorEmploymentGroup] where [local_db].[dbo].[EducatorGroup].id = [timetable-live].[dbo].[EducatorEmploymentGroup].Oid);