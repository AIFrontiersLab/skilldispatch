"""Repository for AI-adjacent role catalog metadata."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from skilldispatch.data.role_catalog import ROLE_CATALOG, ROLE_DEMAND, roles_for_family


class RoleRepository:
    def get(self, title: str) -> Optional[Dict[str, Any]]:
        meta = ROLE_CATALOG.get(title)
        if meta is None:
            return None
        return {"title": title, "demand": ROLE_DEMAND.get(title, 0.5), **meta}

    def list_by_family(self, family: str) -> List[str]:
        return roles_for_family(family)

    def top_by_demand(self, limit: int = 10) -> List[Dict[str, Any]]:
        ranked = sorted(ROLE_DEMAND.items(), key=lambda i: i[1], reverse=True)[:limit]
        out = []
        for title, demand in ranked:
            row = self.get(title) or {"title": title, "demand": demand}
            out.append(row)
        return out

    def families(self) -> List[str]:
        return sorted({str(m.get("family", "general")) for m in ROLE_CATALOG.values()})
