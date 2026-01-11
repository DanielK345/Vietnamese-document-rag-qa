import gc
from pathlib import Path
from typing import List

import torch
from docling.chunking import HybridChunker
from langchain_core.documents import Document
from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType
from tqdm.auto import tqdm