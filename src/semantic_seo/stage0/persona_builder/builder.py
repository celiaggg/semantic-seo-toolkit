from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from semantic_seo.shared.utils.io import read_csv
from semantic_seo.shared.utils.text import normalize_whitespace
from semantic_seo.stage0.context_modeling.contexts import Persona


@dataclass
class PersonaSourceRow:
    name: str
    role: str
    pains: List[str]
    goals: List[str]
    industry: str | None


def build_personas_from_csv(path: str | bytes | bytearray) -> List[Persona]:
    """Create personas from a CSV with columns: name,role,pains,goals,industry.

    pains/goals are expected as semicolon-separated strings.
    """
    rows = read_csv(path)  # type: ignore[arg-type]
    personas: List[Persona] = []
    for r in rows:
        pains = [normalize_whitespace(p) for p in (r.get("pains", "").split(";") if r.get("pains") else [])]
        goals = [normalize_whitespace(g) for g in (r.get("goals", "").split(";") if r.get("goals") else [])]
        personas.append(
            Persona(
                name=normalize_whitespace(r.get("name", "Unknown")),
                role=normalize_whitespace(r.get("role", "Unknown")),
                pains=[p for p in pains if p],
                goals=[g for g in goals if g],
                industry=normalize_whitespace(r.get("industry", "")) or None,
            )
        )
    return personas


def merge_persona_lists(*lists: Iterable[Persona]) -> List[Persona]:
    out: List[Persona] = []
    for lst in lists:
        out.extend(list(lst))
    # optional: dedupe by (name, role)
    seen = set()
    unique: List[Persona] = []
    for p in out:
        key = (p.name.lower(), p.role.lower())
        if key not in seen:
            unique.append(p)
            seen.add(key)
    return unique
