# SOGRACE CRM SaaS M1.1 - Database + Docker Foundation

本版本是 SOGRACE CRM SaaS 的第一阶段地基版本。

## 目标
- 不再使用旧版巨型 main.py
- 使用 FastAPI 模块化后端
- 使用 PostgreSQL
- 使用 Docker Compose 管理服务
- 建立 SaaS 基础数据表

## 包含模块
- users
- companies
- contacts
- leads
- emails
- timeline
- tasks

## 启动
```bash
docker compose up -d --build
```

## 测试
```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/docs
```

## 默认后端地址
http://127.0.0.1:8000

## 当前阶段
M1.1 Database + Docker Foundation
