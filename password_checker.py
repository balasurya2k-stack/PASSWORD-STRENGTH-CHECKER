import tkinter as tk
import re

def check_password():
    password = password_entry.get()

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    result_label.config(text=f"Password Strength: {strength}")

    suggestion_text.delete("1.0", tk.END)

    if suggestions:
        suggestion_text.insert(tk.END, "Suggestions:\n\n")
        for item in suggestions:
            suggestion_text.insert(tk.END, f"• {item}\n")
    else:
        suggestion_text.insert(tk.END, "Excellent! Your password is strong.")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("550x450")

title = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

password_label = tk.Label(
    root,
    text="Enter Password:",
    font=("Arial", 12)
)
password_label.pack()

password_entry = tk.Entry(
    root,
    show="*",
    width=30,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

check_button = tk.Button(
    root,
    text="Check Password",
    font=("Arial", 12),
    command=check_password
)
check_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=10)

suggestion_text = tk.Text(
    root,
    height=10,
    width=50
)
suggestion_text.pack(pady=10)

root.mainloop()
