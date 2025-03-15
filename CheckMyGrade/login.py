import csv
import os
import hashlib

LOGIN_FILE = "data\\login.csv"

class LoginUser:
    def __init__(self):
        self.shift = 3  # Example shift value for Caesar cipher

    def encrypt_password(self, password):
        """Encrypts password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, hashed_password, input_password):
        """Verifies if the input password matches the stored hashed password"""
        return hashed_password == self.encrypt_password(input_password)

    def caesar_cipher_encrypt(self, text):
        """Encrypts text using Caesar cipher with the given shift"""
        result = ""
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                result += chr((ord(char) + self.shift - shift_amount) % 26 + shift_amount)
            else:
                result += char
        return result

    def caesar_cipher_decrypt(self, text):
        """Decrypts text using Caesar cipher with the given shift"""
        return self.caesar_cipher_encrypt(text, -self.shift)

    def register(self, email, password, role):
        """Registers a new user with an encrypted password"""
        encrypted_password = self.encrypt_password(password)

        # Ensure file exists before appending
        if not os.path.exists(LOGIN_FILE):
            with open(LOGIN_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Email", "Password", "Role"])  # Header row

        with open(LOGIN_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email, encrypted_password, role])

        print("✅ User registered successfully!")

    def login(self, email, password):
        """Authenticates a user by verifying email and password"""
        if not os.path.exists(LOGIN_FILE):
            print("❌ No users found! Please register first.")
            return None

        with open(LOGIN_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) == 3 and row[0] == email and self.verify_password(row[1], password):
                    print(f"✅ Login successful! Welcome, {email}. Role: {row[2]}")
                    return row[2]  # Return the role of the user
        
        print("❌ Invalid credentials!")
        return None

    def logout(self):
        """Logs out the user (for session-based authentication)"""
        print("👋 You have been logged out successfully.")

    def change_password(self, email, old_password, new_password):
        """Allows a user to change their password after verifying the old one"""
        if not os.path.exists(LOGIN_FILE):
            print("❌ No users found! Please register first.")
            return False

        users = []
        password_changed = False

        with open(LOGIN_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            users = list(reader)

        for i, row in enumerate(users):
            if len(row) == 3 and row[0] == email and self.verify_password(row[1], old_password):
                users[i][1] = self.encrypt_password(new_password)
                password_changed = True
                break

        if password_changed:
            with open(LOGIN_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(users)
            print("🔒 Password changed successfully!")
            return True
        else:
            print("❌ Incorrect old password!")
            return False
