import tkinter as tk
import tkinter.messagebox as messagebox
from database import add_note,get_all_notes,update_note,delete_note,search_notes_by_title

current_notes_data = []
selected_note_id = None

def save_note_action():
    global selected_note_id
    title = title_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    
    if title == "" or content == "":
        messagebox.showwarning("Warning", "Both Title and Content are required!")
        return

    # Smart checking: Are we writing a new note or modifying an old one?
    if selected_note_id is None:
        add_note(title, content)
        messagebox.showinfo("Success", "Note created successfully!")
    else:
        update_note(selected_note_id, title, content)
        messagebox.showinfo("Success", "Note updated successfully!")
        selected_note_id = None  # Reset tracking state back to New Note mode
    
    # Clear fields and refresh the visual sidebar list
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    load_notes_list()

def delete_note_action():
    global selected_note_id
    # Check if a note is actually active
    if selected_note_id is None:
        messagebox.showwarning("Warning", "Please select a note from the sidebar to delete!")
        return
        
    # Safety confirmation dialog
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to permanently delete this note?")
    if confirm:
        delete_note(selected_note_id)
        selected_note_id = None  # Reset state
        
        # Clear fields and refresh sidebar
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
        load_notes_list()
        messagebox.showinfo("Deleted", "Note removed successfully!")

def load_notes_list(event=None):
    global current_notes_data
    
    notes_listbox.delete(0, tk.END)

    # Grab whatever text is inside our search bar
    search_term = search_entry.get().strip()
    
    # Conditional Check: If search bar has text, use search query; otherwise, grab everything
    if search_term == "":
        current_notes_data = get_all_notes()
    else:
        current_notes_data = search_notes_by_title(search_term)
    
    # Loop through the notes and insert the title and content into the sidebar
    for note in current_notes_data:
        # Remember: Each note tuple looks like: (id, title, content)
        notes_listbox.insert(tk.END, note[1])

def on_note_select(event):
    global selected_note_id  # Bring the state tracker into this scope
    # 1. Check if an item is actually selected
    selection = notes_listbox.curselection()
    if not selection:
        return
        
    # 2. Get the index number of the visually selected row (0, 1, 2...)
    index = selection[0]
    
    # 3. Retrieve the matching full note tuple from our global map
    selected_note = current_notes_data[index]
    selected_note_id = selected_note[0]
    note_title = selected_note[1]
    note_content = selected_note[2]
    
    # 4. Clear out the right side text input views
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)
    
    # 5. Insert the loaded note details into the text inputs
    title_entry.insert(0, note_title)
    content_text.insert("1.0", note_content)

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

# Search Entry Box
search_label = tk.Label(sidebar, text="Search by Title:", font=("Helvetica", 10), bg="#f0f0f0")
search_label.pack(anchor=tk.W, padx=10, pady=(5, 0))

search_entry = tk.Entry(sidebar, font=("Helvetica", 11), bd=1, relief=tk.SOLID)
search_entry.pack(fill=tk.X, padx=10, pady=(0, 5))

# Bind the real-time key release event directly to our loading function!
search_entry.bind("<KeyRelease>", load_notes_list)

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
save_button = tk.Button(main_content, text="Save Note", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5,command=save_note_action)
save_button.pack(side=tk.BOTTOM, anchor=tk.E, padx=20, pady=20)

# 4. Delete Button 
delete_button = tk.Button(main_content, text="Delete Note", font=("Helvetica", 12, "bold"), bg="#f44336", fg="white", bd=0, padx=10, pady=5, command=delete_note_action)
delete_button.pack(side=tk.BOTTOM, anchor=tk.E, padx=20, pady=5)


# 5. Note Content Text Box (Packed LAST - fills the leftover middle space)
content_text = tk.Text(main_content, font=("Helvetica", 12), wrap=tk.WORD, bd=1, relief=tk.SOLID)
content_text.pack(expand=True, fill=tk.BOTH, padx=20, pady=5)


load_notes_list()
notes_listbox.bind("<<ListboxSelect>>", on_note_select)


root.mainloop()