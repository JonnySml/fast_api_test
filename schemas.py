
from typing import Optional
from pydantic import BaseModel


class StaskAdd(BaseModel):
	name: str
	description: Optional[str] = None


class STask(StaskAdd):
	id: int


class STaskID(BaseModel):
	ok: bool = True
	task_id: int