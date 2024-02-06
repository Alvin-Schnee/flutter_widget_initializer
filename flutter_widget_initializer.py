import os
import tkinter as tk
from tkinter import filedialog

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def submit():
    folder_path = folder_entry.get()
    file_name = file_entry.get()

    target_folder = os.path.join(folder_path, 'lib', file_name)
    os.makedirs(target_folder)

    # Create the three files
    file_name = file_name.lower()
    capitalizedName = file_name.capitalize()
    files = [f"{file_name}.dart", f"{file_name}_controller.dart", f"{file_name}_bindings.dart"]
    
    contents = {
        f"{file_name}.dart": f"""\
// {file_name}_widget.dart
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '{file_name}_controller.dart';

class {capitalizedName}Widget extends StatelessWidget
{{
\t{capitalizedName}Widget({{super.key}});\n
\tfinal controller = {capitalizedName}Controller();\n
\t@override
\tWidget build(BuildContext context) {{
\t\treturn Scaffold
\t\t(
\t\t\tappBar: AppBar(title: const Text('{capitalizedName} Widget')),
\t\t\tbody: Center
\t\t\t(
\t\t\t\tchild: Column
\t\t\t\t(
\t\t\t\t\tmainAxisAlignment: MainAxisAlignment.center,
\t\t\t\t\tchildren:
\t\t\t\t\t[
\t\t\t\t\t\tObx(() => Text('Count : ${{controller.count}}')),
\t\t\t\t\t\tElevatedButton(
\t\t\t\t\t\t\tonPressed: () => controller.increment(),
\t\t\t\t\t\t\tchild: const Text('Increment count'),
\t\t\t\t\t\t),
\t\t\t\t\t],
\t\t\t  ),
\t\t\t),
\t\t);
\t}}
}}
""",
        

        f"{file_name}_controller.dart": f"""\
// {file_name}_controller.dart\n
import 'package:get/get.dart';\n
class {capitalizedName}Controller extends GetxController
{{
\tRxInt count = 0.obs;\n	
\tvoid increment()
\t{{
\t\tcount++;
\t}}
}}
""",

        f"{file_name}_bindings.dart": f"""\
// {file_name}_bindings.dart
import 'package:get/get.dart';
import '{file_name}_controller.dart';

class {capitalizedName}Bindings implements Bindings {{
\t@override
\tvoid dependencies() {{
\t\tGet.lazyPut<{capitalizedName}Controller>(() => {capitalizedName}Controller());
\t}}
}}
""",
    }

    for file_name in files:
        file_path = os.path.join(target_folder, file_name)
        with open(file_path, 'w') as file:
            # Write the content to the files
            file.write(contents[file_name])
        print(f"File created: {file_path}")

# Create the main window
window = tk.Tk()
window.title("Folder and File Input")
window.geometry("565x100")

# Folder input
folder_label = tk.Label(window, text="Select your project's folder :")
folder_label.grid(row=0, column=0, padx=10, pady=10)

folder_entry = tk.Entry(window, width=50)
folder_entry.grid(row=0, column=1, padx=5, pady=10)

folder_button = tk.Button(window, text="Browse", command=browse_folder)
folder_button.grid(row=0, column=2, padx=10, pady=10)

# File input
file_label = tk.Label(window, text="Enter your widget's name :")
file_label.grid(row=1, column=0, padx=10, pady=10)

file_entry = tk.Entry(window, width=50)
file_entry.grid(row=1, column=1, padx=5, pady=10)

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=1, column=2, pady=10)

# Output label
output_label = tk.Label(window, text="")
output_label.grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
window.mainloop()
