"""IOCREP MCP server — exposes score() as an MCP tool for Cognis.Studio."""
from __future__ import annotations
import json as _json
from iocrep.core import score_indicator, ReputationDB


def serve() -> int:
    """Start an MCP stdio server. Requires the optional 'mcp' extra:
        pip install "cognis-iocrep[mcp]"
    """
    try:
        from mcp.server.fastmcp import FastMCP
    except Exception:
        print("Install the MCP extra: pip install 'cognis-iocrep[mcp]'")
        return 1
    app = FastMCP("iocrep")
    _db = ReputationDB()

    @app.tool()
    def iocrep_scan(target: str) -> str:
        """Score IOCs against offline reputation/allow lists with explainable
        verdicts. Returns JSON findings."""
        if not target or not target.strip():
            return _json.dumps({"error": "target must be a non-empty string"})
        verdict = score_indicator(target, _db)
        return _json.dumps(verdict.to_dict())

    app.run()
    return 0
