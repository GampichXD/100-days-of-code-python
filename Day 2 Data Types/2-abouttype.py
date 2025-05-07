len("Hello")

# Check Data Type
print(type("Hello"));
print(type(123));
print(type(3.14));
print(type(True));

# Convert Data Type
print(str(123));
print(int("123"));
print(float("3.14"));
print(bool("True"));
print(int("123")+456);
print("123"+str(456));
# print("123"+int("456")); # Error

name_of_user = input("Enter your name: ");
length_of_name = len(name_of_user);
print("Number of Characters in your name:", length_of_name);
print("Number of Characters in 'Hello':", len(input("Enter a word: ")));