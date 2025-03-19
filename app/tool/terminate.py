from app.tool.base import BaseTool


_TERMINATE_DESCRIPTION = """Terminate the interaction when the request is met OR if the assistant cannot proceed further with the task.
When you have finished all the tasks, call this tool to end the work."""


class Terminate(BaseTool):
    name: str = "terminate"
    description: str = _TERMINATE_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "result": {
                "type": "string",
                "description": "任务目标对应的结果信息",
            }
        },
        "required": ["result"],
    }

    async def execute(self, result: str) -> str:
        """Finish the current execution"""
        return result
