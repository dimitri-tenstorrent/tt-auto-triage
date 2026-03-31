"""Shared pytest fixtures for auto_triage Python tests."""

import os
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Provide a temporary data directory mimicking AT_DATA_DIR."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def tmp_output_dir(tmp_path):
    """Provide a temporary output directory mimicking AT_OUTPUT_DIR."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def mock_env(monkeypatch, tmp_path):
    """Set up common environment variables used across modules."""
    monkeypatch.setenv("AT_OWNER", "tenstorrent")
    monkeypatch.setenv("AT_REPO", "tt-metal")
    monkeypatch.setenv("AT_OWNER_REPO", "tenstorrent/tt-metal")
    monkeypatch.setenv("AT_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("AT_OUTPUT_DIR", str(tmp_path / "output"))
    monkeypatch.setenv("AT_LOGS_DIR", str(tmp_path / "logs"))
    (tmp_path / "data").mkdir(exist_ok=True)
    (tmp_path / "output").mkdir(exist_ok=True)
    (tmp_path / "logs").mkdir(exist_ok=True)
    return tmp_path
