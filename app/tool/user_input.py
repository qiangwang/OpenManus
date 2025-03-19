from app.tool.base import BaseTool

class UserInput(BaseTool):
    name: str = "user_input"
    description: str = """使用此工具向用户提出疑问，并让用户确认信息"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "(required) 向用户提出的问题.",
            }
        },
        "required": ["query"],
    }

    async def execute(self, query: str) -> str:
        return input("问题：%s\n请回答: " % query)