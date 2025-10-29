### Persona development guide

1. Aggregate inputs:
   - Customer data and sales feedback
   - Community/forums (Reddit, Stack Overflow, discuss.elastic.co)
   - Support tickets and internal usage analytics

2. Normalize into `Persona` objects:
   - Role, industry, expertise level
   - Pains and goals

3. Model use cases and decision contexts:
   - Constraints (scale, latency, budget)
   - Success metrics

4. Turn into conversation prompts (Stage 0):
   - System prompt: persona context
   - User prompt: concrete use case

5. Validate with LLM testing (Stage 0):
   - Inspect reasoning, cited entities, missing attributes
   - Feed insights into entity map and content planning
