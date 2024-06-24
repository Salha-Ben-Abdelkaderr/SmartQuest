import 'package:flutter/material.dart';
import 'api_service.dart';

class AuthService with ChangeNotifier {
  String? _token;

  String? get token => _token;

  Future<void> login(String email, String password) async {
    var response = await ApiService.login(email, password);
    if (response.containsKey('access_token')) {
      _token = response['access_token'];
      notifyListeners();
    } else {
      // Handle login error
    }
  }

  Future<void> register(
      String name, String firstName, String gender, String email, String password, String dateOfBirth) async {
    var response = await ApiService.register(name, firstName, gender, email, password, dateOfBirth);
    if (response['message'] == 'User registered successfully') {
      // Handle successful registration
    } else {
      // Handle registration error
    }
  }
}
