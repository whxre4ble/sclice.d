# Caesar Cipher Tool

A feature-rich command-line tool for encrypting and decrypting messages using the Caesar cipher algorithm. This implementation includes enhanced UI/UX features, file handling capabilities, and additional functionality like brute force decryption.

## How It Works

### Caesar Cipher Algorithm

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet.

For example, with a shift of 3:
- 'A' becomes 'D'
- 'B' becomes 'E'
- 'C' becomes 'F'
- ...and so on

#### Encryption Process
1. Each letter in the input text is processed individually
2. For each letter:
   - If it's an uppercase letter (A-Z):
     * Convert to number (A=0, B=1, ..., Z=25)
     * Add the shift value
     * Take modulo 26 (to wrap around the alphabet)
     * Convert back to letter
   - If it's a lowercase letter (a-z):
     * Same process as uppercase, but stays lowercase
   - If it's not a letter (spaces, punctuation):
     * Leave unchanged
3. The shifted letters are combined to form the encrypted text

Example with shift = 3:
```
Plain:    HELLO WORLD!
Shifted:  KHOOR ZRUOG!
```

#### Decryption Process
Decryption is simply the reverse of encryption:
1. Take the encrypted text
2. Use a negative shift value (or 26 minus the original shift)
3. Apply the same algorithm

Example:
```
Encrypted: KHOOR ZRUOG!
Shift: -3 (or 23)
Decrypted: HELLO WORLD!
```

## Features

- 🔒 **Message Encryption**: Encrypt any text message using a custom shift value
- 📂 **File Encryption**: Encrypt entire files while preserving formatting
- 🔓 **Message Decryption**: Decrypt encrypted messages with the correct shift value
- 🔨 **Brute Force Decryption**: Try all possible shift values to crack encrypted messages
- 💾 **File Handling**: Save results to files and read from files
- 🎨 **Enhanced UI**: Beautiful command-line interface with loading animations
- ⚠️ **Error Handling**: Robust error handling for all operations
- 🔄 **Multiple Operations**: Perform multiple operations in one session

## Requirements

- Python 3.6 or higher

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. No additional dependencies required!

## Usage

Run the script using Python:

```bash
python caesar_cipher.py
```

### Menu Options

1. **Encrypt a message**: Directly encrypt a text message
   - Enter your message
   - Specify a shift value (integer)
   - Option to save result to file

2. **Encrypt a file**: Encrypt contents of a file
   - Specify input file path
   - Enter shift value
   - Choose output file location

3. **Decrypt a message**: Decrypt an encrypted message
   - Enter encrypted message or load from file
   - Specify the shift value used for encryption
   - Option to save result to file

4. **Brute force decrypt**: Try all possible shift values
   - Enter encrypted message
   - View all 26 possible decryptions
   - Helps when shift value is unknown

5. **Exit**: Close the program

### Examples

#### Encrypting a Message
```
Enter the message to encrypt: Hello, World!
Enter the shift value (an integer): 3
Encrypted result:
──────────────────────────────────────────────────────
Khoor, Zruog!
──────────────────────────────────────────────────────
```

#### Decrypting a Message
```
Enter the message to decrypt: Khoor, Zruog!
Enter the shift value (an integer): 3
Decrypted result:
──────────────────────────────────────────────────────
Hello, World!
──────────────────────────────────────────────────────
```

#### Brute Force Decryption
```
Enter the text to brute force decrypt: Khoor
Brute Force Results:
════════════════════════════════════════════════════════════════
Shift  0: Khoor
Shift  1: Jgnnq
Shift  2: Ifmmp
Shift  3: Hello  <- Likely the correct decryption
Shift  4: Gdkkn
...
════════════════════════════════════════════════════════════════
```

## Features Explained

### Message Encryption/Decryption
- Preserves case (uppercase/lowercase)
- Maintains non-alphabetic characters unchanged
- Supports any integer shift value (automatically normalized to 0-25)

### File Operations
- UTF-8 encoding support
- Error handling for file operations
- Option to save results to files

### Brute Force Decryption
- Displays all 26 possible decryptions
- Helpful when the shift value is unknown
- Makes it easy to identify the correct decryption

### User Interface
- Clear, intuitive menu system
- Loading animations for longer operations
- Error messages for invalid inputs
- Clean, formatted output

## Error Handling

The tool handles various error cases:
- Invalid shift values
- File not found
- Permission errors
- Invalid menu selections
- Keyboard interrupts

## Tips

1. When encrypting sensitive information, use different shift values for different messages
2. For file encryption, ensure you have proper read/write permissions
3. When using brute force decryption, look for readable words to identify the correct shift
4. Save important results to files for future reference

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). This means:

- ✅ You can view, use, and modify the code
- ✅ You can distribute the code and modified versions
- ✅ You must keep the same license for derivative works
- ✅ You must make the source code available
- ❌ You cannot use this code in proprietary (closed source) software
- ❌ You cannot sublicense the code under different terms

For more details, see the [LICENSE](LICENSE) file in the repository.
