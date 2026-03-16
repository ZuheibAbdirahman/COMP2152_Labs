import platform
import sys
import os

def display_header(title):
    """Display a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def display_dict(data, title):
    """Display a dictionary with nice formatting."""
    print(f"\n--- {title} ---")
    for key, value in data.items():
        print(f"  {key:12}: {value}")
def get_system_info():
    """
    Return a dictionary with system information using the platform module.
    Keys: "os", "node", "release", "machine"
    """
    pass

def get_python_info():
    """
    Return a dictionary with Python information using the sys module.
    Keys: "version", "executable", "platform"
    """
    pass
def get_directory_info(path):
    """
    Return a dictionary with directory information using the os module.
    Keys: "path", "exists", "file_count", "is_directory"
    """

    pass

def main():
    display_header("SYSTEM INFORMATION REPORTER")
    system_info = get_system_info()
    display_dict(system_info, "System Info")
    python_info = get_python_info()
    display_dict(python_info, "Python Info")
    dir_info = get_directory_info(".")
    display_dict(dir_info, "Directory Info for '.'")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()