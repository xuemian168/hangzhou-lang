# 贡献指南 - 杭州话编程语言

## 🌟 欢迎来到杭州话编程语言项目！

感谢你有兴趣为杭州话编程语言做出贡献！本文档将指导你如何参与到这个充满创意和地方特色的开源项目中。

### 📖 项目愿景

我们的目标是：
- 保护和传播杭州方言文化
- 创造一个有趣且实用的编程语言
- 建立一个开放、包容的开发者社区

### 🤝 贡献方式

你可以通过以下方式为项目做贡献：

#### 1. 代码贡献
- 修复 Bug
- 添加新功能
- 优化现有代码
- 改进性能

#### 2. 语言扩展
- 添加新的杭州话关键字
- 完善词典工具
- 改进语法解析器
- 扩展内置函数库

#### 3. 文档贡献
- 改进项目文档
- 编写使用教程
- 翻译文档
- 添加代码示例

#### 4. 测试与质量
- 编写单元测试
- 进行代码审查
- 报告 Bug
- 提供性能优化建议

### 🛠 开发环境准备

#### 前置条件
- Python 3.7+
- UTF-8 编码支持
- Git

#### 克隆项目
```bash
git clone https://github.com/xuemian168/hangzhou-lang.git
cd hangzhou-lang
```

#### 安装依赖
```bash
# 建议使用虚拟环境
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -r requirements-dev.txt
```

### 🔍 开发流程

1. **Fork 项目**
   - 访问 [项目主页](https://github.com/xuemian168/hangzhou-lang)
   - 点击右上角 "Fork" 按钮

2. **创建分支**
```bash
git checkout -b feature/your-feature-name
```

3. **提交代码**
   - 遵循代码规范
   - 编写清晰的提交信息
```bash
git add .
git commit -m "feat: 添加新的杭州话关键字 '老倌'"
```

4. **推送代码**
```bash
git push origin feature/your-feature-name
```

5. **创建 Pull Request**
   - 在 GitHub 上创建 PR
   - 描述你的更改
   - 等待代码审查

### 📝 代码规范

#### Python 编码规范
- 遵循 PEP 8 风格指南
- 使用类型注解
- 编写文档字符串
- 保持代码简洁和可读性

#### 杭州话语言规范
- 确保新增关键字符合杭州方言特色
- 保持语法的一致性
- 添加词典和示例

### 🐛 Bug 报告

使用 GitHub Issues 报告 Bug：
- 提供详细的错误描述
- 包含复现步骤
- 提供错误截图（如果可能）
- 说明你的开发环境

### 📚 词汇贡献指南

#### 添加新词汇
1. 编辑 `src/keywords.py`
2. 在 `hangzhou_dict.py` 中添加词典条目
3. 提供普通话对照和使用示例

#### 词汇分类
- 关键字
- 时间表达
- 家庭称谓
- 程度副词
- 动作词汇
- 形容词
- 疑问词
- 量词

### 🏆 贡献者激励

- 所有贡献者将被记录在 CONTRIBUTORS.md
- 重要贡献者可获得项目纪念徽章
- 优秀贡献将在项目文档中展示

### 📜 许可证

本项目采用 MIT 许可证。提交代码即表示你同意遵守项目许可证。

### 💬 联系我们

- 项目主页：https://github.com/xuemian168/hangzhou-lang
- 问题反馈：https://github.com/xuemian168/hangzhou-lang/issues
- 邮箱：xuemian888@gmail.com

### 🌈 最后的话

感谢你对杭州话编程语言项目的兴趣！让我们一起用代码传播杭州方言文化，创造更有温度的技术！

**让编程说杭州话，让代码更有灵魂！** 