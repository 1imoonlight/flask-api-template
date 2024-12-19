#!/bin/sh

# 默认参数
DEFAULT_WORKERS=4
DEFAULT_PORT=8890

# 环境变量
WORKERS=${UWSGI_WORKERS:-$DEFAULT_WORKERS}
PORT=${UWSGI_PORT:-$DEFAULT_PORT}

# 启动uWSGI服务
exec uwsgi \
    --http "0.0.0.0:${PORT}" \
    --wsgi-file app.py \
    --callable flask_app \
    --workers "$WORKERS" \
    --master \
    --enable-threads \
    --uid 1000 \
    --gid 1000
