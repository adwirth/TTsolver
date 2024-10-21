
# Screen Capture OCR Math Solver

This project is a Python application that captures part of the screen, performs OCR to detect mathematical expressions, evaluates them, and inputs the result automatically.

## Installation Guide

### Prerequisites

Before running the application, make sure you have the following installed:

1. **Python 3.x**: Ensure you have Python installed. You can download it from the official [Python website](https://www.python.org/downloads/).
2. **pip**: This is the package installer for Python and comes pre-installed with Python 3.x. You can verify the installation with:
   ```bash
   pip --version
   ```

### Setting up a Virtual Environment (Recommended)

It's recommended to create a virtual environment to manage the dependencies for this project separately from your global Python installation. To set up a virtual environment:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### Installing Dependencies

Once the virtual environment is active, you can install the required packages for this project.

#### Required Libraries

- `easyocr`: For Optical Character Recognition (OCR).
- `Pillow`: For image manipulation (grayscale, inversion, and blur).
- `sympy`: For evaluating mathematical expressions.
- `pyautogui`: For simulating keyboard input.
- `numpy`: Required by EasyOCR for handling image data.

#### Installation Commands

Run the following command to install all necessary libraries:

```bash
pip install easyocr Pillow sympy pyautogui numpy
```

### Installing Tesseract OCR (Optional)

Although this project uses **EasyOCR** for text recognition, you might also want to install **Tesseract OCR** in case of future extensions or comparisons. You can download and install it by following the instructions for your platform:

- **Windows**: Download the installer from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
- **macOS**: Use `brew` to install it:
  ```bash
  brew install tesseract
  ```
- **Linux**: Install via your package manager:
  ```bash
  sudo apt-get install tesseract-ocr
  ```

### Running the Application

1. After installing the necessary dependencies, you can run the Python script as usual:
   ```bash
   python main.py
   ```

2. Make sure to adjust the screen capture region within the code to match the area you want to monitor.

---

### Contributing

If you want to contribute to this project:

1. Fork the repository.
2. Clone your fork.
3. Create a new branch.
4. Commit your changes and push the branch.
5. Open a pull request.

Feel free to submit issues and feature requests as well!
