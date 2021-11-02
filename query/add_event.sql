use local_db
create table Event (
	id uniqueidentifier not NULL,
	[start] datetime NULL,
	[end] datetime NULL,
	educator_assigment uniqueidentifier NULL,
	discipline uniqueidentifier NULL,
	group_union uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (discipline) references Discipline (id),
	FOREIGN KEY (group_union) references Group_union (id)
);
INSERT into [local_db].[dbo].[Event]([id]) SELECT [timetable-live].[dbo].[Event].[Oid] from [timetable-live].[dbo].[Event];
update [local_db].[dbo].[Event] set [start] = (select [timetable-live].[dbo].[Event].[Start] from [timetable-live].[dbo].[Event] where [local_db].[dbo].[Event].id = [timetable-live].[dbo].[Event].Oid);
update [local_db].[dbo].[Event] set [end] = (select [timetable-live].[dbo].[Event].[End] from [timetable-live].[dbo].[Event] where [local_db].[dbo].[Event].id = [timetable-live].[dbo].[Event].Oid);
update [local_db].[dbo].[Event] set educator_assigment = (select [timetable-live].[dbo].[Event].[EducatorAssignment] from [timetable-live].[dbo].[Event] where [local_db].[dbo].[Event].id = [timetable-live].[dbo].[Event].Oid);
update [local_db].[dbo].[Event] set discipline = (select [timetable-live].[dbo].[EducatorAssignment].[Discipline] from [timetable-live].[dbo].[Event], [timetable-live].[dbo].[EducatorAssignment] where [local_db].[dbo].[Event].id = [timetable-live].[dbo].[Event].Oid and [timetable-live].[dbo].[EducatorAssignment].[Oid] = [timetable-live].[dbo].[Event].[EducatorAssignment]);
update [local_db].[dbo].[Event] set group_union = (select [timetable-live].[dbo].[Event].[ContingentUnit] from [timetable-live].[dbo].[Event] where [local_db].[dbo].[Event].id = [timetable-live].[dbo].[Event].Oid);