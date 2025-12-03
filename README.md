# Node Modules Cleaner

A powerful, safe, and efficient tool designed to scan your drives or folders and recursively delete `node_modules` directories to free up valuable disk space.

## Features

- **Dual Modes**: 
  - **Console Mode**: Lightweight, text-based interface for quick operations.
  - **GUI Mode**: Modern, user-friendly graphical interface built with PySimpleGUI.
- **Safety First**:
  - **System Drive Protection**: Prevents accidental scanning/deletion of the entire system drive (C: or /).
  - **Dry Run**: Preview exactly what will be deleted before taking action.
  - **Confirmation**: Requires explicit user approval before deleting files.
- **Efficient Scanning**: Smart algorithm skips traversing into `node_modules` to speed up the search process.
- **Logging**: Keeps a detailed record of all deleted paths in `deleted_node_modules.log`.
- **Cross-Platform**: Works seamlessly on Windows, Linux, and macOS.

## Installation

1. **Clone or Download** this repository.
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: `PySimpleGUI` is required for the GUI version. `PyInstaller` is required if you want to build executables.)*

## Usage

### Console Version
Run the script directly in your terminal:
```bash
python node_modules_cleaner.py
```
Follow the on-screen prompts to select a drive or folder.

### GUI Version
Launch the graphical interface:
```bash
python node_modules_cleaner_gui.py
```
1. **Browse** to select your target folder.
2. Click **Scan**.
3. Review the log and click **Delete All** to clean up.

## Building Standalone Executable (.exe)

You can convert this script into a standalone executable that runs without Python installed.

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
2. **Build**:
   - **Windows (Console)**: `pyinstaller --onefile node_modules_cleaner.py`
   - **Windows (GUI)**: `pyinstaller --onefile --noconsole node_modules_cleaner_gui.py`
3. **Locate**: Find your `.exe` file in the `dist/` folder.

---

## Credits & License

**Developer**: Nirod Ranasinghe

**License**: Licensed by **Detz Global Pvt Ltd**  
**Website**: [detzglobal.com](https://detzglobal.com)

&copy; 2025 Detz Global Pvt Ltd. All Rights Reserved.
