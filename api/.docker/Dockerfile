# Используем легковесную версию Python 3.11 с базовым образом Alpine Linux 3.18
FROM python:3.11.6-alpine3.18

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем системные зависимости
# Здесь мы устанавливаем postgresql-dev, не забывайте о кэшировании слоев
RUN apk add --no-cache postgresql-dev

# Копируем только файл requirements.txt сначала, чтобы использовать кэш Docker
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем остальной код приложения в текущую директорию в контейнере
COPY . .

# Копируем скрипт dev.sh в текущую директорию в контейнере
COPY script/dev.sh .
