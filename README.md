# Let's Calculate
![logo](https://github.com/amankumawat-567/Let-s-calculate/blob/master/banner.png)

## Let's Calculate - A Calculator Application
Let's Calculate is a calculator application created using Python and featuring a backend database for storing user history and conversation parameters. The application includes three modes: Standard, Scientific, and Programming.

## Installation and Setup
1. Clone the repository or download the code files.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Make sure that you have MySQL installed on your system.
4. Update the MySQL credentials if necessary.
5. Launch the calculator by running the `let's calculate.py` file.

## Database
Let's Calculate uses a MySQL database to store calculator history and conversation parameters. The database is automatically created when the user launches the application. The MySQL database can be accessed using the following credentials:

```python
host="localhost",
user="root",
passwd="1234"
```

## Features

### Calculator Modes

#### Standard Calculator
The standard calculator mode includes basic arithmetic operations such as addition, subtraction, multiplication, and division.

#### Scientific Calculator
The scientific calculator mode includes additional operations such as trigonometric functions, logarithmic functions, and exponential functions.

#### Programming Calculator
The programming calculator mode includes conversion between decimal, octal, hexadecimal, and binary. It does not provide bitwise operations such as AND, OR, XOR, and NOT.

### Conversion Utilities

#### Currency Converter
The currency converter mode includes an offline MySQL database that can be updated using the "Update Data" button. The converter uses the latest exchange rates to perform conversions. The base currency is USD. The currency converter also includes a feature to compare up to 5 different currencies using a bar graph.

#### Volume Converter
Converts between different units of volume such as liters, gallons, and milliliters.

#### Length Converter
Converts between different units of length such as kilometers, miles, and meters.

#### Power Converter
Converts between different units of power such as watts, horsepower, and kilowatts.

#### Weight Converter
Converts between different units of weight such as kilograms, pounds, and ounces.

#### Area Converter
Converts between different units of area such as square kilometers, square miles, and hectares.

#### Speed Converter
Converts between different units of speed such as kilometers per hour, miles per hour, and meters per second.

#### Time Converter
Converts between different units of time such as seconds, minutes, and hours.

#### Data Converter
Converts between different units of data such as bytes, kilobytes, and gigabytes.

#### Energy Converter
Converts between different units of energy such as joules, calories, and kilowatt-hours.

#### Pressure Converter
Converts between different units of pressure such as pascals, atmospheres, and pounds per square inch.

#### Angle Converter
Converts between different units of angle such as degrees, radians, and gradians.

### Other Features
* Calculator History: Keeps a history of calculations performed in the calculator.
* Theme Selector: Allows the user to choose from 7 different calculator themes.

## Requirements
To run this project, you need to have the following Python packages installed:
* pillow
* matplotlib
* mysql-connector-python
* requests
* imageio

You can install these packages by running `pip install -r requirements.txt` in the command line after cloning or downloading the project.

Please note that you will also need to have MySQL installed on your system.

## Credits
This project was created as a 12 CBSE Informatics Practices Project by [ME](https://github.com/amankumawat-567). It uses several Python modules including Tkinter, Tkinter.ttk, math, mysql-connector, matplotlib.pyplot, pillow, pathlib, os, requests, and imageio.