import json
import pickle
from datetime import datetime
from typing import Any, Dict, List

from langchain_core.documents import Document

from src.constant import (
    CHARS_PER_TOKEN,
    CHUNKER_MODEL,
    MAX_CHUNK_TOKENS,
    METADATA_FILE,
    OVERLAP_TOKENS,
    PROCESSED_DOCS_FILE,
    PROCESSING_SESSION_ID,
)
from src.utils.logging import get_logger

logger = get_logger("rag.preprocess.storage")
