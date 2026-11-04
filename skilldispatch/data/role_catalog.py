"""Role catalog metadata and synthetic demand scores for ranking."""

from __future__ import annotations

from typing import Dict, List

ROLE_CATALOG: Dict[str, Dict[str, object]] = {
    "Data Annotation & Labeling": {
        "family": "data",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["Label Studio", "Scale", "CVAT"],
        "keywords": ["annotation", "labeling", "dataset quality"],
    },
    "AI Testing Automation": {
        "family": "quality",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Playwright", "pytest", "eval harnesses"],
        "keywords": ["eval", "regression", "model quality"],
    },
    "Financial AI Analysis": {
        "family": "finance",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Python", "spreadsheets", "anomaly detectors"],
        "keywords": ["risk", "forecasting", "ledger intelligence"],
    },
    "AI Chatbot Operations": {
        "family": "support",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["Intercom", "Zendesk AI", "dialog traces"],
        "keywords": ["handoff", "intent", "deflection"],
    },
    "Prompt Engineering": {
        "family": "content",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["ChatGPT", "Claude", "prompt libraries"],
        "keywords": ["prompts", "style guides", "eval sets"],
    },
    "Analytics Automation Specialist": {
        "family": "analytics",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Excel", "Python", "Airflow lite"],
        "keywords": ["automation", "reporting", "metrics"],
    },
    "HR Systems AI Ops": {
        "family": "people",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Workday", "BambooHR", "workflow bots"],
        "keywords": ["hris", "automation", "onboarding"],
    },
    "Talent Intelligence Analyst": {
        "family": "people",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["ATS exports", "embedding search", "scorecards"],
        "keywords": ["sourcing", "matching", "skills graphs"],
    },
    "AI Documentation Engineer": {
        "family": "content",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Docs-as-code", "LLM drafts", "style linters"],
        "keywords": ["docs", "apis", "knowledge"],
    },
    "AI Content Systems Operator": {
        "family": "content",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["CMS", "scheduling AI", "brand prompts"],
        "keywords": ["content ops", "distribution", "brand"],
    },
    "Generative Design Operator": {
        "family": "creative",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Figma", "Midjourney", "Firefly"],
        "keywords": ["assets", "variants", "brand kits"],
    },
    "Multimodal Media Producer": {
        "family": "creative",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Descript", "CapCut", "TTS"],
        "keywords": ["video", "audio", "repurposing"],
    },
    "Speech Data Specialist": {
        "family": "data",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["ASR QA", "diarization tools"],
        "keywords": ["speech", "transcripts", "audio quality"],
    },
    "Localization AI Specialist": {
        "family": "content",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["CAT tools", "MTQE", "glossary AI"],
        "keywords": ["translation", "locale", "quality"],
    },
    "AI Support Escalation Lead": {
        "family": "support",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["ticketing AI", "runbooks", "RAG assistants"],
        "keywords": ["escalation", "kb", "triage"],
    },
    "ML Infrastructure Technician": {
        "family": "infra",
        "remote_friendly": True,
        "entry_barrier": "high",
        "tools": ["Docker", "GPU hosts", "monitoring"],
        "keywords": ["serving", "pipelines", "reliability"],
    },
    "Analytics Engineering Associate": {
        "family": "analytics",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["dbt", "SQL", "BI tools"],
        "keywords": ["models", "metrics", "warehouses"],
    },
    "AI Product Analyst": {
        "family": "product",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Mixpanel", "SQL", "eval dashboards"],
        "keywords": ["product", "experiments", "insights"],
    },
    "AI Delivery Coordinator": {
        "family": "delivery",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Jira", "roadmap AI", "status bots"],
        "keywords": ["delivery", "coordination", "risk"],
    },
    "Conversational Sales Ops": {
        "family": "revenue",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["dialers", "conversation intel"],
        "keywords": ["outbound", "scripts", "conversion"],
    },
    "Revenue Systems AI Ops": {
        "family": "revenue",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Salesforce", "HubSpot", "scoring models"],
        "keywords": ["crm", "pipeline", "automation"],
    },
    "Supply Chain AI Analyst": {
        "family": "operations",
        "remote_friendly": False,
        "entry_barrier": "medium",
        "tools": ["ERP exports", "forecast models"],
        "keywords": ["inventory", "logistics", "demand"],
    },
    "Clinical Data Labeling Specialist": {
        "family": "healthcare",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["clinical ontologies", "PHI-safe tooling"],
        "keywords": ["clinical", "coding", "labels"],
    },
    "Healthcare AI Ops Associate": {
        "family": "healthcare",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["EHR workflows", "claims AI"],
        "keywords": ["ops", "claims", "care admin"],
    },
    "Legal Document AI Specialist": {
        "family": "legal",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["contract AI", "redline assistants"],
        "keywords": ["contracts", "discovery", "review"],
    },
    "Knowledge Base AI Curator": {
        "family": "knowledge",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["Notion AI", "vector stores", "taxonomies"],
        "keywords": ["kb", "curation", "retrieval"],
    },
    "Applied Research Ops": {
        "family": "research",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["survey tools", "coding AI", "synthesis"],
        "keywords": ["research", "coding", "insights"],
    },
    "Scientific Data Labeling Specialist": {
        "family": "science",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["lab notebooks", "sensor labeling"],
        "keywords": ["scientific", "datasets", "protocols"],
    },
    "AI Learning Experience Designer": {
        "family": "learning",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["LMS", "tutoring AI", "curriculum prompts"],
        "keywords": ["learning", "curriculum", "assessment"],
    },
    "AI Concierge Operations": {
        "family": "hospitality",
        "remote_friendly": False,
        "entry_barrier": "low",
        "tools": ["booking AI", "guest assistants"],
        "keywords": ["hospitality", "concierge", "service"],
    },
    "Workplace Automation Specialist": {
        "family": "operations",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["Zapier", "Make", "office bots"],
        "keywords": ["automation", "admin", "workflows"],
    },
    "Legacy Modernization AI Engineer": {
        "family": "engineering",
        "remote_friendly": True,
        "entry_barrier": "high",
        "tools": ["code assistants", "migration scanners"],
        "keywords": ["legacy", "cobol", "modernization"],
    },
    "Scientific Computing AI Associate": {
        "family": "science",
        "remote_friendly": True,
        "entry_barrier": "high",
        "tools": ["NumPy", "simulation assistants"],
        "keywords": ["scientific computing", "models"],
    },
    "AI Application Integrator": {
        "family": "engineering",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["APIs", "webhooks", "LLM wrappers"],
        "keywords": ["integration", "glue code", "apis"],
    },
    "AI Presentation Systems Operator": {
        "family": "content",
        "remote_friendly": True,
        "entry_barrier": "low",
        "tools": ["Gamma", "Beautiful.ai", "deck prompts"],
        "keywords": ["presentations", "storytelling"],
    },
    "Geospatial AI Analyst": {
        "family": "geo",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["QGIS", "satellite CV", "spatial SQL"],
        "keywords": ["gis", "maps", "remote sensing"],
    },
    "Computer Vision Monitoring Ops": {
        "family": "vision",
        "remote_friendly": False,
        "entry_barrier": "medium",
        "tools": ["camera AI", "alert triage"],
        "keywords": ["vision", "monitoring", "alerts"],
    },
    "Retail AI Experience Associate": {
        "family": "retail",
        "remote_friendly": False,
        "entry_barrier": "low",
        "tools": ["store AI", "recommendation ops"],
        "keywords": ["retail", "customer", "floor ops"],
    },
    "Risk Models Operations Associate": {
        "family": "risk",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["case queues", "model score review"],
        "keywords": ["risk", "fraud", "underwriting"],
    },
    "AI Governance Associate": {
        "family": "governance",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["policy trackers", "model cards"],
        "keywords": ["governance", "compliance", "audit"],
    },
    "Trust & Safety AI Associate": {
        "family": "trust",
        "remote_friendly": True,
        "entry_barrier": "medium",
        "tools": ["moderation queues", "policy LLMs"],
        "keywords": ["trust", "safety", "abuse"],
    },
}

ROLE_DEMAND: Dict[str, float] = {
    title: round(0.55 + (idx % 9) * 0.05, 2)
    for idx, title in enumerate(sorted(ROLE_CATALOG.keys()))
}

# Nudge a few strategically important pivots upward.
for _hot in (
    "Prompt Engineering",
    "Data Annotation & Labeling",
    "AI Testing Automation",
    "Analytics Engineering Associate",
    "AI Chatbot Operations",
    "ML Infrastructure Technician",
    "Talent Intelligence Analyst",
    "Legal Document AI Specialist",
):
    ROLE_DEMAND[_hot] = min(0.98, ROLE_DEMAND.get(_hot, 0.7) + 0.18)


def roles_for_family(family: str) -> List[str]:
    return [title for title, meta in ROLE_CATALOG.items() if meta.get("family") == family]
