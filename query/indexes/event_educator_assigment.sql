USE [local_db]

GO

CREATE NONCLUSTERED INDEX [NonClusteredIndex-20211209-230949] ON [dbo].[Event]
(
	[educator_assigment] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF)

GO


