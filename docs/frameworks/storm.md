# STORM (stanford-oval/storm)

> **Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking**

## Quick Stats

| Metric | Value |
|--------|-------|
| **Stars** | 28,088 |
| **Daily Stars** | +7 |
| **Language** | Python |
| **Contributors** | 26 |

## Overview

Stanford OVAIL 实验室开发的研究型写作系统，专注于生成 Wikipedia 风格的长文章。

**核心理念**：通过 Internet 搜索 + 多视角提问，生成带引用的长文章。

## How STORM Works

### Two-Stage Process

```
1. Pre-writing Stage
   ├─ Internet-based research
   ├─ Collect references
   └─ Generate outline
   ↓
2. Writing Stage
   ├─ Use outline + references
   ├─ Generate full-length article
   └─ Add citations
```

### Co-STORM（协作模式）

- Human-AI 协作知识整理
- 支持人类实时介入
- 更偏好对齐的信息检索

## Key Features

1. **引用生成**
   - 自动收集 Internet 参考文献
   - 在文章中添加引用

2. **多视角提问**
   - 从不同角度提问
   - 生成全面的文章大纲

3. **多种 LLM 支持**
   - LiteLLM 集成
   - 支持多种 embedding 模型

4. **VectorRM**
   - 支持用户自定义文档
   - 补充搜索引擎支持

## Installation

```bash
pip install knowledge-storm
```

## Use Cases

- ✅ Wikipedia 风格文章生成
- ✅ 文献综述
- ✅ 知识整理
- ✅ 研究预写阶段

## Links

- 🏠 Demo: https://storm.genie.stanford.edu
- 📦 GitHub: https://github.com/stanford-oval/storm
- 📄 Paper: [STORM](https://arxiv.org/abs/2402.14207), [Co-STORM](https://arxiv.org/abs/2408.15232)
- 🌐 Website: https://storm-project.stanford.edu

## Academic Recognition

- NAACL 2024 Presentation
- EMNLP 2024 (Co-STORM)
- 70,000+ 人试用 Demo

## Notes

- 已被 Wikipedia 编辑用于预写阶段
- 适合生成带引用的知识性文章
- 不适合直接发表（需要人类编辑）