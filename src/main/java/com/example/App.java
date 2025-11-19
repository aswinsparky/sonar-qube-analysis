package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class App {
    public static void main(String[] args) {
        // Hardcoded credential (bad practice)
        String password = "P@ssw0rd";
        System.out.println("Using password: " + password);

        // Insecure random usage (predictable seed risk)
        int rand = new java.util.Random().nextInt();
        System.out.println("Random value: " + rand);

        // SQL Injection example (vulnerable)
        String userInput = System.getenv("USER_INPUT");
        if (userInput == null) {
            userInput = "defaultUser";
        }
        String query = "SELECT * FROM users WHERE name = '" + userInput + "'";
        System.out.println("Query: " + query);
        try {
            Connection conn = DriverManager.getConnection("jdbc:h2:mem:");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println(rs.getString(1));
            }
            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Command injection example (vulnerable)
        try {
            String cmd = "sh -c " + userInput;
            Runtime.getRuntime().exec(cmd);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
