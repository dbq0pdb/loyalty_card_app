import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
 
 
class SupermarketRegistrationApp(tk.Tk):
    def __init__(self):
        super().__init__()
 
        self.title("Supermarket Registration App")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")
 
        self.links = [
            {
                "name": "Asda",
                "cost": "Free",
                "card_required": "No",
                "app_required": "Yes",
                "points": "Yes",
                "discounts": "Yes",
                "url": "https://groceries.asda.com/event/asda-rewards"
            },
            {
                "name": "Co-op",
                "cost": "£1",
                "card_required": "Yes",
                "app_required": "Yes",
                "points": "Yes",
                "discounts": "Yes",
                "url": "https://membership.coop.co.uk/register"
            },
            {
                "name": "Iceland",
                "cost": "Free",
                "card_required": "Yes",
                "app_required": "Yes",
                "points": "Yes",
                "discounts": "Yes",
                "url": "https://www.iceland.co.uk/login?original=https%3A%2F%2Fwww.iceland.co.uk%2Faccount%2Fbonus-card"
            },
            {
                "name": "Lidl Plus",
                "cost": "Free",
                "card_required": "No",
                "app_required": "Yes",
                "points": "No",
                "discounts": "Yes",
                "url": "https://www.lidl.ie/lidl-plus/app-download#LPQRCODE"
            },
            {
                "name": "Marks & Spencer",
                "cost": "Free",
                "card_required": "No",
                "app_required": "Yes",
                "points": "No",
                "discounts": "Yes",
                "url": "https://www.marksandspencer.com/joinsparks"
            },
            {
                "name": "Morrisons",
                "cost": "Free",
                "card_required": "Yes",
                "app_required": "Yes",
                "points": "Yes",
                "discounts": "Yes",
                "url": "https://more.morrisons.com/register"
            },
            {
                "name": "Sainsbury's",
                "cost": "Free",
                "card_required": "Yes",
                "app_required": "Yes",
                "points": "Yes",
                "discounts": "Yes",
                "url": "https://www.nectar.com/id/start/nectar-card-check"
            },
            {
                "name": "Tesco",
                "cost": "Free",
                "card_required": "Yes",
                "app_required": "Yes",
                "points": "Yes",
                "discounts": "Yes",
                "url": "https://www.tesco.com/account/register/en-GB"
            },
            {
                "name": "Waitrose",
                "cost": "Free",
                "card_required": "Yes",
                "app_required": "Yes",
                "points": "No",
                "discounts": "Yes",
                "url": "https://www.waitrose.com/ecom/login?redirect=%2Fecom%2Flogin%3Fredirect%3D%252Fecom%252Fmy-waitrose%252Fjoin"
            }
        ]
 
        self.selected_links = []
 
        self.create_widgets()
 
    def create_widgets(self):
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(pady=10)
 
        self.title_label = tk.Label(frame, text="Supermarket Registration Links", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack()
 
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#ffffff", foreground="#000000", rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
 
        self.link_table = ttk.Treeview(frame, columns=["Name", "Cost", "Card Required", "App Required", "Points", "Discounts"],
                                       show="headings", selectmode="browse", style="Treeview")
        self.link_table.pack(pady=10)
 
        self.link_table.heading("Name", text="Name")
        self.link_table.heading("Cost", text="Cost")
        self.link_table.heading("Card Required", text="Card Required")
        self.link_table.heading("App Required", text="App Required")
        self.link_table.heading("Points", text="Points")
        self.link_table.heading("Discounts", text="Discounts")
 
        self.link_table.column("Name", width=200, anchor=tk.CENTER)
        self.link_table.column("Cost", width=80, anchor=tk.CENTER)
        self.link_table.column("Card Required", width=120, anchor=tk.CENTER)
        self.link_table.column("App Required", width=120, anchor=tk.CENTER)
        self.link_table.column("Points", width=80, anchor=tk.CENTER)
        self.link_table.column("Discounts", width=80, anchor=tk.CENTER)
 
        for link in self.links:
            self.link_table.insert("", tk.END, values=(
                link["name"], link["cost"], link["card_required"], link["app_required"], link["points"], link["discounts"]))
 
        self.open_links_button = tk.Button(frame, text="Open Selected Links", command=self.open_links,
                                           font=("Arial", 12), bg="#e1e1e1", fg="#000000", padx=10, pady=5)
        self.open_links_button.pack(pady=10)
 
        self.select_all_button = tk.Button(frame, text="Select All", command=self.select_all,
                                           font=("Arial", 12), bg="#e1e1e1", fg="#000000", padx=10, pady=5)
        self.select_all_button.pack()
 
        self.export_button = tk.Button(frame, text="Export Links", command=self.export_links,
                                       font=("Arial", 12), bg="#e1e1e1", fg="#000000", padx=10, pady=5)
        self.export_button.pack()
 
        self.clear_button = tk.Button(frame, text="Clear Selection", command=self.clear_selection,
                                      font=("Arial", 12), bg="#e1e1e1", fg="#000000", padx=10, pady=5)
        self.clear_button.pack()
 
        self.link_table.bind("<<TreeviewSelect>>", self.on_table_select)
 
    def open_links(self):
        if not self.selected_links:
            messagebox.showinfo("No Link Selected", "Please select at least one link.")
            return
 
        for link in self.selected_links:
            webbrowser.open_new_tab(link)
 
        messagebox.showinfo("Links Opened", "Selected links have been opened in your default browser.")
 
    def select_all(self):
        self.link_table.selection_set(self.link_table.get_children())
        self.selected_links = [link["url"] for link in self.links]
 
    def export_links(self):
        if not self.selected_links:
            messagebox.showinfo("No Link Selected", "Please select at least one link.")
            return
 
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "w") as file:
                for link in self.selected_links:
                    file.write(link + "\n")
 
            messagebox.showinfo("Links Exported", "Selected links have been exported successfully.")
        else:
            messagebox.showinfo("Export Cancelled", "Export operation has been cancelled.")
 
    def clear_selection(self):
        self.link_table.selection_remove(self.link_table.get_children())
        self.selected_links = []
 
    def on_table_select(self, event):
        selected_rows = self.link_table.selection()
        self.selected_links = [self.links[int(row[1:])]["url"] for row in selected_rows]
 
if __name__ == "__main__":
    app = SupermarketRegistrationApp()
    app.mainloop()
 
