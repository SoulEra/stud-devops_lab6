Flask+redis – веб-приложение со счетчиком входов;
Prometheus+grafana – сервер мониторинга.
Необходимо настроить сбор метрик с приложения на систему мониторинга.

Flask App http://localhost:5000
Prometheus http://localhost:9090
Grafana http://localhost:3000

Копирование проекта с репозитория
```
git clone https://github.com/SoulEra/stud-devops_lab6.git
cd situ-devops-06
```
Запуск 
```
docker compose up -d --build
```
Проверка через curl
```
root@srv-devops:/home/user/my_homework6# curl http://localhost:5000

        <h1>Счётчик посещений</h1>
        <p>Вы посетили эту страницу 9 раз(а).</p>
    root@srv-devops:/home/user/my_homework6#
```
Проверка через веб
<img width="741" height="265" alt="1" src="https://github.com/user-attachments/assets/71077f18-50a3-41e1-a93f-77d47be63cca" />
