from asyncio import tasks
from typing import Annotated

from fastapi import Depends, APIRouter

from schemas import STaskID, StaskAdd, STask
from repository import TaskRepository

router = APIRouter(
	prefix="/tasks",
	tags=["Таски"],
)

@router.post("")
async def add_task(
	task: Annotated[StaskAdd, Depends()],
) -> STaskID:
	task_id = await TaskRepository.add_one(task)
	return {"ok": True, "task_id": task_id}


@router.get("")
async def get_task() -> list[STask]:
	tasks = await TaskRepository.find_all()
	return tasks
