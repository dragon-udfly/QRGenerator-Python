# QR Code Generator
### A simple desktop application built with Python for generating QR codes.

## Features
- User-friendly Interface: A graphical user interface (GUI) built with Tkinter.

- Dynamic Generation: Create QR codes from any text or URL you input.

- Real-time Preview: See a live preview of the generated QR code.

- Download Functionality: Save the generated QR code as a high-quality PNG image.

## Prerequisites
####  Before you run the application, you need to have Python installed on your system. 
You also need to install the following Python libraries:

- qrcode: For generating the QR code data.

- Pillow (PIL Fork): For creating and saving the QR code image file.

You can install both libraries using pip with the following command:

```bash
pip install qrcode[pil]
```

**How to Run**

Save the file: Save the provided Python script as qr_generator_app.py.

Open a terminal or command prompt: Navigate to the directory where you saved the file.

Run the script: Execute the script using the Python interpreter.

```bash
python qr_generator_app.py
```

**How to Use**
1. Enter Text: In the text field, type the text, a URL, or any other data you want to encode into the QR code.

3. Generate: Click the "Generate" button. A QR code image will appear in the window below the button.

5. Download: Once the QR code is displayed, the "Download as PNG" button will become active. Click it to choose a location and filename to save your QR code image.

