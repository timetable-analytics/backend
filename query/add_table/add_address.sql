use local_db
create table Address (
	id uniqueidentifier not NULL,
	address nvarchar(250) NULL,
	PRIMARY KEY (id)
);
INSERT into [local_db].[dbo].[Address]([id]) SELECT [timetable-live].[dbo].[Address].[Oid] from [timetable-live].[dbo].[Address];
update [local_db].[dbo].[Address] set address = (select [timetable-live].[dbo].[Address].[DisplayName1] from [timetable-live].[dbo].[Address] where [local_db].[dbo].[Address].id = [timetable-live].[dbo].[Address].Oid)