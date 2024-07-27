# ViandasGo Platform
ViandasGo aims to be a platform where food places can publish their menu and schedule, and clients can see the menu, make orders, and pay for them beforehand programming the delivery or pickup time. The platform is aimed to be used by small food places that don't have the resources to develop their own platform, and by clients that want to have a more organized way to order food.


URL: [viandasgo.uy](https://viandasgo.app/)

## Tech stack

- **Backend:**
  - [Django](https://www.djangoproject.com/)
    - [Django CKEditor 5](https://pypi.org/project/django-ckeditor-5/): for rich
      text editing
- **Frontend:**
  - Django Templates
  - HTMX: for easy dynamic content loading. We use it with Django templates with
    the help of [django-htmx](https://pypi.org/project/django-htmx/)
  - JavaScript
    - [Splide.js](https://splidejs.com/): for carousels.
  - CSS for styling
    - [Tailwind CSS Framework](https://tailwindcss.com/): for general styling - We use
      Tailwind with the help of
      [django-tailwind](https://pypi.org/project/django-tailwind/)
    - Some CSS files for custom styling. One for general rules directly in
      _staticfiles_ and another others in every app directory that needs it.
  - Icons from [Heroicons](https://heroicons.com/)
- **Database:**
  - PostgreSQL

## Apps
- **Core:** The core app of the project. It contains the main views and
  templates. Like the landing page, and the contact page. Also authentication is managed here.
- **Clients:** The clients app contains the views and templates for the clients
  section. Here the clients can see the menu and make orders.
- **Food Places:** The food places app contains the views and templates for the
  food places section. Here the food places can manage their menu schedule and orders.
- **Payments:** The payments app contains the views and templates for the payments
  section. Here the clients can see the payment methods and make payments.
- **Internal:** The internal app contains the views and templates us, the ViandasGo
  team, use to manage the platform. Here we can manage the clients, food places,
  orders, and payments. This is aimed to be used through the Django admin panel.

### Theme app
Yes actually `theme` is a django app too, that's the way `django-tailwind` works. But I kept it outside the apps folder.



## Run the project

```bash
docker compose up
```

You'll get the app running on `http://localhost:8000`

## Make and apply migrations

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

## Collect statics

```bash
docker compose exec web python manage.py collectstatic
```

# Some notes or clarifications

- Tailwind is integrated using the `django-tailwind` package, as was mentioned before. And it requires the `python manage.py tailwind start` command in development mode to compile the CSS needed in the templates, this triggers the watch mode for the Tailwind CSS compiler, that's why it needs a separate process to keep it running: hence we have the _tailwind_ service in the `docker-compose.yml` file.