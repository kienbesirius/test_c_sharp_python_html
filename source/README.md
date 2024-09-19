# TEST C# PYTHON HTML

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![.NET Version](https://img.shields.io/badge/.NET-8.0-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Project Structure
```
source/
│
├── database/
│   └── MariaDBConnector/          # Main project folder
│       ├── bin/                   # Built folder
│       ├── obj/                   # Build files (automatically generated)
│       ├── MariaDBConnector.csproj # C# project file
│       ├── app.config             # Info server (late)
│       └── Program.cs             # Main entry point of the application
│
├── mysql.data.9.0.0/              # MySQL Data Library (version 9.0.0) https://www.nuget.org/packages/MySql.Data/
│
├── templates/                     # HTML and Python template files
│   └── index.html                 # Example HTML file
│
├── index.py                       # Example Python script
│
└── README.md                      # Project documentation (this file)
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
- 
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
```
pip install Flask
```

### Create new C-Sharp Project
```bash
cd source\database                      
dotnet new console -n MariaDBConnector  
```

### Delete the Project (if needs)
```bash
cd source\database  
Remove-Item -Recurse -Force MariaDBConnector  
``` 

### Add new .cs to Project (if needs)
```bash
cd source\database\MariaDBConnector
New-Item -Path . -Name "NewClass.cs" -ItemType "file"
```

### Delete .cs in Project (if needs)
```bash
cd source\database\MariaDBConnector
del NewClass.cs
```

### Compile project to exe & Run Project (run if needs)
```bash
cd source\database\MariaDBConnector
dotnet build
dotnet run
```

### Add some Library to ensure everything works well. Then check the .csproj (NEEDED)
```bash
cd source\database\MariaDBConnector
dotnet add package MySql.Data
dotnet add package System.Text.Json
dotnet add package System.Configuration.ConfigurationManager
```

### Run the App.py after settings all the things
```bash
cd source
python index.py
```
### Clone the repository
```bash
git clone https://github.com/kienbesirius/test_c_sharp_python_html.git
cd test_c_sharp_python_html
```
