use local_db
create table EducatorAssigmentUnit (
	id uniqueidentifier not NULL,
	event uniqueidentifier NULL,
	educator_employment uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (event) references Event (id),
	FOREIGN KEY (educator_employment) references EducatorEmployment (id)
);
INSERT into [local_db].[dbo].[EducatorAssigmentUnit]([id]) SELECT [timetable-live].[dbo].[EducatorAssignmentUnit].[Oid] from [timetable-live].[dbo].[EducatorAssignmentUnit];
update [local_db].[dbo].[EducatorAssigmentUnit] set event = (select [timetable-live].[dbo].[EducatorAssignmentUnit].[EducatorAssignment] from [timetable-live].[dbo].[EducatorAssignmentUnit] where [local_db].[dbo].[EducatorAssigmentUnit].id = [timetable-live].[dbo].[EducatorAssignmentUnit].Oid)