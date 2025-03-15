# 🧮 Let's Calculate  

![Banner](https://raw.githubusercontent.com/amankumawat-567/Let-s-calculate/master/banner.png)  

## 📌 Overview  

**Let's Calculate** is a Python-based **Tkinter GUI application** that provides various mathematical and conversion functions. It is designed to be an easy-to-use tool for quick calculations, conversions, and mathematical operations.  

## ✨ Features  

- 🖥 **Tkinter-Based UI** – A simple, interactive, and responsive GUI using Tkinter.  
- 📊 **Mathematical Functions** – Perform basic and advanced mathematical operations.  
- 🔄 **Converters** – Convert values between different units (angle, temperature, currency, and more).  
- 🔢 **Function Pack** – Predefined set of useful functions.  
- 📜 **History Management** – Keep track of previous calculations.  
- 🎨 **Custom Themes** – Personalize the UI with different themes.  
- 🌐 **Multiple Calculator Modes**:  
  - **Standard Calculator** – Basic arithmetic operations.  
  - **Scientific Calculator** – Advanced mathematical functions.  
  - **Programming Calculator** – Binary, hexadecimal, and logical operations.  
- 🏗 **Modular Architecture** – Well-structured code for better maintainability.  

## 🚀 Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/amankumawat-567/Let-s-calculate.git
   cd Let-s-calculate
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the application:  
   ```bash
   python let's calculate.pyw
   ```  

## 📁 Project Structure  

```
Let-s-calculate/
│-- Convertors/          # Unit conversion functions
│   ├── AngleConvertor.py         # Convert angles (degrees, radians)
│   ├── CurrencyData.py           # Currency conversion data
│   ├── TemperatureConvertor.py   # Convert temperatures (Celsius, Fahrenheit, Kelvin)
│   ├── UnitConvertor.py          # Convert units (area, data, energy, length, weight, power, pressure, speed, time, volume)
│   ├── __init__.py
│
│-- Data/                # Data files (if applicable)
│
│-- FunctionPack/        # Predefined mathematical functions
│
│-- module/              # Core functionalities (credentials, history, theme)
│   ├── GetCredentials.py     # Manages user credentials
│   ├── HistoryManager.py     # Handles calculation history
│   ├── ImageManager.py       # Manages images in the UI
│   ├── ThemeManager.py       # Controls application themes
│   ├── __init__.py
│
│-- Routers/             # Routing logic for different calculators
│   ├── About.py               # About section logic
│   ├── Base.py                # Base class for calculators
│   ├── Convertor.py           # Conversion operations
│   ├── History.py             # History management
│   ├── Pannel.py              # UI panel setup
│   ├── ProgrammingCalculator.py # Programming calculator logic
│   ├── ScientificCalculator.py  # Scientific calculator logic
│   ├── StandardCalculator.py    # Standard calculator logic
│   ├── Theme.py                # Theme configurations
│   ├── __init__.py
│
│-- resources/          # Additional resource files (icons, images, etc.)
│-- ui_setup.py         # Tkinter UI setup script
│-- requirements.txt    # Required dependencies
│-- LICENSE.txt         # License file
│-- README.md           # Project documentation
```

## 📜 License  

This project is licensed under the terms of the MIT License. See [LICENSE](https://github.com/amankumawat-567/Let-s-calculate/blob/master/LICENSE.txt) for details.  

## 💡 Contribution  

Want to improve this project? Feel free to fork and contribute!  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Added new feature"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature-branch
   ```  
5. Open a Pull Request.  

---
