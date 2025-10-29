"""Example: Build personas from a CSV file.

CSV schema: name,role,pains,goals,industry
- pains/goals are semicolon-separated
"""
from pathlib import Path
from semantic_seo.stage0.persona_builder.builder import build_personas_from_csv

if __name__ == "__main__":
    path = Path("./data/personas.csv")
    if not path.exists():
        print("Create ./data/personas.csv first (see docstring for schema).")
    else:
        personas = build_personas_from_csv(path)
        for p in personas:
            print(p.model_dump())
