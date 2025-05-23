def show_category_content(parent_frame, module_name):
    # Clear previous content
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Import and call appropriate module
    try:
        module = __import__(f'home.categories.{module_name}', fromlist=['show'])
        module.show(parent_frame)
    except Exception as e:
        import tkinter as tk
        tk.Label(parent_frame, text=f"Failed to load {module_name}: {str(e)}", font=("Arial", 14)).pack(pady=20)
