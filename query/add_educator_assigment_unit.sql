use local_db
create table EducatorAssigmentUnit (
	id uniqueidentifier not NULL,
	educator_assigment uniqueidentifier NULL,
	educator_employment uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (educator_employment) references EducatorEmployment (id),
);
INSERT into [local_db].[dbo].[EducatorAssigmentUnit]([id]) SELECT [timetable-live].[dbo].[EducatorAssignmentUnit].[Oid] from [timetable-live].[dbo].[EducatorAssignmentUnit];
update [local_db].[dbo].[EducatorAssigmentUnit] set educator_assigment = (select [timetable-live].[dbo].[Event].[EducatorAssignment] from [timetable-live].[dbo].[EducatorAssignmentUnit], [timetable-live].[dbo].[Event], [timetable-live].[dbo].[EducatorAssignment] where [local_db].[dbo].[EducatorAssigmentUnit].id = [timetable-live].[dbo].[EducatorAssignmentUnit].Oid and [timetable-live].[dbo].[Event].[EducatorAssignment] = [timetable-live].[dbo].[EducatorAssignment].[Oid] and [timetable-live].[dbo].[EducatorAssignmentUnit].[EducatorAssignment] = [timetable-live].[dbo].[EducatorAssignment].[Oid]);
update [local_db].[dbo].[EducatorAssigmentUnit] set educator_employment = (select [timetable-live].[dbo].[EducatorAssignmentUnit].[EducatorEmployment] from [timetable-live].[dbo].[EducatorAssignmentUnit] where [local_db].[dbo].[EducatorAssigmentUnit].id = [timetable-live].[dbo].[EducatorAssignmentUnit].Oid);