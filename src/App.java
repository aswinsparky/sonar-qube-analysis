public class Main {

    // Hardcoded credentials (sensitive)
    private static final String ADMIN_PASSWORD = "root123"; // [Sensitive Data]
    private static final String KEY = "xyzsecretKey"; // [Sensitive Data]

    public static void main(String[] args) {

        // Unused variables
        int unusedInt = 0;
        String unusedString;

        // NullPointerException risk
        String userInput = null;
        if (userInput.equals("something")) {  // Bug: Null check missing
            System.out.println("User input matches!");
        }

        // System.exit in main (bad practice)
        if (args.length > 0 && args[0].equals("exit")) {
            System.exit(1);
        }

        // Use of system.out instead of logger
        System.out.println("Admin password: " + ADMIN_PASSWORD);

        // Redundant conditional branches (code smell)
        int score = 100;
        if (score > 50) {
            System.out.println("Passed!");
        } else {
            System.out.println("Passed!");
        }

        // SQL injection risk
        String username = "baduser";
        String query = "SELECT * FROM accounts WHERE username = '" + username + "' AND password = '" + KEY + "'";
        System.out.println("Query: " + query);

        // Unreachable code
        return;
        // This line can never be reached:
        // System.out.println("Unreachable!");

        // Big block with magic numbers, empty catch
        try {
            int x = 10 / 0; // Always fails
        } catch (Exception ex) {
            // should log or handle: empty catch block
        }
    }
}
