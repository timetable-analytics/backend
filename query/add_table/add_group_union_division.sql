use local_db
create table Group_union_Division (
	id uniqueidentifier not NULL,
	group_union uniqueidentifier NULL,
	division uniqueidentifier NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (group_union) references Group_union (id),
	FOREIGN KEY (division) references Division (id)
);
insert into [local_db].[dbo].[Group_union_Division]([id]) select [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations].[Oid] from [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations];
update [local_db].[dbo].[Group_union_Division] set group_union = (select [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations].[ContingentUnitCombinations] from [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations] where [local_db].[dbo].[Group_union_Division].id = [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations].Oid);
update [local_db].[dbo].[Group_union_Division] set division = (select [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations].[Divisions] from [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations] where [local_db].[dbo].[Group_union_Division].id = [timetable-live].[dbo].[DivisionDivisions_ContingentUnitContingentUnitCombinations].Oid);