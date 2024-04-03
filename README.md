## ✨ COMO USARLO E INSTALARLO

> Clonar el repositorio en cualquier carpeta

```bash
$ git clone https://github.com/claseacademy/bolsistamv.git
$ cd bolsistamv
```

<br />

### 👉 INSTALACION PARA CUALQUIER SISTEMA OPERATIVO `Unix`, `MacOS`, `Windows`

> Instalar modulos via `VENV` o entorno virtual

```bash
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> Activar e instalar la Base de Datos del sistema

```bash
$ Activar BD mysql
$ Crear BD
$ Importar BD ubicada y con nombre db/djngo.sql
```

<br />

> Inicializar el sistema

```bash
$ python manage.py runserver
```

Enlace web local del sistema `http://127.0.0.1:8000/`.


<br />

> USUARIOS

# ADMINISTRADOR

  USERNAME:  admin
  PASSWORD:  admin123

# USUARIO DE PRUEBAS

  USERNAME:  usuario
  PASSWORD:  adm12345


<br />

## ✨ ESTRUCTURA DEL PROYECTO

El proyecto está codificado utilizando una estructura simple e intuitiva que se presenta a continuación:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```
