# cjm-capability-monitor-nvidia

<!-- generated from the context graph by `cjm-context-graph readme` — do not edit by hand; edit the graph (the urge to hand-edit = move it on-graph) -->

An NVIDIA GPU monitoring capability for the cjm-substrate runtime that provides real-time hardware telemetry via nvitop.

## Modules

- **`cjm_capability_monitor_nvidia.capability`** — NVIDIA GPU monitoring capability using nvitop — real-time hardware telemetry (GPU memory/utilization, system RAM, CPU) with an nvidia-smi fallback.

## API

### `cjm_capability_monitor_nvidia.capability`

- `NvidiaMonitorCapability` _class_ — NVIDIA System Monitor using nvitop (a pure-telemetry ToolCapability).
