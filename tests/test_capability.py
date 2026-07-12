"""Hermetic tests for cjm_capability_monitor_nvidia.capability (c25780e8 flip).

The notebook carried no test cells; these cover identity, config surface, and
the live-telemetry SHAPE (no GPU compute, no network — RAM/CPU ride psutil and
the GPU fields degrade to zero/[] on GPU-less hosts per the documented contract)."""

from cjm_capability_monitor_nvidia.capability import NvidiaMonitorCapability
from cjm_capability_primitives.monitoring import ProcessStats, SystemStats


def test_identity_from_distribution():
    cap = NvidiaMonitorCapability()
    assert cap.name == "cjm-capability-monitor-nvidia"
    assert cap.version  # derived from importlib.metadata, never hardcoded


def test_initialize_and_config_surface():
    cap = NvidiaMonitorCapability()
    cap.initialize()
    assert isinstance(cap.get_config_schema(), dict)
    assert isinstance(cap.get_current_config(), dict)


def test_system_status_shape():
    # RAM/CPU telemetry rides psutil, so the shape holds even with no GPU;
    # gpu fields are zero/absent rather than raising when nothing is visible.
    cap = NvidiaMonitorCapability()
    cap.initialize()
    stats = cap.get_system_status()
    assert isinstance(stats, SystemStats)
    assert stats.memory_available_mb >= 0 and stats.cpu_percent >= 0


def test_list_processes_shape():
    # documented contract: [] when there is no GPU or no per-process attribution
    cap = NvidiaMonitorCapability()
    cap.initialize()
    procs = cap.list_processes()
    assert isinstance(procs, list)
    assert all(isinstance(p, ProcessStats) for p in procs)
