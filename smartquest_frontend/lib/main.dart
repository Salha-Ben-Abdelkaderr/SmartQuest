import 'package:flutter/material.dart';
import 'package:smartquest_frontend/pages/signup_page.dart';

void main() {
  runApp(SmartQuestApp());
}

class SmartQuestApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SmartQuest',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: RegisterScreen(),
      routes: {
        '/signup': (context) => RegisterScreen(),
      },
    );
  }
}
