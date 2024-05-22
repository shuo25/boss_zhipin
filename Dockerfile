# 使用官方Python基础镜像
FROM python:3.8

# 设置 pip 镜像源为国内源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露Flask应用端口
EXPOSE 8088

# 启动脚本
ENTRYPOINT ["sh", "./run.sh"]
