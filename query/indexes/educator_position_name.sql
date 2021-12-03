USE [local_db]
GO

SET ANSI_PADDING ON
GO

/****** Object:  Index [NonClusteredIndex-20211203-173548]    Script Date: 03.12.2021 20:23:36 ******/
CREATE NONCLUSTERED INDEX [NonClusteredIndex-20211203-173548] ON [dbo].[EducatorPosition]
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO


