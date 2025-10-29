from __future__ import annotations

from typing import List, Optional

from semantic_seo.stage0.context_modeling.contexts import DecisionContext, Persona


def system_prompt_for_persona(persona: Persona) -> str:
    return (
        f"You are assisting a {persona.role} (industry: {persona.industry or 'general'}). "
        f"Their goals: {', '.join(persona.goals) or 'n/a'}. "
        f"Their pains: {', '.join(persona.pains) or 'n/a'}."
    )


def user_prompt_for_use_case(context: DecisionContext) -> str:
    return (
        f"We need guidance for: {context.use_case.title}. "
        f"Environment: {context.environment or 'unspecified'}. "
        f"Constraints: {', '.join(context.use_case.constraints) or 'none'}."
    )


def generate_conversation_prompts(context: DecisionContext) -> List[str]:
    """Return a list of prompts simulating a realistic conversation for an LLM."""
    sys = system_prompt_for_persona(context.persona)
    user = user_prompt_for_use_case(context)
    return [sys, user]
