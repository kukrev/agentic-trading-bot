from pydantic import BaseModel

class RagToolSchema(BaseModel):
    question:str