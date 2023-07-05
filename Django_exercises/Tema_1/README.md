# Django "Hello World" Tutorial

This tutorial will guide you through the process of creating a "Hello World" view in a Django app. By following these steps, you will learn the basics of creating a view and connecting it to a URL in Django.

## Prerequisites

Before starting, ensure that you have the following:

- **Windows:**
  - [Python installed on your system](https://github.com/Axlfc/python3-course/tree/master#windows-installation)
  - [Django framework installed](https://github.com/Axlfc/python3-course/tree/master/Django_exercises#windows-installation)

- **GNU/Linux (Ubuntu):**
  - Python installed on your system:
    ```shell
    sudo apt update
    sudo apt install python3
    ```
  - Django framework installed:
    ```shell
    sudo apt install python3-django
    ```

- **macOS:**
  - [Python installed on your system](https://github.com/Axlfc/python3-course/tree/master#macos-installation)
  - [Django framework installed](https://github.com/Axlfc/python3-course/tree/master/Django_exercises#macos-installation)

## Steps

1. **Create a new Django project:**

   - **Windows:** Open your command prompt and navigate to the desired location for your project. Run the following command to create a new Django project named `helloworld`:
     ```shell
     django-admin startproject helloworld
     ```

   - **GNU/Linux (Ubuntu) and macOS:** Open your terminal and navigate to the desired location for your project. Run the following command to create a new Django project named `helloworld`:
     ```shell
     django-admin startproject helloworld
     ```

2. **Navigate to the project directory:** Change to the project directory using the following command:

   ```shell
   cd helloworld
   ```

3. **Create a new Django app:** Inside the project directory, create a new Django app named `helloworld` by running the following command:

   ```shell
   python manage.py startapp helloworld
   ```

4. **Create a view:** Open the `helloworld/views.py` file in a text editor and add the following code to define a view function named `greet`:

   ```python
   from django.http import HttpResponse

   def greet(request):
       return HttpResponse("Hello, World!")
   ```
   
Make sure to include the `request` parameter in the greet method to access the incoming request.

5. **Create a URL mapping:** Open the `helloworld/urls.py` file in a text editor and add the following code to map the `greet` view to a URL:

   ```python
   from django.contrib import admin
   from django.urls import path
   from . import views

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('greet/', views.greet, name="greet"),
   ]
   ```

6. **Run the development server:** Start the Django development server using the following command:

   ```shell
   python manage.py runserver
   ```

   You should see output indicating that the server is running.

7. **Access the "Hello World" view:** Open your web browser and visit `http://localhost:8000/greet/`. You should see the text "Hello, World!" displayed in your browser.

Congratulations! You have successfully created a "Hello World" view in your Django app.

## Conclusion

In this tutorial, you learned how to create a simple "Hello World" view in a Django app. This involved creating a view function, mapping it to a URL, and running the development server to access the view in a

 web browser. Feel free to explore Django further and build upon this foundation to create more complex web applications.

For more information and detailed documentation, visit the [Django documentation](https://docs.djangoproject.com/).
