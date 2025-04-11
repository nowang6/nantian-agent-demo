 # Nantian Agent Demo

这是一个基于 Python 的智能代理演示项目，使用 OpenAI API 和 Deepseek API 进行开发。

## 环境要求

- Python >= 3.12
- pip 或 uv 包管理器

## 安装步骤

1. 克隆项目到本地：
```bash
git clone [your-repository-url]
cd nantian-agent-demo
```

2. 创建并激活虚拟环境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
# 或使用 uv
uv pip install -r requirements.txt
```

4. 配置环境变量：
```bash
cp .env.example .env
```
然后编辑 `.env` 文件，填入相应的 API 密钥和配置信息。

## 项目结构

```
nantian-agent-demo/
├── src/
│   ├── agent/     # 代理相关代码
│   ├── mcp/       # MCP 相关代码
│   └── basic/     # 基础功能代码
├── .env           # 环境变量配置
├── .env.example   # 环境变量示例
└── pyproject.toml # 项目配置和依赖管理
```

## 主要依赖

- helium >= 5.1.1
- pillow >= 11.1.0
- pydantic-ai >= 0.0.53
- pydantic-graph >= 0.0.53
- python-dotenv >= 1.0.0
- selenium >= 4.31.0
- smolagents >= 1.13.0
- torch >= 2.6.0
- transformers >= 4.51.1

## 使用说明

1. 确保已正确配置所有环境变量
2. 运行相应的 Python 脚本或模块
3. 查看日志输出以了解运行状态

## 注意事项

- 请妥善保管 API 密钥，不要将其提交到版本控制系统
- 建议使用虚拟环境来隔离项目依赖
- 确保网络连接正常，以便访问 API 服务

