DTMF Table
===========

.. image:: https://img.shields.io/pypi/v/dtmf-table?style=for-the-badge&color=009E73&label=PyPI
   :target: https://pypi.org/project/dtmf-table/
   :alt: PyPI

.. image:: https://img.shields.io/crates/l/audio_samples?style=for-the-badge&label=license&labelColor=gray
   :target: https://github.com/jmg049/dtmf_table/blob/main/LICENSE
   :alt: License: MIT

A zero-heap, Rust backed, **const-first** implementation of the standard DTMF (Dual-Tone Multi-Frequency) keypad used in telephony systems.

This Python package provides fast, efficient DTMF frequency lookups built on Rust bindings with a Pythonic API.

Features
--------

- **Const-evaluated forward and reverse mappings** between DTMF keys and frequencies
- **Closed enum for keys** — invalid keys are unrepresentable
- **Zero allocations** in the underlying Rust implementation
- Runtime helpers:

  - Tolerance-based reverse lookup (e.g., from FFT peaks)
  - Nearest snapping for noisy frequency estimates
  - Iteration over all tones and keys

Installation
------------

Install from PyPI using pip:

.. code-block:: bash

   pip install dtmf-table

Quick Start
-----------

Here's a simple example to get you started:

.. code-block:: python

   from dtmf_table import DtmfTable, DtmfKey

   # Construct a table instance
   table = DtmfTable()

   # Forward lookup from key to canonical frequencies
   key = DtmfKey.from_char('8')
   low, high = key.freqs()
   assert (low, high) == (852, 1336)

   # Reverse lookup with tolerance (e.g., from FFT bin centres)
   key = table.from_pair_tol_f64(770.2, 1335.6, 6.0)
   assert key.to_char() == '5'

   # Nearest snapping for noisy estimates
   key, snapped_low, snapped_high = table.nearest_u32(768, 1342)
   assert key.to_char() == '5'
   assert (snapped_low, snapped_high) == (770, 1336)

DTMF Frequency Table
--------------------

The library contains all 16 standard DTMF frequencies used in telephony:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * -
     - 1209 Hz
     - 1336 Hz
     - 1477 Hz
     - 1633 Hz
   * - 697 Hz
     - 1
     - 2
     - 3
     - A
   * - 770 Hz
     - 4
     - 5
     - 6
     - B
   * - 852 Hz
     - 7
     - 8
     - 9
     - C
   * - 941 Hz
     - \*
     - 0
     - #
     - D

Audio Processing Integration
-----------------------------

This library pairs naturally with audio analysis pipelines:

1. Take an audio segment
2. Compute FFT magnitude
3. Pick two frequency peaks
4. Use ``from_pair_tol_f64`` or ``nearest_f64`` to resolve the DTMF key

Example:

.. code-block:: python

   # freq1 and freq2 are the peak frequencies extracted from your FFT
   table = DtmfTable()
   key = table.from_pair_tol_f64(freq1, freq2, 5.0)
   if key is not None:
       print(f"Detected key: {key.to_char()}")

Contents
--------

.. toctree::
   :maxdepth: 2

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
