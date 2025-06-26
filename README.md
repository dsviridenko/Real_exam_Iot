# Exam

## Запуск проекта

1. Склонируйте репозиторий и перейдите в папку проекта.
   ``` bash
   git clone https://github.com/dsviridenko/exam_IOT.git
   ```
 
2. Откройте терминал и запустите виртуальное окружение
   ``` bash
   python -m venv venv
   ```
   Затем активируйте его
   *Если у вас Windows:
   ``` bash
   venv\Scripts\activate
   ```
   *Если Linux или MacOS:
   ``` bash
   source venv/bin/activate
   ```
3. Установите зависимости
   ``` bash
   pip install -r requerements
   ```
4. Запустите приложение
   ``` bash 
   uvicorn main:app --reload
   ```
