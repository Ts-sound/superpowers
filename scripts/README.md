# Scripts

## dev-link.sh

将当前 superpowers 仓库以符号链接方式安装到 Claude Code 插件系统，修改即刻同步，无需重新安装。

```bash
./scripts/dev-link.sh
```

做了什么：
1. 注册本地 `superpowers-dev` 市场（如已存在则跳过）
2. 通过插件系统安装 `superpowers@superpowers-dev`
3. 将 cache 目录替换为指向仓库的符号链接

此后修改仓库中任意 skill、hook、agent 文件，Claude Code 读到的是最新内容。
版本号变更（`.claude-plugin/plugin.json` 中的 `version`）后需重新运行。
