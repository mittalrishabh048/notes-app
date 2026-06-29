import tkinter as tk

# Set up the main window
root = tk.Tk()
root.title("Notes App")
root.geometry("800x600")

# ==========================================
# 1. LEFT SIDEBAR FRAME (Navigation)
# ==========================================
sidebar = tk.Frame(root, width=250, bg="#f0f0f0", bd=1, relief=tk.SOLID)
sidebar.pack(side=tk.LEFT, fill=tk.Y)
sidebar.pack_propagate(False)  # Prevents the frame from shrinking to fit its contents

# Sidebar Title
sidebar_label = tk.Label(sidebar, text="My Notes", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
sidebar_label.pack(pady=10)

# Listbox to display note titles
notes_listbox = tk.Listbox(sidebar, font=("Helvetica", 12))
notes_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


# ==========================================
# 2. RIGHT MAIN FRAME (Editing Area)
# ==========================================
main_content = tk.Frame(root, bg="white")
main_content.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# 1. Title Label & Entry (Packed first)
title_label = tk.Label(main_content, text="Title:", font=("Helvetica", 12, "bold"), bg="white")
title_label.pack(anchor=tk.W, padx=20, pady=(20, 5))

title_entry = tk.Entry(main_content, font=("Helvetica", 14), bd=1, relief=tk.SOLID)
title_entry.pack(fill=tk.X, padx=20, pady=5)

# 2. Content Label (Packed next)
content_label = tk.Label(main_content, text="Content:", font=("Helvetica", 12, "bold"), bg="white")
content_label.pack(anchor=tk.W, padx=20, pady=(10, 5))

# 3. Save Button (Pack this BEFORE the big Text widget)
save_button = tk.Button(main_content, text="Save Note", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
save_button.pack(side=tk.BOTTOM, anchor=tk.E, padx=20, pady=20)

# 4. Note Content Text Box (Packed LAST - fills the leftover middle space)
content_text = tk.Text(main_content, font=("Helvetica", 12), wrap=tk.WORD, bd=1, relief=tk.SOLID)
content_text.pack(expand=True, fill=tk.BOTH, padx=20, pady=5)


# Start the main loop
root.mainloop()