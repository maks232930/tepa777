# tepa777

ВРЕМЕННО ДОСТУПЕН ПО АДРЕСУ: http://95.128.71.65/

sudo apt update

Установка Nginx
sudo apt install nginx
sudo systemctl enable nginx
sudo service nginx status

Установка всех необходимых элементов
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo apt install python3-ven

Создание виртуальной среды Python
python3 -m venv venv
source venv/bin/activate

Установка приложения
git clone https://github.com/maks232930/tepa777
pip install -r requirements.txt

touch .env 
С содержанием:
FLASK_APP=builder
SECRET_KEY=SECRET_KEY
SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://USER:PASSWORD@localhost/BD или не указывать и содаться sqlite

Для установки postgresql
sudo apt install postgresql postgresql-contrib

sudo -u postgres createuser USERNAME -P --interactive
![image](https://github.com/maks232930/tepa777/assets/53191956/2374be0b-caca-4bee-b467-48deb8c2650a)

![image](https://github.com/maks232930/tepa777/assets/53191956/e7c4f922-d813-42d0-9be4-5e2740f6928e)
Указываем USERNAME И PASSWORD в файле .env

mkdir migrations/versions

flask db migrate
flask db upgrade

Настройка Gunicorn
Создать файл
sudo vi etc/systemd/system/tepa777.service
С содержанием:
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

Запустим созданную службу Gunicorn и активируем ее запуск при загрузке системы:
sudo systemctl start tepa777
sudo systemctl enable tepa777

Настройка Nginx
sudo vi /etc/nginx/sites-available/tepa777
Содержание:
server {
    listen 80;
    server_name IP or domain;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/USER/tepa777/tepa777.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/tepa777 /etc/nginx/sites-enabled
sudo systemctl restart nginx
sudo ufw allow 'Nginx Full'




