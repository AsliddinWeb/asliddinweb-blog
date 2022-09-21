git clone https://github.com/AsliddinWeb/asliddinweb-blog.git

cd asliddinweb-blog

pip install -r requirements/local.txt

python manage.py migrate

python manage.py runserver
