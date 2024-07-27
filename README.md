# ViandasGo Platform (Work in progress...)
ViandasGo is a platform where food places can publish their menu and schedule, and clients can see the menu, make orders, and pay for them beforehand programming their lunches of the entire week. The platform is aimed to be used by small food places that don't have the resources to develop their own platform providing also an optimal way of provisions purchase for them, and by clients that want to have a more organized way to order food **mainly solving the issue for those who work and don't have time to cook or go out to eat.**


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

# Some tech notes or clarifications

- Tailwind is integrated using the `django-tailwind` package, as was mentioned before. And it requires the `python manage.py tailwind start` command in development mode to compile the CSS needed in the templates, this triggers the watch mode for the Tailwind CSS compiler, that's why it needs a separate process to keep it running: hence we have the _tailwind_ service in the `docker-compose.yml` file.

---------------

# Author's notes
> I do not believe in the foolishness of investing resources in protecting code. The success of businesses is not the idea nor the technology that implements it; but rather the execution of all parts that make it up. That is why I am keeping this project open-source for the moment. There are no use cases programmed here that do not already exist in the world, and perhaps it can serve someone as a guide or example for working with Django, django-tailwind, HTMX, and Docker.

>**By: Fausto Márquez**

> This project also makes use of a lot of my friend, partner and colleague's work and wisdom, [@CrhistyanSilva](https://github.com/CrhistyanSilva), who is one of the best engineers I have ever met, and even a better person. For more about his work and research over the Python + Django ecosystem visit our [Falcode's Documentation](https://docs.falcode.dev/django/).