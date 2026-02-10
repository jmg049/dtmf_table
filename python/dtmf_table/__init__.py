"""DTMF (Dual-Tone Multi-Frequency) frequency table for telephony applications.

This library provides efficient, const-first mappings between DTMF keys and their
canonical frequency pairs. Built with Rust for performance, it offers both exact
lookups and tolerance-based matching for real-world audio analysis.
"""
from .dtmf_table import DtmfKey, DtmfTable, DtmfTone, LOWS, HIGHS

__all__ = ["DtmfKey", "DtmfTone", "DtmfTable", "LOWS", "HIGHS"]