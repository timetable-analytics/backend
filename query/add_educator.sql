use local_db
create table Educator (
	id uniqueidentifier not NULL,
	full_name nvarchar(302) NULL,
	is_active bit NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[Educator]([id]) SELECT [timetable-live].[dbo].[EducatorMasterPerson].[Oid] from [timetable-live].[dbo].[EducatorMasterPerson];
update [local_db].[dbo].[Educator] set full_name = (select ([timetable-live].[dbo].[EducatorMasterPerson].[LastName] + ' ' + [timetable-live].[dbo].[EducatorMasterPerson].[FirstName] + ' ' + [timetable-live].[dbo].[EducatorMasterPerson].[MiddleName]) from [timetable-live].[dbo].[EducatorMasterPerson] where [local_db].[dbo].[Educator].id = [timetable-live].[dbo].[EducatorMasterPerson].Oid);
update [local_db].[dbo].[Educator] set is_active = (select [timetable-live].[dbo].[EducatorMasterPerson].[IsActive] from [timetable-live].[dbo].[EducatorMasterPerson] where [local_db].[dbo].[Educator].id = [timetable-live].[dbo].[EducatorMasterPerson].Oid);
