# Claw Code (ultraworkers/claw-code)

> **Rust CLI Agent Harness - The Claw Way**

## Quick Stats

| Metric | Value |
|--------|-------|
| **Stars** | 184,690 |
| **Daily Stars** | 0（稳定） |
| **Language** | Rust |
| **Contributors** | 4 |

## Overview

Claw Code 是一个用 Rust 实现的 CLI Agent 运行框架，专注于终端自动化。

**核心理念**：Container-first workflow，提供高效的 Agent 运行环境。

## Architecture

```
rust/ — Canonical Rust workspace
├─ claw CLI binary
├─ USAGE.md — Usage guide
├─ PARITY.md — Rust-port status
└─ ROADMAP.md — Roadmap

Companion:
├─ src/ + tests/ — Python reference
└─ docs/container.md — Container workflow
```

## Key Features

1. **Rust 实现**
   - 高性能
   - 内存安全
   - 跨平台支持

2. **CLI Harness**
   - `claw doctor` — 健康检查
   - `claw acp` — ACP 状态查询
   - Container-first workflow

3. **Parity Check**
   - 与 Python 版本对齐
   - 持续迁移

## Current Status

- **ACP/Zed**: 不提供 ACP/Zed daemon entrypoint
- **Runtime**: `claw acp serve` 是 discoverability alias
- **Roadmap**: ACP 支持在 ROADMAP.md 中跟踪

## Quick Start

```bash
# Build
cargo build --release

# Health check
claw doctor

# ACP status
claw acp
```

## Use Cases

- ✅ 终端自动化
- ✅ 开发者工具集成
- ✅ Container workflow
- ✅ 高性能 Agent 运行

## Links

- 📦 GitHub: https://github.com/ultraworkers/claw-code
- 📖 Usage: [USAGE.md](https://github.com/ultraworkers/claw-code/blob/main/USAGE.md)
- 🗺️ Roadmap: [ROADMAP.md](https://github.com/ultraworkers/claw-code/blob/main/ROADMAP.md)
- 💬 Discord: UltraWorkers Discord

## Why Rust?

| 对比维度 | Rust | Python |
|----------|------|--------|
| 性能 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 内存安全 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 跨平台 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| AI/ML 生态 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| 学习曲线 | ⭐⭐ | ⭐⭐⭐⭐ |

**结论**：Rust 适合企业级、高性能场景；Python 适合快速原型、研究场景。

## Notes

- Stars 最高（184K），但增长已稳定
- 适合追求性能的开发者
- ACP 支持仍在开发中