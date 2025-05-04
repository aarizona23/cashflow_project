# Cashflow Web App

Веб-приложение для управления денежными потоками с возможностью фильтрации по дате, статусу, типу, категории и подкатегории.

---

## Инструкция по запуску проекта

### 🔧 1. Клонирование репозитория

```bash
git clone https://github.com/aarizona23/cashflow_project.git
cd cashflow
```

2. Создание и активация виртуального окружения
```bash
python -m venv venv
source venv/bin/activate        # для Linux/macOS
venv\Scripts\activate           # для Windows
```

3. Установка зависимостей
```bash
pip install -r requirements.txt
```

4. База данных данных
По умолчанию используется SQLite.

5. Применение миграций и создание суперпользователя
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Следуйте инструкциям для создания учётной записи администратора.

▶️ 6. Запуск сервера разработки
```bash
python manage.py runserver
```
Админка доступна по адресу: http://127.0.0.1:8000/admin/
Приложение будет доступно по адресу: http://127.0.0.1:8000/cashflow/index/
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/fc915a93-d96e-411b-b26c-cafacbd3ce90" />
Нажмите "Управление справочниками", чтобы перейти в другую страницу где можно создавать, редактировать либо удалять статусы, типы, категории, подкатегории.
<img width="1425" alt="image" src="https://github.com/user-attachments/assets/a6ebd573-2412-48c8-9e19-ac614cf1515e" />

Фильтрация записей. После выбора нужных параметров нажмите "Применить", чтобы обновить список записей.
Нажмите "Добавить запись", чтобы перейти в другую страницу для добавления новой записи.
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/1fc6bec2-913b-49c2-8d73-de69bdabf93c" />

Нажмите кнопку редактирования справа от записи в таблице, чтобы перейти в другую страницу для редактирования этой записи.
<img width="1431" alt="image" src="https://github.com/user-attachments/assets/b9e5f16d-0884-493a-9b35-109e0bb908d2" />

Нажмите кнопку удаления справа от записи в таблице, чтобы удалить запись.

