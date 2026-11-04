"""Phased learning actions keyed by role family and specialty."""

from __future__ import annotations

from typing import Dict, List

FOUNDATION_ACTIONS: Dict[str, str] = {
    "data": "Complete a supervised labeling project with written quality rubrics",
    "quality": "Learn LLM evaluation basics and write 20 regression prompts",
    "finance": "Rebuild one spreadsheet workflow as a reproducible Python notebook",
    "support": "Map top 30 support intents and draft bot handoff criteria",
    "content": "Build a personal prompt library with style constraints and evals",
    "analytics": "Automate one recurring report end-to-end with tests",
    "people": "Document a skills taxonomy for one hiring funnel stage",
    "creative": "Generate and critique 50 asset variants against a brand kit",
    "infra": "Stand up a local model-serving container and health checks",
    "product": "Instrument a toy product funnel and define AI success metrics",
    "delivery": "Create an AI-assisted status operating cadence for one squad",
    "revenue": "Score a sample CRM export and compare against human ranking",
    "operations": "Prototype a demand or staffing forecast with naive baselines",
    "healthcare": "Practice PHI-safe redaction and clinical label guidelines",
    "legal": "Review 10 contracts with an AI assistant under human oversight",
    "knowledge": "Migrate a FAQ into a retrieval-ready chunked knowledge base",
    "research": "Code a qualitative dataset and synthesize themes with AI assist",
    "science": "Label a small scientific dataset and document edge cases",
    "learning": "Design a micro-curriculum with AI tutoring checkpoints",
    "hospitality": "Script an AI concierge flow for the top five guest intents",
    "engineering": "Use a coding assistant to migrate a tiny legacy module",
    "geo": "Run a geospatial classification notebook on open satellite tiles",
    "vision": "Triage a synthetic camera-alert queue with precision/recall notes",
    "retail": "Design an aisle assistant playbook for one product category",
    "risk": "Shadow a fraud queue and document model disagreement cases",
    "governance": "Draft a one-page model card for a toy classifier",
    "trust": "Calibrate a moderation rubric against 100 labeled examples",
    "general": "Learn Python basics and prompt hygiene for knowledge work",
}

PRACTICE_ACTIONS: Dict[str, str] = {
    "data": "Ship a public sample dataset with inter-annotator agreement notes",
    "quality": "Contribute eval cases to an open-source LLM test suite",
    "finance": "Publish a risk-flagging notebook on anonymized sample ledgers",
    "support": "Simulate deflection improvements on a synthetic ticket corpus",
    "content": "Produce a before/after content pack using constrained prompts",
    "analytics": "Open-source a tiny metrics pipeline with CI checks",
    "people": "Build a skills-to-role matcher demo on a public jobs dump",
    "creative": "Create a generative brand system with rejection criteria",
    "infra": "Benchmark inference latency across two local model backends",
    "product": "Write an AI feature brief with kill criteria and eval plan",
    "delivery": "Run a two-week AI delivery experiment with risk logs",
    "revenue": "Prototype a lead-routing assistant and measure precision",
    "operations": "Compare AI forecast vs moving average on public demand data",
    "healthcare": "Complete a synthetic claims ops walkthrough with audit trails",
    "legal": "Build a clause extraction demo with lawyer-in-the-loop notes",
    "knowledge": "Publish a retrieval demo with citation faithfulness checks",
    "research": "Release a coded interview set with AI-assisted theme maps",
    "science": "Document a labeling protocol suitable for lab handoff",
    "learning": "Pilot a tutoring loop with pre/post assessment deltas",
    "hospitality": "Prototype a booking-recovery assistant conversation tree",
    "engineering": "Modernize a 200-line legacy script with assistant + tests",
    "geo": "Ship a map story that combines CV detections and spatial joins",
    "vision": "Build an alert-prioritization rubric with false-positive analysis",
    "retail": "Demo a recommendation explanation card for store associates",
    "risk": "Create a disagreement dashboard for human/model score gaps",
    "governance": "Assemble a lightweight AI policy checklist for a small team",
    "trust": "Publish a safety incident postmortem template for AI products",
    "general": "Build three portfolio projects that prove transferable judgment",
}

NETWORK_ACTIONS: List[str] = [
    "Join one AI practitioner community and post a weekly learning note",
    "Request informational chats with two people already in the target role",
    "Contribute a small PR or dataset issue to an adjacent open-source tool",
    "Present a 10-minute pivot teardown at a local meetup or internal guild",
]

SPECIALIZATION_ACTIONS: Dict[str, str] = {
    "Prompt Engineering": "Specialize in eval-driven prompt systems for one vertical",
    "Data Annotation & Labeling": "Specialize in rubric design and consensus workflows",
    "AI Testing Automation": "Specialize in LLM regression harnesses and golden sets",
    "ML Infrastructure Technician": "Specialize in local GPU serving and observability",
    "Legal Document AI Specialist": "Specialize in clause taxonomies and review UX",
    "Talent Intelligence Analyst": "Specialize in skills-graph matching quality",
    "Analytics Engineering Associate": "Specialize in semantic metrics layers for AI products",
    "default": "Deepen one tool stack until you can mentor a junior peer",
}

PORTFOLIO_ACTIONS: List[str] = [
    "Publish a case study with problem, method, artifacts, and measured lift",
    "Record a short walkthrough of your best artifact for hiring managers",
    "Maintain a living skills graph linking legacy experience to AI proof points",
]
