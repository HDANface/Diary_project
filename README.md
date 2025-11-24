# Django 任务管理系统

一个基于 Django 构建的简单高效任务管理应用，支持任务的创建、查看、编辑、删除（CRUD）等核心操作，帮助用户轻松管理日常任务。

## 功能特点

- **任务管理**：完整支持任务的创建、查看、编辑与删除
- **响应式设计**：适配桌面端和移动端，随时随地管理任务
- **实时时钟**：首页显示当前时间，直观掌握时间节点
- **任务搜索**：快速检索目标任务，提高管理效率
- **任务统计**：侧边栏展示总任务数，全局掌握任务规模
- **友好界面**：基于 Tailwind CSS 打造简洁直观的操作界面，搭配 Font Awesome 图标提升视觉体验

## 技术栈

- **后端**：Django 5.2.6
- **前端**：HTML、Tailwind CSS、JavaScript
- **数据库**：SQLite（Django 默认数据库）
- **UI 组件**：Font Awesome 图标库

## 安装与部署

### 1. 克隆仓库

```bash
git clone <仓库地址>
cd To_do-list/commission
```

### 2. 创建并激活虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# Windows 激活虚拟环境
venv\Scripts\activate

# macOS/Linux 激活虚拟环境
source venv/bin/activate
```



```bash
pip install django==5.2.6
```

### 4. 数据库迁移

```bash
python manage.py migrate
```

### 5. 启动开发服务器

```bash
python manage.py runserver
```

### 6. 访问应用

打开浏览器，输入地址 `http://127.0.0.1:8000/` 即可进入应用

## 使用说明

- **首页**：展示最近 6 条任务，同时显示实时时钟
- **任务列表**：查看所有任务，通过搜索框快速筛选目标任务
- **创建任务**：点击「添加新任务」按钮，填写任务标题、作者和备注信息完成创建
- **编辑任务**：点击任意任务卡片上的「编辑」按钮，修改任务详情后保存
- **删除任务**：点击任意任务卡片上的「删除」按钮，确认后即可移除任务

## 项目结构

- `note/models.py`：定义任务（Subject）数据模型
- `note/views.py`：处理应用核心业务逻辑与视图渲染
- `note/forms.py`：管理任务创建 / 编辑的表单验证规则
- `note/templates/`：存储所有页面的 HTML 模板文件
- `commission/settings.py`：Django 项目核心配置文件
