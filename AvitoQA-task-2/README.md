## How to use it 

1. Создайте venv и установите все необходимые зависимости:

    ```bash
        python -m venv venv
        venv\Scripts\activate
    ```
    Установите pytest-playwright

    ```bash
        pip install pytest-playwright
        playwright install
    ```    

2. Запустите инциализацию тестовых данных:

    ```bash
        python init.py
    ```
    Полученные mock'и для выполнения тестов будут находиться в директории `mock/`

3. Запустите выполнение параметризованных тестов `def test_counter(context, test)`

4. Полученные скриншоты будут находиться в директории `output/`