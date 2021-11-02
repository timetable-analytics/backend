use local_db
create table EventLocation (
	id uniqueidentifier not NULL,
	[event] uniqueidentifier NULL,
	classroom uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY ([event]) references Event (id),
	FOREIGN KEY (classroom) references Classroom (id)
);
INSERT into [local_db].[dbo].[EventLocation]([id]) SELECT [timetable-live].[dbo].[EventLocation].[Oid] from [timetable-live].[dbo].[EventLocation];
update [local_db].[dbo].[EventLocation] set [event] = (select [timetable-live].[dbo].[EventLocation].[Event] from [timetable-live].[dbo].[EventLocation] where [local_db].[dbo].[EventLocation].id = [timetable-live].[dbo].[EventLocation].Oid);