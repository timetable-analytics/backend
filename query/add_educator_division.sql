use local_db
create table EducatorDivision (
	id uniqueidentifier not NULL,
	educator_employment uniqueidentifier NULL,
	division uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (educator_employment) references EducatorEmployment (id),
	FOREIGN KEY (division) references Division (id)
);
INSERT into [local_db].[dbo].[EducatorDivision]([id]) SELECT [timetable-live].[dbo].[EducatorStudyWorkUnit].[Oid] from [timetable-live].[dbo].[EducatorStudyWorkUnit];
update [local_db].[dbo].[EducatorDivision] set educator_employment = (select [timetable-live].[dbo].[EducatorStudyWorkUnit].[EducatorEmployment] from [timetable-live].[dbo].[EducatorStudyWorkUnit] where [local_db].[dbo].[EducatorDivision].id = [timetable-live].[dbo].[EducatorStudyWorkUnit].Oid);
update [local_db].[dbo].[EducatorDivision] set division = (select [timetable-live].[dbo].[EducatorStudyWorkUnit].[Division] from [timetable-live].[dbo].[EducatorStudyWorkUnit] where [local_db].[dbo].[EducatorDivision].id = [timetable-live].[dbo].[EducatorStudyWorkUnit].Oid);