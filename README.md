Countries & Requirements
=====

Installation
------

The project uses `pipenv` to manage its dependencies. Create a virtual environment by running

```
pipenv install
```

Activate it:

```
pipenv shell
```

Then init the database. `sqlite` is the default.

```
./manage.py migrate
```

If you have `DEBUG = True` in your settings this will also create users with
following credentials

```
admin/admin
editor/editor
readonly/readonly
external/external
```

Then you can run the server:

```
./manage.py runserver
```

Implementation
------

The project uses its own `users.User` model, adding a required `role` field. A custom permission system is implemented with `users.permissions.RoleMixin`.

To see it in use go to the `app.roles` module.
