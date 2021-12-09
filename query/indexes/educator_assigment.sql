USE [local_db]
GO

/****** Object:  Index [NonClusteredIndex-20211209-225748]    Script Date: 09.12.2021 22:58:32 ******/
CREATE NONCLUSTERED INDEX [NonClusteredIndex-20211209-225748] ON [dbo].[EducatorAssigmentUnit]
(
	[educator_assigment] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO


