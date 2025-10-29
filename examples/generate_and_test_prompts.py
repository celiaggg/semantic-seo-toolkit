"""Example: Generate and test LLM prompts for a decision context."""
from semantic_seo.stage0.context_modeling.contexts import Persona, UseCase, DecisionContext
from semantic_seo.stage0.llm_testing.evaluator import LLMTester
from semantic_seo.stage0.prompt_engineering.generator import generate_conversation_prompts

if __name__ == "__main__":
    persona = Persona(
        name="Senior Search Engineer",
        role="Engineer",
        pains=["latency under 200ms", "cost control", "integration complexity"],
        goals=["production-ready semantic search", "use Elasticsearch vectors"],
        industry="e-commerce",
    )
    use_case = UseCase(
        title="Add semantic search to high-traffic platform",
        constraints=["10M+ daily queries", "sub-200ms latency", "reuse Elasticsearch stack"],
    )
    ctx = DecisionContext(persona=persona, use_case=use_case, environment="Elasticsearch 8.x")

    sys, user = generate_conversation_prompts(ctx)
    print("System:\n", sys)
    print("User:\n", user)

    # Requires API keys (.env)
    tester = LLMTester(provider="openai")
    result = tester.run(ctx)
    print("Model:", result.model)
    print("Output:\n", result.output)
