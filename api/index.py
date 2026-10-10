import sys
from pathlib import Path

# Make the existing backend package importable in Vercel's project-root runtime.
backend_dir = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(backend_dir))

from app.main import app

__all__ = ["app"]
