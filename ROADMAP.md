Main goal of this strategy: 
Transform Elastic’s website into a semantically optimized knowledge hub,  a model of what a website should look like for semantic systems such as large language models (LLMs) and semantic search engines.
This means building an ontological and entity-driven information architecture that:
Accurately represents Elastic’s core topical domains (AI Search, Enterprise Search, Observability, and Security) and all relevant subtopics, concepts, and relationships.


Provides comprehensive, semantically rich content aligned with user personas, intents, and funnel stages (informational, commercial, transactional).


Ensures that Elastic’s information is machine-readable, retrievable, and contextually relevant, so that LLMs and search systems can understand, recommend, and cite Elastic as an authoritative resource.


Ultimately positions Elastic as both the topical authority and the preferred solution for users and systems seeking information or products in its key domains.

How to achieve this
To turn Elastic’s website into a semantically optimized, machine-understandable knowledge hub, we will:
Disambiguate and define key entities


Explicitly define Elastic’s main entities and their relationships to ensure machines can interpret them correctly.
Example: ensure Elasticsearch is recognized not only as a “search engine” but also as a vector database and core component of AI Search.


Implement a modern semantic infrastructure


Apply entity-based modeling, schema markup, embeddings, and internal linking strategies to strengthen semantic relevance across all content layers — from site architecture to paragraphs.
Use structured data, ontologies, and contextual linking to connect entities and improve topical salience.


Modernize and automate the query research and content creation pipeline


Build an automated process for query discovery, clustering, and content gap analysis to ensure timely, semantically relevant SEO and LLMO recommendations.
Integrate LLM-based keyword expansion and query fan-out techniques to capture emerging intents.


Establish offsite semantic vigilance


Implement a monitoring system to track and analyze how Elastic is mentioned and defined externally (press, documentation, third-party sites, community forums).
Detect inconsistencies and opportunities to reinforce Elastic’s entity definitions and brand semantics.


Ensure full retrievability and crawlability


Guarantee that all pages and assets are technically accessible and indexable for both search engines and LLM retrieval systems.
Address issues related to crawling, rendering, and structured content exposure.


Enable foundational prerequisites


Ensure all source data is cleaned, normalized, and accessible.
Secure access to semantic tools, APIs, and internal datasets needed to run entity extraction, embeddings, and hybrid retrieval workflows.
Build the required infrastructure gradually, starting with semi-automated scripts and evolving toward fully automated pipelines.


Cross-team alignment and semantic governance


Align SEO, content, product, data, and engineering teams on shared definitions and taxonomies.
Define governance processes to maintain consistency as Elastic’s product lines evolve.
Establish measurable KPIs 

Stages of the Semantic Roadmap: 

Stage 1: Define core Entity/topical map and main semantic clusters  

Establish the main semantic clusters grounded in Elastic’s products, solutions, and use cases.
These clusters will form the backbone of Elastic’s ontology, guiding content coverage, internal linking, and topical hierarchy.
Each cluster represents a core semantic entity network around which relevance, authority, and retrieval are built

Defining Core Semantic Clusters
There are already  identified three established semantic clusters that align with Elastic’s main business domains: Enterprise Search, Observability, Security
However, we are currently missing one crucial cluster: AI Search.
Although AI Search overlaps with Enterprise Search at a conceptual level, it constitutes a semantically distinct cluster.
 Its underlying entities, relationships, and vocabulary  such as embeddings, vector databases, semantic retrieval, RAG pipelines, and AI agents  form a different meaning network and address different user intents.
From an information retrieval and knowledge graph perspective, AI Search sits at a different technological paradigm. Therefore, it requires a dedicated cluster to:
Ensure clear disambiguation between traditional and AI-driven search concepts.


Strengthen topical salience and internal linking around new emerging entities.


Align Elastic’s positioning with how modern search and AI systems categorize and retrieve information.


To validate and structure this new cluster, we will use a combination of semantic and NLP-based analysis tools, including:
Google Natural Language API and Knowledge Graph API to identify and categorize recognized entities and relationships.


spaCy NER for named-entity extraction and ontology expansion.


Embedding-based similarity analysis (cosine similarity, clustering) to quantify the semantic distance between AI Search concepts and other clusters.


Optionally, Gemini API or other LLM-based models to interpret conceptual boundaries and co-occurrence patterns between entities.


This evidence-based approach will confirm whether “AI Search” functions as an independent semantic cluster within Elastic’s knowledge ecosystem.

Define Main Entities and Subentities
For each semantic cluster, identify the core entities and their relationships (subject–object–verb triples) based on Elastic’s main solution pages and supporting documentation.
 This phase builds the conceptual graph that connects our content architecture with how machines represent knowledge.
If priorities or resources are limited, we can begin with a single high-impact cluster — for example, AI Search — and expand progressively.
Example structure (illustrative):
AI Search (broad paradigm)
│
└── Semantic Search (subset focused on meaning-based retrieval)
     │
     └── Vector Database (core enabling infrastructure)
          ├── Uses → Embeddings
          ├── Implements → ANN / HNSW / FAISS
          ├── Enables → Similarity Search, Hybrid Search
          ├── Powers → Contextual Engineering
          └── Used by → Agentic Builders / AI Agents

Tools and methods used to define entities and relationships:
Google Knowledge Graph API → to detect recognized entities and their existing semantic connections.


Google Natural Language API and spaCy → for entity extraction and dependency parsing (subject–object–verb relationships).


Embedding-based similarity modeling (cosine similarity, clustering) → to group conceptually related entities.


Gemini API or other LLMs → to interpret latent semantic relationships and validate hierarchical structure.


Manual ontology refinement → to ensure alignment with Elastic’s product taxonomy and terminology.


This phase results in a machine-readable entity map that defines the conceptual backbone for each semantic cluster and powers all later content, linking, and retrieval optimizations.

Disambiguate and Align with the Core Topical Map
Identify and strengthen product pages whose entity representations are ambiguous, weakly connected, or semantically incomplete within the overall topical map.
 The objective is to ensure every key entity is clearly defined, contextually linked, and semantically reinforced across Elastic’s content ecosystem.
To detect underdefined or misaligned entities, we will:
Query LLMs and knowledge graph APIs to evaluate how Elastic’s entities are currently interpreted by machines.


Analyze anchor text networks and internal linking patterns to uncover missing semantic bridges.


Apply embedding similarity checks to identify pages whose semantic vectors deviate from their intended cluster.


Examples:
Elasticsearch is widely recognized as a search engine but not as a vector database. This gap originates from Elastic’s own pages (and wikipedia articles and knowledge graph definition), where the vector database role is not explicitly or consistently defined, limiting how machines categorize it within the AI Search domain.


Elastic Cloud is often conflated with general cloud computing concepts, creating ambiguity in how search systems and LLMs understand its specialized scope and value proposition.


This phase ensures all core entities are disambiguated, explicitly defined, and aligned with Elastic’s overarching ontology and topical map, so that both users and machines interpret them accurately.

4. Add comprehensive structured data 
(example, Product/SoftwareApplication, Organization, FAQPage, HowTo) with explicit entity linking (sameAs, IDs) to encode roles like “vector database”


5. Offsite + Onsite Entity Consistency Check
Onsite consistency: Once entities are explicit, routinely audit how they’re defined and cross-referenced across pages. Use Screaming Frog/Botify exports to locate pages by entity mentions, verify definitions, and inspect anchor text and internal links for semantic alignment.


Vector-based checks (future-ready): With content embedded, run periodic similarity checks in Elasticsearch to spot pages that are semantically off-cluster, missing links, or using inconsistent terminology.


Offsite vigilance: Track how third-party sites define Elastic entities; flag mismatches and prioritize outreach/content fixes to harmonize definitions.

Stage 2. Keyword research and content gap analysis

We will approach this in two phases: an initial phase in the near future, followed by a later phase where we can scale our efforts once the necessary infrastructure is established.

Keyword research is essential for identifying main semantic clusters and gaps, and for understanding user needs and search volume. However, we need to modernize our approach to incorporate new techniques that are compatible with Large Language Model (LLM) requirements.

Proposed Process for LLM-Specific Optimization
Traditional keyword research (queries like “best vector database”) reflects search engine behavior, not how LLMs process or retrieve information.
 When you ask such a question to a model like ChatGPT, it tends to simulate a search engine,  surfacing aggregated web answers, rather than reasoning semantically or contextually.
To optimize for LLMs, we need to shift from query thinking to context thinking.
 Our goal is to ensure that Elastic’s content provides the contextual signals and domain coverage an LLM would need to select, recommend, or cite Elastic as a solution.
Step 1 — Model real LLM user contexts
Build personas based on:


Internal usage data, client profiles, and sales feedback.
Real-world user discussions on sources like Reddit, Stack Overflow, and discuss.elastic.co 


For each persona, identify recurrent use cases and decision contexts  


Step 2 — Turn personas into LLM conversation prompts
Create ideal prompts that simulate how these personas would naturally interact with LLMs.


Example: instead of “best vector database,” use conversational inputs like
 “Our engineering team needs to add semantic search to our e-commerce platform handling 10M+ daily queries, but we're concerned about maintaining sub-200ms latency, scaling vector operations cost-effectively, and integrating with our existing Elasticsearch infrastructure without a complete rewrite.”


Observe the LLM’s reasoning path → what entities, attributes, and product types it mentions  to identify what Elastic needs to make explicit in its own content.


Step 3 — Flatten and structure prompts into query elements
Convert insights from these prompts into structured components:


Entities ( vector database, hybrid search)
Attributes (cost, scalability, integration options)
Intent types (informational, solution-seeking, technical troubleshooting)
FAQ-style questions to include in the query map


Step 4 — Expand through query fan-outs
Use LLM-based query expansion (fan-out) to discover variant formulations and sub-questions.


Map these expanded prompts to existing content to find coverage gaps and RAG opportunities, areas where Elastic’s documentation or product pages should provide structured, retrievable answers.


Outcome
This process moves Elastic’s keyword research from short-tail keyword coverage to semantic prompt coverage, aligning our content strategy with how LLMs infer, retrieve, and contextualize information,  not just how search engines rank it.
2. Traditional Keyword Research
Use BigQuery, Google Search Console, SEMrush, and other data sources to perform large-scale keyword extraction and performance analysis.
 This step ensures we maintain full coverage of existing search-driven opportunities , complementing the new LLM-focused process with traditional SEO insights on traffic, demand, and ranking potential.


2. Proposed process for overall needs: 

For now, we will rely on manual and semi-automated processes to handle specific content and ad-hoc keyword requests.
However, the long-term goal is to build a scalable keyword research and mapping system,  one that continuously integrates new data sources, captures emerging intents, and evolves with technological and user behavior shifts aggregating data from tools like BigQuery, Google Search Console, SEMrush, and LLM-based query expansion.



Stage 3. Cluster Keywords and Prompts into Entities, Subentities, and Attributes
We’ll cluster all queries and prompts into semantic groups that combine:
Entity (core concept)
Attributes/modifiers (query language, cost, latency, integration, scalability, for rag, download, deploy, documentation, what is, etc )
Micro-intent (the real purpose behind the query: quick look up, comparison, concept explanation, tutorial, example, video demo, etc)
Brand context (branded vs. non-branded)


This clustering becomes the backbone for gap analysis, content recommendation, and query-level performance evaluation.
Phase 1 — Manual and Semi-Automated Clustering
Before full automation, we’ll use:
Manual labeling and keyword-matching scripts (example, Python + Sentence Transformers).
LLM-based classification APIs to detect entity types, micro-intents, and semantic overlaps.


This stage will give us an initial, flexible entity–intent map to validate patterns before scaling.
Phase 2 — Automated Classification and Embedding Pipeline
Once the infrastructure is ready, we’ll implement an internal classifier trained on Elastic’s own content and taxonomy.
 Each query will be classified and embedded automatically to power both analytics and content recommendations.
The classifier won’t use the outdated “informational / navigational / transactional” model → those intent categories are too broad to be actionable.
 Instead, we’ll define Elastic-specific micro-intents, directly tied to content formats and user behaviors, such as:
Documentation / Reference lookup → short factual answers, code examples, or definitions.
Comparison → side-by-side feature.
Solution / Product page → high-level positioning and benefits.
Tutorial or How-to → procedural, task-oriented content.
Troubleshooting / Integration → step-by-step guides addressing technical blockers.
Thought leadership / Blog → conceptual or strategic insights.


By classifying queries this way, we’ll be able to instantly infer the ideal content format (quick lookup, table, feature overview, tutorial, video, etc.) and connect it to the right location in our entity map.
This classifier will also allow us to:
Segment traffic and rankings by content purpose, not just by keyword or funnel stage.
Understand the impact of algorithmic and content changes on specific query types.


The goal is to move from a static “intent model” to a dynamic understanding of user purpose that directly drives the right content experience.

Stage 4: Filling and Expanding the Elastic Entity Map
Once keyword and prompt data are classified, we’ll use it to expand the Elastic Entity Map, translating raw query signals into a structured network of entities, subentities, attributes, and intent modifiers.
Using a combination of semantic salience, vector similarity (semantic distance), and behavioral insights (engagement metrics, click data, dwell time), we’ll identify which entities deserve deeper coverage and how they interconnect.
This intelligence will guide:
Internal linking architecture, connecting semantically related pages and clusters.
Content hierarchy,  deciding which entities merit full pages, which belong as sections or paragraphs, and which should be merged for stronger topical authority.
UX-driven prioritization,  aligning the structure with actual user behavior and intent signals is crucial


The goal is not to give every entity a page, but to give every concept a place,  building a site architecture where meaning, intent, and user engagement converge.


Stage 5: Gap Analysis
Phase 1 — Manual and Semi-Automated (Pre-Infrastructure)
Generate temporary embeddings for Elastic’s existing content and crawl the site using Botify or Screaming Frog.
 By comparing each page’s semantic similarity to target entities and queries, we can detect:
Content gaps → topics or subtopics not yet covered.
Weak connections → pages that should be semantically related but aren’t properly linked.
Low-relevance areas → content whose embeddings fall below similarity thresholds and need rewriting or restructuring.


At this stage, main queries (converted into entity + attribute + question form) will be mapped against both the ideal Elastic sitemap and the current site structure, allowing us to visualize semantic coverage and identify missing or diluted topics.
Phase 2 — Scalable and Automated (Embedding Infrastructure in Place)
Once full embedding pipelines are available, we’ll run semantic gap detection at scale using Elastic’s vector search capabilities.
 By combining dense retrieval (embeddings) and sparse retrieval (BM25) in hybrid search, we’ll mirror how modern systems (from Google Search to LLM RAG rerankers) evaluate content relevance.
This hybrid approach allows us to:
Surface under-optimized pages across entire clusters.
Quantify where Elastic’s coverage is strongest or weakest within each semantic domain.
Continuously feed this insight back into content recommendations, linking updates, and entity map refinement.
The goal: ensure every core entity and topic is contextually connected, semantically strong, and retrievable,  both by humans and by machines.

Stage 6: Content Recommendation Process
When a content gap or low-similarity area is identified, the next step is to generate or optimize content guided by the entity map and query classification.
 Each recommendation is data-driven,  designed to match the right entity, subentity, and intent with the right content format, structure, and tone.
Step 1 — Define the Semantic Context
Leverage the query classifier to determine:
Intent and format documentation snippet, tutorial, comparison page).
Target entity and attributes from the Elastic Entity Map.
Existing subentities and relationships already mapped for that topic.


Use entity extraction and vector search to surface the most relevant subtopics, co-occurring terms, and semantic clusters that must appear in the text to achieve high topical relevance.
Step 2 — Analyze Competitors and High-Authority Sources
Study organic competitors and highly-ranked pages for the target topic that clearly targets the intent, such as pages featured in AI overviews, featured snippets, or developer documentation.
 From these, extract:
High-salience entities and the terms most consistently co-occurring across top content.
Content structure, tone, and intent patterns (tutorial, guide, FAQ, etc.).
Style and sentiment cues that influence how LLMs and search engines interpret authority.
 Supplement this with related questions (using tools like AlsoAsked.com, keywords everywhere, etc) to enrich the outline with long-tail, conversational prompts.


Step 3 — Design the Semantic Content Brief
Combine all insights to build an SEO + LLMO–friendly content brief that:
Breaks the topic into short, focused chunks, each targeting a specific subentity or question.
Uses clear, structured headings and semantically dense paragraphs to help retrieval systems map the content accurately.
Specifies content format, depth, and tone aligned with the identified micro-intent (quick reference, tutorial, comparison, etc.).


Step 4 — Validate and Optimize
Before publishing, test semantic strength by calculating BM25 lexical scores and cosine similarity between the new content and target entities/subentities.
 This ensures each section achieves high semantic relevance and contributes meaningfully to the broader entity and topical map.
The goal: create content that doesn’t just rank →  it retrieves. Every page becomes a node in a semantic network, designed for both search engines and LLMs to understand, connect, and recommend.

Stage 7: Content Dilution Issues Audit
Identify content that is topically weak, semantically irrelevant, or misaligned with Elastic’s core entity-map, and either improve, merge, relocate deeply, or de-index it.
 Why this matters: when a website includes many pages that drift from the main themes or carry low semantic focus, it can reduce the site’s overall topical authority and confuse both search engines and LLM-based retrieval systems indirectly
From the Google leak: internal documentation reveals metrics like siteFocusScore (how tightly a site sticks to its main theme) and siteRadius (how far individual pages deviate topically) : the larger the topical deviation, the more the site appears unfocused, which may lead to demotion

Infrastructure Roadmap
Building Elastic's semantic infrastructure in phases: data setup → validation → build → automation → continuous improvement.
PHASES:
1 — Data Foundations (Immediate)
Goal: Get all our data in one place and ready to use.
Actions:
Gather missing data from all subdomains (GSC, log files, crawl data)
Centralize everything in BigQuery or Elasticsearch with consistent formats
Clean up Botify segmentation to match our semantic clusters
Set up monitoring for LLM bot crawls (ChatGPT, Claude, etc.)
Start manually tagging queries by entity and intent to train our classifier
Get API access to necessary tools (Gemini, Google NLP, OpenAI)
Build ad hoc scripts for keyword research gap analysis and query clustering
Build ad hoc scripts for content recommendation

Outcome: Clean, centralized data ready for semantic work.
2 — Feasibility Check
Goal: Figure out what we can reuse vs. what we need to build, and who owns what.
Key Questions:
Can our internal search index handle vector search, or do we need a separate layer?
Does our Elastic crawler fully render JavaScript and Next.js content? If not, do we extend it or use external tools?
Which team owns the vector database, classifier, and embeddings? (SEO handles strategy/taxonomy, Engineering handles infrastructure)
What stack do we use for the query classifier? (Prototype with Python/Hugging Face, production with Elastic ML)
Outcome: A clear blueprint defining who builds what, with which tools, and on which timeline.
3 — Build Core Systems (Short-Term)
Goal: Get the foundational systems working.
Actions:
Build and train query classifier v1 (classifies queries by entity, intent, micro-intent)
Deploy vector database using Elasticsearch's dense_vector capabilities
Connect all data sources (Botify, BigQuery, CMS, etc.)
Start monitoring how LLMs and search engines interact with our content
Outcome: Working semantic infrastructure → embeddings, classification, hybrid search.
4 — Automate (Mid-Term)
Goal: Scale it up and reduce manual work.
Actions:
Integrate with CMS to automate schema markup and internal linking suggestions
Use embeddings and engagement data to recommend semantic connections between pages
Build dashboards to flag crawl issues or content gaps automatically
Refine hybrid search (keyword + vector) to match how Google and LLMs actually rank content
Outcome: Self-monitoring system that optimizes continuously with minimal manual intervention.

5 — Continuous Learning (Long-Term)
Goal: Make the system adaptive and self-improving.
Actions:
Set up automated feedback loops: classifier → embeddings → optimization → retraining
Retrain models regularly as user behavior and query patterns change
Monitor how Elastic is defined externally (Wikipedia, forums, docs) and correct inconsistencies
Align taxonomies across SEO, Docs, Product, and AI teams
Outcome: A living semantic infrastructure that maintains Elastic's authority as search and LLM technology evolves.


Technical seo/llmo roadmap
1: Foundation & Critical Fixes 
Critical Issues:
Fix crawl issues (noindex, 403 errors, crawl budget waste)
Fix JavaScript localized rendering (main nav, language picker)
International SEO fixes
Bot Management:
Centralize bot monitoring via log file analysis
Audit robots.txt and current bot handling
Identify all bot traffic (search engines, LLM crawlers, scrapers)
Baseline crawl patterns and resource consumption

2: LLM Optimization
Content Extractability:
Audit JavaScript accessibility for LLM bots
Test content parsing (GPTBot, Claude-Web, PerplexityBot)
Ensure static HTML availability for critical content
Bot Management:
Implement differential bot handling (optimize for high-value, block low-value)
Set up alerting for bot anomalies
Ensure LLM bots access semantic-rich content

3: Automation & Advanced Testing 
Performance & Infrastructure:
Backend/frontend improvements for web performance and LLM extractability
Automated crawl budget optimization
Advanced Bot Management:
Test agentic accessibility (can AI agents perform actions?)
Build automated bot classification and routing system
Continuous monitoring and monthly bot audit reports
