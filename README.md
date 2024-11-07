# CSV to Excel Converter App

## Features

- **Upload CSV Files**: The app allows users to select and upload a CSV file from their computer.
- **Convert to Excel**: Once a CSV file is uploaded, the app automatically loads and stores the data.
- **Save as Excel**: The user can save the data as an Excel file (.xlsx) on their desktop.
- **Error Handling**: If any errors occur during file reading, conversion, or saving, the app displays a relevant error message.
- **User-Friendly Interface**: The application uses `tkinter` to create a clean and simple interface for users, including clear instructions and feedback messages.

## Code Explanation

### Libraries Used:

- **tkinter**: Used for creating the graphical user interface (GUI), including buttons, message boxes, and file dialogs.
- **pandas**: Used to handle and process CSV and Excel files.
- **os**: Used to determine the desktop path for saving the Excel file.

### Functions:

#### `upload_and_convert()`:
- Opens a file dialog where the user can select a CSV file to upload.
- Reads the CSV file into a pandas DataFrame.
- If the file is successfully read, it stores the DataFrame globally in `converted_df` and enables the "Save Excel File" button.
- If an error occurs during reading, it shows an error message.

#### `save_excel()`:
- Saves the `converted_df` (which holds the uploaded CSV data) as an Excel file on the desktop.
- The saved file is named `output.xlsx`.
- If successful, it displays a success message with the path to the saved file. If there's an issue, it shows an error message.

### GUI Components:

- **Upload Button**: A button labeled "Upload CSV File", which opens a file dialog to select and upload a CSV file.
- **Save Button**: A button labeled "Save Excel File" that is initially disabled and gets enabled after a successful CSV upload. This button allows users to save the data as an Excel file on the desktop.
- **Success and Error Messages**: The app provides feedback through message boxes:
  - Success messages inform the user about successful file conversion and saving.
  - Error messages inform the user if something goes wrong during the process (e.g., invalid file or file-saving issues).

### Window Configuration:

- The main window is created with `Tk()` and is configured with a white background, a window title, and a set window size (600x600).
- The upload button and save button are styled with custom colors (`#4CAF50` for upload and `#2196F3` for save) and font styles (Helvetica, size 12, bold).
- The save button is initially disabled, preventing the user from attempting to save before uploading a CSV file.

### File Handling:

- The uploaded CSV file is read into a pandas DataFrame, which is then stored globally for later use.
- The `save_excel()` function saves the DataFrame as an Excel file on the user's desktop under the filename `output.xlsx`.
### Thank You
