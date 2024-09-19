using System;
using System.Text.Json;
using MySql.Data.MySqlClient;
using System.Configuration;  // Dùng để đọc App.config


namespace MariaDBConnector
{
    class Program
    {
        static void Main(string[] uinfo)
        {
            // Kiểm tra nếu số lượng tham số đúng
            if (uinfo.Length != 3)
            {
                var errorResponse = new
                {
                    success = false,
                    message = "Usage: MariaDBConnector <name> <phone_number> <gender>"
                };
                Console.WriteLine(JsonSerializer.Serialize(errorResponse));
                return;
            }
            
            string name = uinfo[0];
            string phone_number = uinfo[1];
            string gender = uinfo[2];

            string host = ConfigurationManager.AppSettings["host"] ?? "FATAL ERROR";
            string user = ConfigurationManager.AppSettings["user"] ?? "FATAL ERROR";
            string password = ConfigurationManager.AppSettings["password"] ?? "FATAL ERROR";
            string database = ConfigurationManager.AppSettings["database"] ?? "FATAL ERROR";
            string port = ConfigurationManager.AppSettings["port"] ?? "FATAL ERROR";

            // Chuỗi kết nối tới MariaDB (thay đổi nếu cần)
            string connectionString = $"server={host};user={user};database={database};port={port};password={password};";

            try
            {
                using (MySqlConnection conn = new MySqlConnection(connectionString))
                {
                    conn.Open();

                    // Truy vấn SQL để thêm dữ liệu vào bảng Users
                    string sql = "INSERT INTO Users (name, phone_number, gender) VALUES (@name, @phone_number, @gender)";
                    using (MySqlCommand cmd = new MySqlCommand(sql, conn))
                    {
                        // Gán giá trị tham số
                        cmd.Parameters.AddWithValue("@name", name);
                        cmd.Parameters.AddWithValue("@phone_number", phone_number);
                        cmd.Parameters.AddWithValue("@gender", gender);

                        // Thực thi truy vấn
                        int rowsAffected = cmd.ExecuteNonQuery();

                        var successResponse = new
                        {
                            success = true,
                            message = $"{rowsAffected} row(s) added."
                        };
                        Console.WriteLine(JsonSerializer.Serialize(successResponse));
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                var errorResponse = new
                {
                    success = false,
                    message = $"Error: {ex.Message}"
                };
                Console.WriteLine(JsonSerializer.Serialize(errorResponse));
            }
        }
    }
}
