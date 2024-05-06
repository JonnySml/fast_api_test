from sqlalchemy import select
from database import TaskTable, new_session
from schemas import StaskAdd, STask

class TaskRepository:
	@classmethod
	async def add_one(cls, data: StaskAdd) -> int:
		async with new_session() as session:
			task_dick = data.model_dump()

			task = TaskTable(**task_dick)
			session.add(task)
			await session.flush()
			await session.commit()
			return task.id



	@classmethod
	async def find_all(cls) -> list[STask]:
		async with new_session() as session:
			querry = select(TaskTable)
			result = await session.execute(querry)
			task_models = result.scalars().all()
			task_schemas = [STask.model_validate(task_model) for task_model in task_models]
			return task_schemas