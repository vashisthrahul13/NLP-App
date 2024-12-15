import tkinter as tk

def adjust_height(event):
    # Calculate the number of lines based on input
    lines = event.widget.get("1.0", "end-1c").count("\n") + 3
    # Set the height of the Text widget based on the number of lines
    event.widget.config(height=lines)

# Create the main window
root = tk.Tk()
root.title("Auto-Adjusting Text Input")

# Create a Text widget
text_box = tk.Text(root, height=3, width=40, wrap="word")  # Initial height is 1 line
text_box.pack(pady=20)

# Bind the <KeyRelease> event to adjust the height dynamically
text_box.bind("<KeyRelease>", adjust_height)

# Run the main loop
root.mainloop()