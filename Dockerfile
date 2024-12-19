# 使用官方Python镜像作为基础镜像
FROM python:3.12-alpine

LABEL maintainer="lipengcheng"

# 安装PCRE库和其他依赖
RUN apk update && apk add pcre pcre-dev gcc libc-dev linux-headers

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于容器内的/app中
COPY . /app

# 创建日志目录并设置权限
RUN mkdir -p /app/logs && chown -R 1000:1000 /app/logs

# 使用阿里云镜像源安装依赖g
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 确保start.sh脚本可执行
RUN chmod +x start.sh

# 使用启动脚本作为容器的默认命令
CMD ["./start.sh"]
