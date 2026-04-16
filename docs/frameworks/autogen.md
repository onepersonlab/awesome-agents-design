# AutoGen

> **A programming framework for agentic AI**

## Quick Stats

| Metric | Value |
|--------|-------|
| **Stars** | 57,138 |
| **Forks** | 8,598 |
| **Language** | Python |
| **Issues** | 766 |

## Overview

Microsoft 开发的多 Agent 对话框架，主打：

- 💬 **对话式协作**：Agent 通过对话完成任务
- 🔧 **可定制 Agent**：角色、工具、记忆皆可配置
- 🏢 **企业级支持**：微软背书，生态成熟

## Architecture

```
User Proxy Agent
    ├── 发送消息给其他 Agent
    ├── 执行代码
    └── 人类介入
    │
Assistant Agent
    ├── 接收消息
    ├── 生成代码/回复
    └── 调用工具
```

## Key Features

1. **对话式编排**：Agent 通过对话协作
2. **代码执行**：支持 Python 代码执行
3. **人类介入**：User Proxy 可随时介入
4. **工具集成**：支持函数调用

## Links

- 📦 GitHub: https://github.com/microsoft/autogen
- 📚 Docs: https://microsoft.github.io/autogen
- 📄 Paper: https://arxiv.org/abs/2308.08155

## When to Use

- ✅ 需要微软生态支持
- ✅ 对话式协作场景
- ✅ 企业级部署
- ✅ 需要人类介入控制