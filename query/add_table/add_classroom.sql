use local_db
create table Classroom (
	id uniqueidentifier not NULL,
	name nvarchar(100) NULL,
	classroom_kind uniqueidentifier NULL,
	capacity int NULL,
	address uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (classroom_kind) references Classroom_kind (id),
	FOREIGN KEY (address) references Address (id)
);
insert into [local_db].[dbo].[Classroom]([id]) select [timetable-live].[dbo].[Location].[Oid] from [timetable-live].[dbo].[Location];
update [local_db].[dbo].[Classroom] set name = (select [timetable-live].[dbo].[Location].[NumberActual] from [timetable-live].[dbo].[Location] where [local_db].[dbo].[Classroom].id = [timetable-live].[dbo].[Location].Oid);
update [local_db].[dbo].[Classroom] set classroom_kind = (select [timetable-live].[dbo].[Location].[ClassroomKind] from [timetable-live].[dbo].[Location] where [local_db].[dbo].[Classroom].id = [timetable-live].[dbo].[Location].Oid);
update [local_db].[dbo].[Classroom] set capacity = (select [timetable-live].[dbo].[Location].[Capacity] from [timetable-live].[dbo].[Location] where [local_db].[dbo].[Classroom].id = [timetable-live].[dbo].[Location].Oid);
update [local_db].[dbo].[Classroom] set address = (select [timetable-live].[dbo].[Location].[Address] from [timetable-live].[dbo].[Location] where [local_db].[dbo].[Classroom].id = [timetable-live].[dbo].[Location].Oid);