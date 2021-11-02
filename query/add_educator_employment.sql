use local_db
create table EducatorEmployment (
	id uniqueidentifier not NULL,
	position uniqueidentifier NULL,
	educator uniqueidentifier NULL,
	educator_group uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (position) references EducatorPosition (id),
	FOREIGN KEY (educator) references Educator (id),
	FOREIGN KEY (educator_group) references EducatorGroup (id)
);
INSERT into [local_db].[dbo].[EducatorEmployment]([id]) SELECT [timetable-live].[dbo].[EducatorEmployment].[Oid] from [timetable-live].[dbo].[EducatorEmployment];
update [local_db].[dbo].[EducatorEmployment] set position = (select [timetable-live].[dbo].[EducatorEmployment].[Position] from [timetable-live].[dbo].[EducatorEmployment] where [local_db].[dbo].[EducatorEmployment].id = [timetable-live].[dbo].[EducatorEmployment].Oid);
update [local_db].[dbo].[EducatorEmployment] set educator = (select [timetable-live].[dbo].[EducatorEmployment].[EducatorMasterPerson] from [timetable-live].[dbo].[EducatorEmployment] where [local_db].[dbo].[EducatorEmployment].id = [timetable-live].[dbo].[EducatorEmployment].Oid);
update [local_db].[dbo].[EducatorEmployment] set educator_group = (select [timetable-live].[dbo].[EducatorEmployment].[Group] from [timetable-live].[dbo].[EducatorEmployment] where [local_db].[dbo].[EducatorEmployment].id = [timetable-live].[dbo].[EducatorEmployment].Oid);