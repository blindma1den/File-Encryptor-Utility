# File-Encryptor-Utility

This script is a File Encryption Utility that uses the cryptography library in Python to encrypt and decrypt files. It provides an interactive menu for generating encryption keys, encrypting files, and decrypting files. Users can securely protect their sensitive data by using this tool to encrypt files, making them unreadable without the encryption key. It's a simple and effective way to enhance data privacy and security."

Please note that this description assumes the basic functionality and purpose of the script as previously discussed. You can tailor the description further if your script has specific features or capabilities that you'd like to highlight.

You can customize this script according to your needs 


How to install:

Installation:

Python Installation:
Ensure you have Python installed on your system. If not, download and install Python from the official Python website (https://www.python.org/downloads/).
Library Installation:
Open a terminal or command prompt and install the "cryptography" library using pip:
Copy code
pip install cryptography
Usage:

Clone or Download the Script:
Clone this script from the repository or download it to your computer.
Generate Encryption Key:
Open a terminal or command prompt.
Navigate to the directory where the script is located using the cd command.
Run the script using the command:
Copy code
python script.py
Select option "1" to generate an encryption key. The key will be saved in a file called "key.key" in the same directory. You only need to generate a key once.
Encrypt a File:
Run the script again using the same command:
Copy code
python script.py
Choose option "2" to encrypt a file.
Enter the path of the file you want to encrypt when prompted.
The script will use the encryption key generated in step 2 to encrypt the file. The encrypted file will be saved with the prefix "cifrado_" in the same directory as the original file.
Decrypt a File:
To decrypt a previously encrypted file, run the script again:
Copy code
python script.py
Select option "3" and enter the path of the encrypted file you wish to decrypt.
The decrypted file will be saved with the prefix "descifrado_" in the same directory as the encrypted file.

How to use:


Usage Instructions: File Encryption Utility

Generate Encryption Key:
Select option "1" to generate an encryption key. This key will be saved in a file called "key.key" in the script's directory. You only need to generate a key once.
Encrypt a File:
Choose option "2" to encrypt a file. You will be prompted to enter the path of the file you want to encrypt.
The script will use the encryption key generated in step 1 to encrypt the file, and the encrypted file will be saved with the prefix "cifrado_" in the same directory as the original file.
Decrypt a File:
Select option "3" to decrypt a previously encrypted file. You will need the same encryption key generated in step 1.
Enter the path of the encrypted file you wish to decrypt.
The decrypted file will be saved with the prefix "descifrado_" in the same directory as the encrypted file.
Exit:
To exit the program, select option "4."
Notes:

Ensure that you have the "cryptography" library installed in your Python environment before running the script (install with pip install cryptography).
Keep the encryption key ("key.key") safe, as it is required for decrypting files encrypted with this script.
This utility simplifies the process of file encryption and decryption, enhancing data security and privacy.
