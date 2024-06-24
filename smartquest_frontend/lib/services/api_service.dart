import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://localhost:8000'; // Replace with your backend URL

  static Future<Map<String, dynamic>> login(String email, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/token'),
      headers: <String, String>{
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: <String, String>{
        'username': email,
        'password': password,
      },
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      return {
        'error': 'Failed to login',
        'message': response.body,
      };
    }
  }

  static Future<Map<String, dynamic>> register(String name, String firstName, String gender, String email, String password, String dateOfBirth) async {
    final response = await http.post(
      Uri.parse('$baseUrl/register/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'name': name,
        'first_name': firstName,
        'gender': gender,
        'email': email,
        'password': password,
        'date_of_birth': dateOfBirth,
      }),
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      return {
        'error': 'Failed to register',
        'message': response.body,
      };
    }
  }

  static Future<Map<String, dynamic>> getUser(String token) async {
    final response = await http.get(
      Uri.parse('$baseUrl/users/me/'),
      headers: <String, String>{
        'Authorization': 'Bearer $token',
      },
    );

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      return {
        'error': 'Failed to get user',
        'message': response.body,
      };
    }
  }
}
