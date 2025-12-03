import os
import subprocess
import sys
import platform
import shutil

def check_pyinstaller():
    """Checks if PyInstaller is installed."""
    try:
        subprocess.run(["pyinstaller", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def build_executable(script_name, console=True):
    """Builds a single executable."""
    print(f"\n[BUILD] Building {script_name}...")
    
    cmd = ["pyinstaller", "--onefile", "--clean"]
    
    if not console:
        cmd.append("--noconsole")
        
    cmd.append(script_name)
    
    try:
        subprocess.run(cmd, check=True)
        print(f"[SUCCESS] Built {script_name}")
        return True
    except subprocess.CalledProcessError:
        print(f"[ERROR] Failed to build {script_name}")
        return False

def main():
    print("="*50)
    print("   Node Modules Cleaner - Build System")
    print("="*50)
    
    # 1. Check Prerequisites
    if not check_pyinstaller():
        print("\n[ERROR] PyInstaller is not installed.")
        print("Please run: pip install pyinstaller")
        input("\nPress Enter to exit...")
        sys.exit(1)
        
    print("\n[INFO] PyInstaller found. Starting build process...")
    
    # 2. Build Console Version
    success_console = build_executable("node_modules_cleaner.py", console=True)
    
    # 3. Build GUI Version
    # Check if GUI script exists
    if os.path.exists("node_modules_cleaner_gui.py"):
        success_gui = build_executable("node_modules_cleaner_gui.py", console=False)
    else:
        print("\n[WARN] GUI script not found, skipping.")
        success_gui = False

    # 4. Summary
    print("\n" + "="*50)
    print("   Build Summary")
    print("="*50)
    
    if success_console:
        print(f"[*] Console App: SUCCESS -> dist/node_modules_cleaner{'.exe' if platform.system() == 'Windows' else ''}")
    else:
        print("[!] Console App: FAILED")
        
    if success_gui:
        print(f"[*] GUI App:     SUCCESS -> dist/node_modules_cleaner_gui{'.exe' if platform.system() == 'Windows' else ''}")
    elif os.path.exists("node_modules_cleaner_gui.py"):
        print("[!] GUI App:     FAILED")
    
    # 5. Copy Artifacts
    print("\n" + "="*50)
    print("   Copy Executables")
    print("="*50)
    print("Where would you like to copy the files?")
    print("1. Downloads")
    print("2. Desktop")
    print("3. Skip")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    dest_dir = None
    home = os.path.expanduser("~")
    
    if choice == '1':
        dest_dir = os.path.join(home, "Downloads")
    elif choice == '2':
        dest_dir = os.path.join(home, "Desktop")
    
    if dest_dir and os.path.exists(dest_dir):
        print(f"\nCopying files to: {dest_dir}")
        count = 0
        
        # Define files to copy
        ext = '.exe' if platform.system() == 'Windows' else ''
        files_to_copy = []
        if success_console:
            files_to_copy.append(f"node_modules_cleaner{ext}")
        if success_gui:
            files_to_copy.append(f"node_modules_cleaner_gui{ext}")
            
        for f_name in files_to_copy:
            src = os.path.join("dist", f_name)
            dst = os.path.join(dest_dir, f_name)
            try:
                shutil.copy2(src, dst)
                print(f"[OK] Copied {f_name}")
                count += 1
            except Exception as e:
                print(f"[ERR] Failed to copy {f_name}: {e}")
                
        if count > 0:
            print(f"\nSuccessfully copied {count} file(s).")
    elif choice != '3':
        print("\n[WARN] Invalid choice or destination directory does not exist.")

    print("\nDone.")
    if platform.system() == 'Windows':
        input("Press Enter to close...")

if __name__ == "__main__":
    main()
