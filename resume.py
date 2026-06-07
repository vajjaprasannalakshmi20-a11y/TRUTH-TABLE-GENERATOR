import tkinter as tk
from tkinter import messagebox, filedialog

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Resume Builder Pro")
root.geometry("650x750")
root.config(bg="white")

# ---------------- FUNCTIONS ----------------

def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_text.get("1.0", tk.END)
    education = edu_text.get("1.0", tk.END)
    skills = skills_text.get("1.0", tk.END)
    experience = exp_text.get("1.0", tk.END)

    if name == "" or email == "":
        messagebox.showwarning("Error", "Name and Email are required!")
        return

    global resume_data

    resume_data = f"""
================ RESUME ================
Name: {name}
Email: {email}
Phone: {phone}
Address: {address}

----------- EDUCATION -----------
{education}

------------- SKILLS -------------
{skills}

----------- EXPERIENCE -----------
{experience}
======================================
"""

    preview_box.delete("1.0", tk.END)
    preview_box.insert(tk.END, resume_data)


def save_resume():
    if preview_box.get("1.0", tk.END).strip() == "":
        messagebox.showwarning("Error", "Generate resume first!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(preview_box.get("1.0", tk.END))
        messagebox.showinfo("Success", "Resume saved successfully!")


# ---------------- UI DESIGN ----------------

title = tk.Label(root, text="💼 Resume Builder Pro",
                 font=("Arial", 20, "bold"), bg="white")
title.pack(pady=10)

# NAME
tk.Label(root, text="Name", bg="white").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

# EMAIL
tk.Label(root, text="Email", bg="white").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

# PHONE
tk.Label(root, text="Phone", bg="white").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

# ADDRESS
tk.Label(root, text="Address", bg="white").pack()
address_text = tk.Text(root, height=2, width=50)
address_text.pack()

# EDUCATION
tk.Label(root, text="Education", bg="white").pack()
edu_text = tk.Text(root, height=3, width=50)
edu_text.pack()

# SKILLS
tk.Label(root, text="Skills", bg="white").pack()
skills_text = tk.Text(root, height=3, width=50)
skills_text.pack()

# EXPERIENCE
tk.Label(root, text="Experience", bg="white").pack()
exp_text = tk.Text(root, height=3, width=50)
exp_text.pack()

# BUTTONS
btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate Resume",
          bg="green", fg="white", command=generate_resume).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Save Resume",
          bg="blue", fg="white", command=save_resume).grid(row=0, column=1, padx=5)

# PREVIEW BOX
tk.Label(root, text="Preview", bg="white").pack()

preview_box = tk.Text(root, height=15, width=70)
preview_box.pack()

# RUN APP
root.mainloop()