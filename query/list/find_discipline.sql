use local_db
select [Discipline].[name]
from [Discipline]
group by [Discipline].[name] --��� ��� ���� �������
order by [Discipline].[name]