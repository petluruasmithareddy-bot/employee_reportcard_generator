#  Password Generator (Python)

A smart and secure password generator built using Python. This project creates strong random passwords using a combination of letters, digits, and special characters.


##  Project Description

This project generates a random password based on user-defined length. It ensures strong password creation by including at least one uppercase letter, one lowercase letter, one digit, and one special character.

It is designed to demonstrate:

* Functions
* Data Structures (List & Dictionary)
* Random module usage
* String handling
* Input validation


##  Features

*  User-defined password length
*  Strong password generation
*  Randomized character selection
*  Input validation (handles invalid inputs)
* Uses list and dictionary data structures

##  Technologies Used

* Python 3
* Built-in modules:

  * `random`
  * `string`


##  How to Use

1. Run the program
2. Enter password length (minimum 4)
3. The program will generate a strong password
4. View the generated password in the terminal

-

##  Sample Output

 Password is generating
Enter password length (min 4): 8

 Generated Password: A3@kLp9!


##  Key Concepts Used

###  Functions

* `generate_password(length)` → Generates password

###  Data Structures

* **List** → Used to store password characters
* **Dictionary** → Used to store password details

###  Modules

* `random.choice()` → Select random characters
* `string.ascii_letters` → Letters
* `string.digits` → Numbers
* `string.punctuation` → Symbols

##  Project Structure

* `generate_password()` → Main logic for password creation
* Input handling → Takes user input
* Validation → Ensures valid length
* Output → Displays generated password

##  Future Improvements

* Add password strength checker
* Add options (only digits / only letters / strong password)
* Save passwords to file
* Build GUI using Tkinter
* Convert into web app using Flask

## Contributing

Feel free to fork this repository and improve the project. Contributions are welcome!


## License

This project is open-source and free to use.

## Acknowledgements

This project is created as part of learning Python, functions, and data structures, helping to build strong programming fundamentals.
