from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


class Persona(BaseModel):
    name: str
    role: str
    expertise_level: str = Field(default="intermediate")
    pains: List[str] = Field(default_factory=list)
    goals: List[str] = Field(default_factory=list)
    industry: Optional[str] = None


class UseCase(BaseModel):
    title: str
    description: Optional[str] = None
    constraints: List[str] = Field(default_factory=list)
    success_metrics: List[str] = Field(default_factory=list)


class DecisionContext(BaseModel):
    persona: Persona
    use_case: UseCase
    environment: Optional[str] = None  # e.g., stack, scale, latency requirements
