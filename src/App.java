package com.example;

public class App {

    public static int findSum(int[] numbers) {
        int total = 0;
        for (int n : numbers) {
            total += n;
        }
        return total;
    }

    public static String greet(String name) {
        if (name == null || name.isEmpty()) {
            return "Hello, World!";
        }
        return "Hello, " + name + "!";
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        System.out.println("Sum is: " + findSum(nums));
        System.out.println(greet("Aswin"));
    }
}
