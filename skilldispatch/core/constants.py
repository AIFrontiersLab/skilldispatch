"""Cross-cutting constants for Skilldispatch."""

PIPELINE_VERSION = "static-v3"
DEFAULT_LOCALE = "en-US"
MAX_SKILL_TOKENS = 64
MAX_SKILL_CHARS = 4000
DEFAULT_REPORT_TITLE = "Skilldispatch Pivot Report"
SUPPORTED_INPUT_FORMATS = ("comma_separated", "semicolon_separated", "newline_separated")
PHASE_ORDER = (
    "foundation",
    "practice",
    "network",
    "specialization",
    "portfolio",
)
HTTP_API_TAGS = ("pivot", "catalog", "ops")
