FROM continuumio/miniconda3

WORKDIR /app

RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Cài đặt các thư viện Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Tạo thư mục log cho supervisor
RUN mkdir -p /var/log/supervisor && chmod -R 777 /var/log/supervisor

# Cấu hình Nginx và Supervisor
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf



EXPOSE 8888 8000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]


