# tepa777

# ВРЕМЕННО ДОСТУПЕН ПО АДРЕСУ: https://python-top.space/

sudo apt update

## Установка Nginx
sudo apt install nginx<br/>
sudo systemctl enable nginx<br/>
sudo service nginx status<br/>

## Установка всех необходимых элементов
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv

## Создание виртуальной среды Python
python3 -m venv venv<br/>
source venv/bin/activate<br/>

## Установка приложения
git clone https://github.com/maks232930/tepa777<br/>
pip install -r requirements.txt<br/>

### touch .env 
С содержанием:<br/>
FLASK_APP=builder<br/>
SECRET_KEY=SECRET_KEY<br/>
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://USER:PASSWORD@localhost/BD или не указывать и создаться sqlite<br/>

## Для установки postgresql
sudo apt install postgresql postgresql-contrib<br/>

sudo -u postgres createuser USERNAME -P --interactive<br/>
![image](https://github.com/maks232930/tepa777/assets/53191956/2374be0b-caca-4bee-b467-48deb8c2650a)<br/>

![image](https://github.com/maks232930/tepa777/assets/53191956/e7c4f922-d813-42d0-9be4-5e2740f6928e)<br/>
Указываем USERNAME И PASSWORD в файле .env<br/>

mkdir migrations/versions<br/>

flask db migrate<br/>
flask db upgrade<br/>

## Настройка Gunicorn
Создать файл<br/>
sudo vi etc/systemd/system/tepa777.service<br/>
С содержанием:<br/>
```
Description=Gunicorn instance
After=network.target

[Service]
User=USER
Group=www-data

WorkingDirectory=/home/USER/tepa777
Environment="PATH=/home/USER/tepa777/venv/bin"
ExecStart=/home/USER/tepa777/venv/bin/gunicorn --workers 3 --bind unix:tepa777.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
Запустим созданную службу Gunicorn и активируем ее запуск при загрузке системы:<br/>
sudo systemctl start tepa777<br/>
sudo systemctl enable tepa777<br/>

## Настройка Nginx
sudo vi /etc/nginx/sites-available/tepa777<br/>
Содержание:
```
server {
    listen 80;
    server_name IP or domain;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/USER/tepa777/tepa777.sock;
    }
}
```
sudo ln -s /etc/nginx/sites-available/tepa777 /etc/nginx/sites-enabled<br/>
sudo systemctl restart nginx<br/>
sudo ufw allow 'Nginx Full'<br/>




