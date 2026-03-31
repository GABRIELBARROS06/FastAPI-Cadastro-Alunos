from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Aluno(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    idade: int = Field(..., gt=0, lt=120)
    curso: Optional[str] = Field(default=None, max_length=100)