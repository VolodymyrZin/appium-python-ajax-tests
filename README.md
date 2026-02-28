## Ajax Systems, Python developer in test for Application team

# Appium Python Automation Framework

## Опис
Цей проєкт — тестова автоматизація мобільного застосунку Ajax Systems за допомогою **Appium** та **Pytest**.  
Використовується патерн **Page Object Model** для підтримки чистої архітектури та зручності розширення.

## Структура проєкту
dev_in_test_app_teamss/ 
├── framework/        # базові утиліти та драйвер 
├── pages/            # Page Object класи 
├── tests/            # тестові сценарії 
├── pytest.ini        # конфігурація pytest 
├── requirements.txt  # залежності 
├── README.md         # документація 
└── .gitignore        # виключені файли
|__ .env



## Використані технології
- **Python 3.10+**
- **Appium**
- **Pytest**
- **Selenium WebDriver**
- **python-dotenv** для роботи з `.env`

## Налаштування
1. Клонувати репозиторій:
   ```bash
   git clone https://github.com/VolodymyrZin/dev_in_test_app_teamss.git
   cd dev_in_test_app_teamss

2. Створити віртуальне середовище та встановити залежності:

    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows
    pip install -r requirements.txt

3. Створити .env файл у корені проєкту:

    LOGIN=your_login
    PASSWORD=your_password
    PASSWORD_WRONG=wrong_password
    NAME=your_name

4. Запустити тести:

    pytest -v --alluredir=reports

5. Приклад тестів
   - Авторизація: позитивний та негативний сценарій логіну.
   - Редагування акаунту: зміна імені користувача.
   - Навігація: перевірка елементів та порядку у navbar.
   Логи та репорти
   - Логи зберігаються у test_logs.log (ігнорується у .gitignore).
   - Результати тестів можна переглядати через Allure Report.

   
### Корисні посилання:
1) Застосунок Ajax Systems - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Робота з реальним телефоном - https://developer.android.com/tools/adb
3) Налаштування емулятора - https://developer.android.com/studio/run/emulator
4) Драйвер - http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/
5) Appium Inspector - https://github.com/appium/appium-inspector
