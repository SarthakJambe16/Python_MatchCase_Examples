# 1
grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Invalid grade")


# 2
a = 10
b = 5
op = "+"

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")


# 3
signal = "red"

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")


# 4
command = "delete"
match command:
    case "add" | "create":
        print("Adding new entry...")
    case "delete" | "remove":
        print("Deleting entry...")
    case "edit" | "update":
        print("Editing entry...")
    case "list" | "show":
        print("Listing all entries...")
    case _:
        print("Unknown command")


# 5
status = 404
match status:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case 403 | 405 | 409:
        print("Error")
    case _:
        print(f"Unknown status {status}")


# 6
fruit = "apple"

match fruit:
    case "apple":
        print("Red fruit")
    case "banana":
        print("Yellow fruit")
    case "orange":
        print("Orange fruit")
    case _:
        print("Unknown fruit")

# 7
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")


# 8 
status = "success"

match status:
    case "success":
        print("Login successful")
    case "failed":
        print("Login failed")
    case "locked":
        print("Account locked")
    case _:
        print("Unknown status")


# 9
vehicle = "bike"

match vehicle:
    case "car":
        print("Four wheels")
    case "bike":
        print("Two wheels")
    case "bus":
        print("Public transport")
    case _:
        print("Unknown vehicle")


# 10
greeting = "hello"

match greeting:
    case "hello":
        print("Hi!")
    case "bye":
        print("Goodbye!")
    case "thanks":
        print("Welcome!")
    case _:
        print("Unknown message")
