from flask import Flask,render_template, request, jsonify
import json
import subprocess

# from YourNamespace import YourClass
app = Flask(__name__)

# Defines Functions
# Định nghĩa hàm gọi chương trình C#
def call_csharp(name, phone_number, gender):
    try:
         # Đường dẫn đến file .exe
        exe_path = r'database/MariaDBConnector/bin/Debug/net8.0/MariaDBConnector.exe'
        
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
        return {"success": False, "message": str(e)}

# Defines Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
     # Lấy dữ liệu từ request
    name = request.form['name']
    phone_number = request.form['phone_number']
    gender = request.form['gender']
    
    # Gọi hàm để chạy chương trình C# và nhận kết quả
    response = call_csharp(name, phone_number, gender)
    
      # Trả về mã trạng thái HTTP dựa trên thành công hay thất bại
    if response['success']:
        return jsonify(response), 200  # HTTP 200 OK
    else:
        return jsonify(response), 500  # HTTP 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
