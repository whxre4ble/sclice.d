#!/usr/bin/env python3

import os
import sys
import time
from typing import Union, Tuple

def print_banner():
    """Display a stylized welcome banner."""
    banner = """
╔══════════════════════════════════════════════════════════╗
║                   Caesar Cipher Tool                     ║
║           Encrypt and Decrypt Your Messages              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def print_loading(message: str):
    """Display a loading animation with a message."""
    for _ in range(3):
        for char in "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏":
            print(f"\r{message} {char}", end="", flush=True)
            time.sleep(0.1)
    print("\r" + " " * (len(message) + 2))  # Clear the loading animation

def validate_shift_value(shift: str) -> Tuple[bool, Union[int, str]]:
    """
    Validate the shift value input.
    
    Args:
        shift (str): The shift value to validate
        
    Returns:
        Tuple[bool, Union[int, str]]: (success, result)
            - If successful: (True, int_value)
            - If failed: (False, error_message)
    """
    try:
        value = int(shift)
        # Normalize the shift value to be within 0-25
        return True, value % 26
    except ValueError:
        return False, "Error: Shift value must be an integer."

def caesar_encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using the Caesar cipher algorithm.
    
    Args:
        text (str): The text to encrypt
        shift (int): The shift value (0-25)
        
    Returns:
        str: The encrypted text
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case and base ASCII value
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Apply the shift
            shifted = (ord(char) - ascii_base + shift) % 26
            result += chr(ascii_base + shifted)
        else:
            result += char
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    """
    Decrypt text using the Caesar cipher algorithm.
    
    Args:
        text (str): The text to decrypt
        shift (int): The shift value (0-25)
        
    Returns:
        str: The decrypted text
    """
    return caesar_encrypt(text, -shift)

def save_to_file(content: str, filename: str) -> Tuple[bool, str]:
    """
    Save content to a file.
    
    Args:
        content (str): The content to save
        filename (str): The target filename
        
    Returns:
        Tuple[bool, str]: (success, message)
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, f"Content successfully saved to {filename}"
    except Exception as e:
        return False, f"Error saving to file: {str(e)}"

def read_from_file(filename: str) -> Tuple[bool, str]:
    """
    Read content from a file.
    
    Args:
        filename (str): The file to read from
        
    Returns:
        Tuple[bool, str]: (success, content/error_message)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return True, f.read()
    except FileNotFoundError:
        return False, f"Error: File '{filename}' not found."
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def get_shift_value() -> int:
    """
    Get and validate the shift value from user input.
    
    Returns:
        int: The validated shift value
    """
    while True:
        shift = input("\nEnter the shift value (an integer): ")
        success, result = validate_shift_value(shift)
        if success:
            return result
        print(result)  # Print error message if validation failed

def handle_encryption(is_file: bool = False):
    """Handle the encryption workflow."""
    if is_file:
        filename = input("\nEnter the path to the file to encrypt: ")
        success, content = read_from_file(filename)
        if not success:
            print(content)
            return
        
        print(f"\nFile contents loaded from: {filename}")
    else:
        content = input("\nEnter the message to encrypt: ")
    
    shift = get_shift_value()
    print_loading("Encrypting")
    encrypted = caesar_encrypt(content, shift)
    
    print("\nEncrypted result:")
    print("─" * 50)
    print(encrypted)
    print("─" * 50)
    
    save = input("\nWould you like to save the result to a file? (y/n): ").lower()
    if save == 'y':
        filename = input("Enter the filename to save to: ")
        success, message = save_to_file(encrypted, filename)
        print(message)

def handle_decryption():
    """Handle the decryption workflow."""
    # Ask if input is from file
    from_file = input("\nWould you like to decrypt from a file? (y/n): ").lower()
    
    if from_file == 'y':
        filename = input("\nEnter the path to the file to decrypt: ")
        success, content = read_from_file(filename)
        if not success:
            print(content)
            return
    else:
        content = input("\nEnter the message to decrypt: ")
    
    shift = get_shift_value()
    print_loading("Decrypting")
    decrypted = caesar_decrypt(content, shift)
    
    print("\nDecrypted result:")
    print("─" * 50)
    print(decrypted)
    print("─" * 50)
    
    save = input("\nWould you like to save the result to a file? (y/n): ").lower()
    if save == 'y':
        filename = input("Enter the filename to save to: ")
        success, message = save_to_file(decrypted, filename)
        print(message)

def brute_force_decrypt(text: str):
    """
    Attempt to decrypt text using all possible shift values.
    
    Args:
        text (str): The text to decrypt
    """
    print("\nBrute Force Results:")
    print("═" * 60)
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2d}: {decrypted}")
    print("═" * 60)

def main():
    """Main program flow."""
    print_banner()
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Encrypt a file")
        print("3. Decrypt a message")
        print("4. Brute force decrypt")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            handle_encryption()
        elif choice == '2':
            handle_encryption(is_file=True)
        elif choice == '3':
            handle_decryption()
        elif choice == '4':
            text = input("\nEnter the text to brute force decrypt: ")
            print_loading("Analyzing all possible shifts")
            brute_force_decrypt(text)
        elif choice == '5':
            print("\nThank you for using the Caesar Cipher Tool!")
            sys.exit(0)
        else:
            print("\nError: Invalid choice. Please enter a number between 1 and 5.")
        
        # Ask if user wants to perform another operation
        if input("\nWould you like to perform another operation? (y/n): ").lower() != 'y':
            print("\nThank you for using the Caesar Cipher Tool!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
        sys.exit(0)
