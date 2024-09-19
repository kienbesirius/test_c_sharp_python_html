from django.shortcuts import render
import json
import subprocess
from django.http import JsonResponse
from pathlib import Path
import os

# Đường dẫn đến file .exe
BASE_DIR = Path(__file__).resolve().parent.parent.parent
subpath = os.path.join(BASE_DIR, 'models')
exe_path = os.path.join(subpath, 'MariaDBConnector', 'bin', 'Debug', 'net8.0', 'MariaDBConnector.exe')

# Định nghĩa hàm gọi chương trình C#
def call_csharp(name, phone_number, gender):
    try:
        # Chạy file .exe với các tham số
        process = subprocess.run([exe_path, name, phone_number, gender], capture_output=True, text=True)
        print(process)
        # Kiểm tra nếu chương trình chạy thành công
        if process.returncode == 0:
            # Parse JSON từ output của C#
            result = json.loads(process.stdout)
            return result
        else:
            return {"success": False, "message": process.stderr}

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return {"success": False, "message": str(e)}


def add_user(request):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')

        # Gọi hàm để chạy chương trình C# và nhận kết quả
        response = call_csharp(name, phone_number, gender)
    
        # Trả về mã trạng thái HTTP dựa trên thành công hay thất bại
        if response['success']:
          return JsonResponse(response,status = 200)  # HTTP 200 OK
        else:
            print(f"Error from C#: {response['message']}")
            return JsonResponse(response,status = 500)   # HTTP 500 Internal Server Error
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status = 400) # HTTP 400 Bad Request

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Render file index.html từ thư mục templates
