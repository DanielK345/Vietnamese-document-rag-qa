"""
RAG Retrieval Components
========================

Unified Vietnamese RAG system with internal modular components.
"""

# Core search components
from src.rag_retriever.hybrid_search import HybridSearcher, hybrid_search

# LLM integration
from src.rag_retriever.llm_caller import RAGLLMCaller, get_rag_llm_caller

# Model loading utilities
from src.rag_retriever.model_loader import get_embedding_model, get_reranker_model, load_retrieval_models

# Main unified system
from src.rag_retriever.vietnamese_rag import VietnameseRAG, get_vietnamese_rag

__all__ = [
    # Model loading
    "get_embedding_model",
    "get_reranker_model",
    "load_retrieval_models",
    # Core search
    "HybridSearcher",
    "hybrid_search",
    # Main unified system
    "VietnameseRAG",
    "get_vietnamese_rag",
    # LLM integration
    "RAGLLMCaller",
    "get_rag_llm_caller",
]
