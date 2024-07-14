<!-- <div style="display: flex; justify-content: center; align-items: center;">
  <img src="./staticfiles/img/zalon_design_logo.png" alt="zalon design logo" width="250"/>
</div> -->

ViandasGo platform.

[Website here](https://viandasgo.app/)

## Tech stack

- **Backend:**
  - [Django](https://www.djangoproject.com/)
    - [Django CKEditor 5](https://pypi.org/project/django-ckeditor-5/): for rich
      text editing
- **Frontend:**
  - Django Templates
  - JavaScript
    - [Splide.js](https://splidejs.com/): for carousels.
  - CSS for styling
    - [Tailwind CSS Framework](https://tailwindcss.com/): for general styling - We use
      Tailwind with the help of
      [django-tailwind](https://pypi.org/project/django-tailwind/)
    - [Lineicons](https://lineicons.com/): for icons
    - Some CSS files for custom styling. One for general rules directly in
      _staticfiles_ and another others in every app directory that needs it.

## Apps
- **Main:** The main app of the project. It contains the main views and
  templates. Like the landing page, and the contact page.
- **Clients:** The clients app contains the views and templates for the clients
  section. Here the clients can see the menu and make orders.
- **Food Places:** The food places app contains the views and templates for the
  food places section. Here the food places can manage their menu schedule and orders.
- **Payments:** The payments app contains the views and templates for the payments
  section. Here the clients can see the payment methods and make payments.
- **Internal:** The internal app contains the views and templates us, the ViandasGo
  team, use to manage the platform. Here we can manage the clients, food places,
  orders, and payments. This is aimed to be used through the Django admin panel.


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
