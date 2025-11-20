# Hardcoded credentials (sensitive)
password = "pa$$w0rd"
api_key = "123456"

def main():
    # Unused variable
    temp = 123

    # Null dereference and bug
    value = None
    if value > 0:  # This will raise TypeError
        print("positive")

    # Duplicate code block
    sum1 = 0
    for i in range(10):
        sum1 += i

    sum2 = 0
    for i in range(10):
        sum2 += i

    # Unreachable code
    return
    print("This line is unreachable")

    # Using eval (security issue)
    user_input = "3*3"
    result = eval(user_input)  # Critical: never use eval with user input
    print("Eval result:", result)

    # Empty except block (bad practice)
    try:
        5 / 0
    except:
        pass

    # Function redefinition
def foo():
    return 5

def foo():
    # Duplicate definition
    return "bad"

    # Bad variable naming, long line, and logic error
    BADCaseVar = 5
    this_is_a_very_long_variable_name_example_that_is_far_too_long_for_pep8_and_should_be_broken_up = "long"

    # Compare with is for string
    x = "fail"
    y = "fail"
    if x is y:
        print("Using is instead of == for string comparison")

if __name__ == "__main__":
    main()
    foo()
