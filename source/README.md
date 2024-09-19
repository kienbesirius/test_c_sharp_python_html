# TEST C# PYTHON HTML Django App

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![.NET Version](https://img.shields.io/badge/.NET-8.0-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Project Structure
```markdown
source/
│
├── models/                     # Database related files
│   └── MariaDBConnector/          # Main project folder
│       ├── bin/                   # Built folder
│       ├── obj/                   # Build files (automatically generated)
│       ├── MariaDBConnector.csproj # C# project file
│       ├── app.config             # Info server (late)
│       └── Program.cs             # Main entry point of the application
│
├── templates/                    # HTML and Python template files
│   └── index.html                # Example HTML file
│
├── views/                        # Django view files and configurations
│   └── myapp/
│       ├── __init__.py           # Initializer for views module
│       ├── admin.py              
│       ├── apps.py           
│       ├── models.py          
│       ├── tests.py              
│       └── views.py              
│   └── views/
│       ├── __init__.py           # Initializer for views module
│       ├── asgi.py               # ASGI configuration for async support
│       ├── settings.py           # Project settings and configurations
│       ├── urls.py               # URL routing configuration
│       └── wsgi.py               # WSGI configuration for deployment
│   └── manage.py                 # Django management script
│
└── README.md                     # Project documentation (this file)
```
## Features
- 

## Prerequisites
- .NET SDK 8.0 or higher
- Windows
- Python
- MySql
- HTML/CSS

## Getting Started

Please first follow the folder structure in the Overview. 

Then follow powersell cmd below to construct a C# Project rightly!

### Create folder & files follow the structure
```markdown
source/
│
├── models/
│
├── templates/                     # HTML and Python template files
│   └── index.html                 # Example HTML file
│
└── README.md                      # Project documentation (this file)
```
### Create DB
```
-- test MariaDB -- 
CREATE DATABASE test_maria_db;
USE test_maria_db;
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Kiểm tra cấu trúc bảng -- 
DESCRIBE Users;
-- Thêm bản ghi thử nghiệm --
INSERT INTO Users (name, phone_number, gender)
VALUES ('John Doe', '0123456789', 'Male'),
       ('Jane Doe', '0987654321', 'Female');
-- Xem dữ liệu đã thêm -- 
SELECT * FROM Users;
```
### Install Python library
```bash
pip install django
```
### Create Django Project
```bash
cd source
django-admin startproject views
```
### Delete Django Project
```bash
cd source
Remove-Item -Recurse -Force views
```

### 1. Create an app inside the project
```bash
cd source/views
python manage.py startapp myapp
```
### 2. Add myapp into settings.py in source/views/views/settings.py
```bash
INSTALLED_APPS = [
    # Các app khác
    'myapp',
]
```
### 3. Link Django project with index.html in templates
Trước tiên trong mục `source/views/views/`, định nghĩa một URL trong file `urls.py`. Và thêm bên trong `urlpatterns = [...]`
```bash
from myapp import views  # Import views từ app
 # Đường dẫn rỗng ('') đại hiện cho trang chủ bởi vì khi vào web không có đường dẫn phụ nào 
 #     path('admin/', admin.site.urls) bên đây admin thì lại cần truy cập vào đường link cụ thể là admin để hiển thị
 # còn với '' thì không, trực tiếp hiển thị khi truy cập vào webapp
path('', views.index, name='index'),  # Kết nối URL gốc với view index
```
### 4. Create View
trong mục `myapp` tìm file `views.py`, bạn cần tạo một hàm (view function) để render file `index.html`.
```bash
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Render file index.html từ thư mục templates
```
### 5. Ensure in settings.py
Trong file `settings.py`, đảm bảo rằng bạn đã cấu hình đúng đường dẫn đến thư mục chứa `templates`. Django mặc định sẽ tìm kiếm file HTML trong thư mục `templates`, nhưng bạn cần kiểm tra và chỉnh sửa nếu cần.
```bash
import os

# Đường dẫn gốc của project (cho việc tìm templates nằm ngoài thư mục project gốc cụ thể ở đây là bên ngoài thư mục views)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### 6. Migrate & Run
```bash
cd source/views
python manage.py migrate
python manage.py runserver
```
### Create Super user for admin panel
```bash
cd source/views
python manage.py createsuperuser
```

### Create new C-Sharp Project
```bash
cd source\models                      
dotnet new console -n MariaDBConnector  
```

### Delete the Project (if needs)
```bash
cd source\models  
Remove-Item -Recurse -Force MariaDBConnector  
``` 

### Add new .cs to Project (if needs)
```bash
cd source\models\MariaDBConnector
New-Item -Path . -Name "NewClass.cs" -ItemType "file"
```

### Delete .cs in Project (if needs)
```bash
cd source\models\MariaDBConnector
del NewClass.cs
```

### Compile project to exe & Run Project (run if needs)
```bash
cd source\models\MariaDBConnector
dotnet build
dotnet run
```

### Add some Library to ensure everything works well. Then check the .csproj (NEEDED)
```bash
cd source\models\MariaDBConnector
dotnet add package MySql.Data
dotnet add package System.Text.Json
dotnet add package System.Configuration.ConfigurationManager
```
### Create app.config inside MariaDBConnector (NEEDED)
```bash
...
```


### 1. Settings for link  views (Python) to models (C# Proj) (NEEDED)
Bước 1: Cấu hình URL
Trong urls.py
```bash
from django.urls import path
from myapp import views  # Import views từ app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Trang chủ với form HTML
    path('add_user', views.add_user, name='add_user'),  # Đường dẫn để xử lý form
]
```
### 2. Settings for link  views (Python) to models (C# Proj) (NEEDED)
Bước 2: Định nghĩa view xử lý form trong views.py
Trong views.py
```bash
...
```

### 3. Settings for link  views (Python) to models (C# Proj) (NEEDED)
Bước 3: Thêm token `{% csrf_token %}` cho form
Bởi vì Django từ chối một yêu cầu vì lý do bảo mật, thường là do thiếu hoặc cấu hình không đúng các biện pháp bảo vệ như CSRF token (Cross-Site Request Forgery). Django mặc định kích hoạt bảo vệ CSRF, và nếu bạn gửi yêu cầu POST từ một form, bạn cần đảm bảo rằng form đó bao gồm token CSRF để ngăn chặn các cuộc tấn công CSRF
```bash
  <form id="userForm">
    {% csrf_token %}
    <h2>Thông tin người dùng</h2>
    <input type="text" name="name" placeholder="Name" required />
    <input type="text" name="phone_number" placeholder="Phone Number" required />
    <select name="gender">
      <option value="Male">Male</option>
      <option value="Female">Female</option>
    </select>
    <button type="submit">Submit</button>
  </form>
```



### Run the App.py after settings all the things
```bash
cd source/views
python manage.py migrate
python manage.py runserver
```
### Clone the repository
```bash
git clone https://github.com/kienbesirius/test_c_sharp_python_html.git
cd test_c_sharp_python_html
```
