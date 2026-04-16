# Framework Comparison Matrix

> Last updated: 2026-04-16

## Overview

| Framework | Category | Stars | Forks | Language | Active |
|-----------|----------|-------|-------|----------|--------|
| **OpenClaw** | Platform | 358,474 | 72,876 | TypeScript | ✅ |
| **AutoGPT** | General | 183,481 | 46,223 | Python | ✅ |
| **AutoGen** | General | 57,138 | 8,598 | Python | ✅ |
| **MetaGPT** | General | 52,821 | 6,255 | Python | ✅ |
| **CrewAI** | General | 48,996 | 6,698 | Python | ✅ |
| **LangGraph** | General | 29,416 | 5,033 | Python | ✅ |
| **Swarm** | General | 21,316 | 2,276 | Python | ✅ |
| **AI-Scientist** | Research | 8,216 | 945 | Python | ✅ |
| **AutoResearchClaw** | Research | 11,232 | 1,285 | Python | ✅ |
| **Research-Claw** | Research | 696 | 91 | TypeScript | ✅ |

---

## Category Analysis

### 🏆 Platform (开源运行平台)

| Framework | Stars | Description |
|-----------|-------|-------------|
| **OpenClaw** | 358K | Your own personal AI assistant. Any OS. Any Platform. |

**特点**：
- 跨平台支持（Windows/macOS/Linux）
- 技能系统 + 多渠道接入
- Manager-Worker 架构
- 最活跃的社区（18K+ Issues）

---

### 🔧 General Purpose (通用框架)

| Framework | Stars | Architecture | Best For |
|-----------|-------|--------------|----------|
| **AutoGPT** | 183K | Single Agent | 自主任务执行 |
| **AutoGen** | 57K | Multi-Agent | 对话式协作 |
| **MetaGPT** | 53K | Role-based | 软件开发流程 |
| **CrewAI** | 49K | Role-playing | 团队协作场景 |
| **LangGraph** | 29K | Graph-based | 状态管理 + 流程控制 |
| **Swarm** | 21K | Lightweight | 简单编排教学 |

**选择指南**：
- 🎯 快速上手 → **Swarm**（最轻量）
- 🏢 企业级 → **AutoGen**（微软背书）
- 💼 软件开发 → **MetaGPT**（角色分工）
- 📊 流程控制 → **LangGraph**（图结构）
- 🤝 团队协作 → **CrewAI**（角色扮演）

---

### 🔬 Research (研究型)

| Framework | Stars | Description |
|-----------|-------|-------------|
| **AutoResearchClaw** | 11K | 从 Idea 到 Paper 全流程自动化 |
| **AI-Scientist** | 8K | 自动化科学研究 |
| **Research-Claw** | 696 | 让每个人成为 PI |

**特点**：
- 📝 论文自动生成
- 🔍 自动文献调研
- 🧪 实验设计建议
- 📊 结果分析整理

---

## Technical Comparison

| Framework | Language | Learning Curve | Extensibility | Production Ready |
|-----------|----------|----------------|---------------|------------------|
| OpenClaw | TypeScript | Medium | ⭐⭐⭐⭐⭐ | ✅ |
| AutoGPT | Python | Low | ⭐⭐⭐⭐ | ✅ |
| AutoGen | Python | Medium | ⭐⭐⭐⭐⭐ | ✅ |
| MetaGPT | Python | Medium | ⭐⭐⭐⭐ | ✅ |
| CrewAI | Python | Low | ⭐⭐⭐⭐ | ✅ |
| LangGraph | Python | High | ⭐⭐⭐⭐⭐ | ✅ |
| Swarm | Python | Very Low | ⭐⭐⭐ | 🧪 Educational |
| AI-Scientist | Python | High | ⭐⭐⭐ | 🧪 Research |
| AutoResearchClaw | Python | Medium | ⭐⭐⭐⭐ | ✅ |

---

## Use Case Mapping

| Use Case | Recommended Framework |
|----------|----------------------|
| **个人 AI 助手** | OpenClaw |
| **自动化任务执行** | AutoGPT |
| **多 Agent 协作开发** | AutoGen, MetaGPT |
| **企业流程自动化** | CrewAI, LangGraph |
| **学术论文研究** | AutoResearchClaw, AI-Scientist |
| **学习 Agent 编排** | Swarm |
| **状态复杂的流程** | LangGraph |

---

## Ecosystem Size

| Framework | Community | Docs | Examples | Plugins |
|-----------|-----------|------|----------|---------|
| OpenClaw | 🔥🔥🔥🔥🔥 | ✅ | ✅ | 100+ Skills |
| AutoGPT | 🔥🔥🔥🔥🔥 | ✅ | ✅ | Plugins |
| AutoGen | 🔥🔥🔥🔥 | ✅ | ✅ | Extensions |
| CrewAI | 🔥🔥🔥🔥 | ✅ | ✅ | Tools |
| LangGraph | 🔥🔥🔥 | ✅ | ✅ | LangChain |
| MetaGPT | 🔥🔥🔥🔥 | ✅ | ✅ | Limited |
| Swarm | 🔥🔥🔥 | ✅ | ✅ | None |

---

## Quick Decision Tree

```
你的需求是什么？
│
├─ 🏠 个人使用 → OpenClaw
│
├─ 🏢 企业部署
│   ├─ 需要微软支持 → AutoGen
│   ├─ 需要角色分工 → MetaGPT / CrewAI
│   └─ 需要流程控制 → LangGraph
│
├─ 🔬 学术研究 → AutoResearchClaw / AI-Scientist
│
├─ 🎓 学习 Agent → Swarm
│
└─ 🤖 自主任务 → AutoGPT
```

---

*Data sourced from GitHub API. Updated weekly.*