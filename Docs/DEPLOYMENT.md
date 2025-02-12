
# Deployment Guide

## 1. Making a Local Clone

To clone the project repository to your local machine, run the following command:

```bash
git clone https://github.com/your-username/buyback.git
cd buyback
```

Replace `your-username` with your GitHub username or the appropriate repository URL.

## 2. Creating a PostgreSQL Database

### Install PostgreSQL

If you don't have PostgreSQL installed, download and install it from [here](https://www.postgresql.org/download/).

### Create a Database

1. Open a terminal and log in to PostgreSQL:

    ```bash
    psql -U postgres
    ```

2. Create a new database:

    ```sql
    CREATE DATABASE buyback;
    ```

3. Exit PostgreSQL:

    ```sql
    \q
    ```

### Update Django settings for PostgreSQL

In your `settings.py` file, configure the database settings to use PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'buyback',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Make sure to replace `your-username` and `your-password` with your PostgreSQL credentials.

## 3. Creating an Application with Heroku

### Install Heroku CLI

To install the Heroku CLI, follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli).

### Log in to Heroku

After installing the Heroku CLI, log in to Heroku using the following command:

```bash
heroku login
```

### Create a New Heroku Application

Navigate to the project directory and create a new Heroku app:

```bash
heroku create buyback
```

Heroku will generate a unique name for your app. You can also specify a name by passing an argument:

```bash
heroku create your-app-name
```

### Add PostgreSQL Add-on

Heroku provides a free PostgreSQL database with the following command:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

This will create a PostgreSQL database for your app on Heroku.

## 4. Deploying to Heroku

### Install Dependencies

Ensure that your `requirements.txt` is up-to-date with all your project's dependencies. You can generate it using:

```bash
pip freeze > requirements.txt
```

### Add a Procfile

Create a `Procfile` in the root of your project with the following contents:

```
web: gunicorn buyback.wsgi:application
```

This tells Heroku how to run your app using Gunicorn.

### Push to Heroku

Push your changes to Heroku:

```bash
git push heroku master
```

### Migrate the Database

Once your app is deployed, run migrations on Heroku:

```bash
heroku run python manage.py migrate
```

### Open the Application

Open the application in your browser:

```bash
heroku open
```

## 5. Creating a VSCode Workspace

### Create Workspace File

1. Open your project in Visual Studio Code.
2. Go to `File > Add Folder to Workspace...` and add your project folder.
3. Save the workspace by going to `File > Save Workspace As...` and choosing a location to save the `.code-workspace` file.

### Optional: Add Extensions

You can add useful extensions like:

- Python
- Django
- PostgreSQL

Install them from the VSCode extensions marketplace.

## 6. Connecting to Cloudinary for Media Files

### Set Up Cloudinary

1. Sign up for a free account at [Cloudinary](https://cloudinary.com).
2. In the Cloudinary dashboard, find your API credentials (API Key, API Secret, and Cloud Name).

### Install Cloudinary

Install the Cloudinary package:

```bash
pip install cloudinary
```

### Update Django Settings

In your `settings.py`, add the following Cloudinary configurations:

```python
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
  cloud_name="your-cloud-name",
  api_key="your-api-key",
  api_secret="your-api-secret"
)

DEFAULT_FILE_STORAGE = 'cloudinary.storage.MediaCloudinaryStorage'
```

Replace `your-cloud-name`, `your-api-key`, and `your-api-secret` with your actual Cloudinary credentials.

### Update Models for Media Files

Make sure your models use the `CloudinaryField` for media uploads:

```python
from cloudinary.models import CloudinaryField

class YourModel(models.Model):
    media = CloudinaryField('media')
```

### Run Migrations

Run the migrations to apply any changes to the database:

```bash
python manage.py migrate
```

Now your media files will be stored on Cloudinary.
