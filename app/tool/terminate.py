from app.tool.base import BaseTool


_TERMINATE_DESCRIPTION = """Terminate the interaction when the request is met OR if the assistant cannot proceed further with the task.
When you have finished all the tasks, call this tool to end the work.
IMPORTANT：Synthesize and summarize the acquired information to filter out irrelevant information."""


class Terminate(BaseTool):
    name: str = "terminate"
    description: str = _TERMINATE_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "info": {
                "type": "string",
                "description": "Summary result information of the current task, such as user response information, refined search results, etc.",
            }
        },
        "required": ["info"],
    }

    async def execute(self, info: str) -> str:
        """Finish the current execution"""
        return info
