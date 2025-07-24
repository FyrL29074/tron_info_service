# Tron Info Service

Сервис для работы с кошельками в сети TRON.  
Позволяет получать и сохранять информацию о балансе, bandwidth и energy кошельков.

---

## Особенности

- Получение баланса, bandwidth и energy кошельков TRON
- Сохранение информации в базу данных
- REST API для добавления и получения данных кошельков
- Тесты с моками для работы с сетью TRON

---

## Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:fyrl29074/tron_info_service.git
cd tron_info_service
```

2. Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

# Запуск
```bash
uvicorn app.api.main:app --reload
```
API будет доступен по адресу: http://127.0.0.1:8000

# Тесты
Запуск тестов:
```bash
pytest tests/
```

# Как использовать:
- POST /api/wallet с JSON:
{
  "address": "TWjGXki59uJWpBfsX5wU2EybPt2CW8TvV3"
}
- GET /api/wallet?skip=0&limit=10 — получить список сохранённых кошельков. 
