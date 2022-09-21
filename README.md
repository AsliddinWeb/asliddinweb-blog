Avval Github'dan omborni klonlang va yangi katalogga o'ting:

$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
Loyihangiz uchun virtualenvni faollashtiring.

Loyihaga bog'liqliklarni o'rnatish:

$ pip install -r requirements/local.txt
Keyin shunchaki migratsiyalarni qo'llang:

$ python manage.py migrate
Endi siz ishlab chiqish serverini ishga tushirishingiz mumkin:

$ python manage.py runserver
