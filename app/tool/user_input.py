from app.tool.base import BaseTool

class UserInput(BaseTool):
    name: str = "user_input"
    description: str = """Use this tool to ask the user questions and have the user confirm the information."""
    parameters: dict = {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "ask for more information",
            }
        },
        "required": ["question"],
    }

    async def execute(self, question: str) -> str:
        return input("问题：%s\n请回答: " % question)