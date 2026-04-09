"""Base data structures for agent outputs."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentResult:
    """Normalized payload emitted by each agent in the graph."""

    agent_name: str
    output: str
    metadata: dict[str, Any] = field(default_factory=dict)
