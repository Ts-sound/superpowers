# ${PROJECT_NAME}

项目简要描述。

**语言切换**: [English](README.md) | [中文](README.zh.md)

## 功能特性

- 功能 1
- 功能 2

## 安装

### 方式一：虚拟环境（推荐）

```powershell
# Windows
.\scripts\setup-venv.ps1
.\.venv\Scripts\Activate.ps1
```

```bash
# Unix
./scripts/setup.sh
source venv/bin/activate
```

### 方式二：全局安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
python main.py
```

## 测试

```bash
pytest tests/ -v
pytest tests/ --cov=src --cov-report=html
```

## 打包

```powershell
# Windows
pyinstaller -F -w -n "${PROJECT_NAME}" main.py
```

```bash
# Unix
./scripts/build.sh
```

## 文档

详见 [docs/](docs/) 目录。

## 许可证

MIT License - 查看 [LICENSE](LICENSE)