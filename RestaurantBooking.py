import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
COLOR_BG = "#F5F7FA"     
COLOR_CARD = "#FFFFFF"    
COLOR_ACCENT = "#2D5AFE"   
COLOR_TEXT_MAIN = "#1A1D23" 
COLOR_TEXT_SEC = "#737D8C"  
COLOR_BORDER = "#E1E4E8"   
COLOR_DANGER = "#DC3545"   

class ModernRestaurantApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система бронирования столиков")
        self.geometry("850x650")
        self.configure(bg=COLOR_BG)
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure("TLabel", background=COLOR_BG, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 11))
        self.style.configure("Card.TLabel", background=COLOR_CARD, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 11))
        self.style.configure("Subtitle.TLabel", background=COLOR_CARD, foreground=COLOR_TEXT_SEC, font=("Segoe UI", 10))
        
        self.style.configure("TRadiobutton", background=COLOR_CARD, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 10), focuscolor=COLOR_CARD)
        
        self.current_user = ""
        self.current_role = ""
        self.bookings = [
            {"id": 1, "name": "Иванов Иван", "date": "16.06.2026", "time": "18:00", "guests": "4", "status": "Подтверждено"},
            {"id": 2, "name": "Петров Петр", "date": "16.06.2026", "time": "19:30", "guests": "2", "status": "Ожидает"}
        ]
        
        self.show_login_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
    def show_login_screen(self):
        self.clear_screen()    
        main_title = tk.Label(self, text="Забронировать Столик", bg=COLOR_BG, fg=COLOR_ACCENT, font=("Segoe UI", 26, "bold"))
        main_title.pack(pady=(50, 30))
        login_card = tk.Frame(self, bg=COLOR_CARD, bd=0, relief="flat", padx=40, pady=40)
        login_card.pack(pady=20, expand=True)
        
        card_border = tk.Frame(self, bg=COLOR_BORDER, height=1)
        card_border.pack(fill="x", after=login_card)
        ttk.Label(login_card, text="Вход в систему", style="Card.TLabel", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 5))
        ttk.Label(login_card, text="Введите ваши данные ниже", style="Subtitle.TLabel").pack(anchor="w", pady=(0, 25))
        
        input_frame = tk.Frame(login_card, bg=COLOR_CARD)
        input_frame.pack(fill="x", pady=5)
        ttk.Label(input_frame, text="ФИО Пользователя", style="Card.TLabel").pack(anchor="w")
        self.username_entry = tk.Entry(input_frame, bg="#FFFFFF", fg=COLOR_TEXT_MAIN, insertbackground=COLOR_ACCENT, 
                                       width=40, font=("Segoe UI", 12), bd=1, relief="solid", highlightthickness=0)
        self.username_entry.config(highlightbackground=COLOR_BORDER, highlightcolor=COLOR_ACCENT)
        self.username_entry.insert(0, "")
        self.username_entry.pack(fill="x", ipady=8, pady=(5, 15))
       
        ttk.Label(login_card, text="Ваша Роль", style="Card.TLabel").pack(anchor="w", pady=(10, 5))
        
        self.role_var = tk.StringVar(value="Клиент")
        role_frame = tk.Frame(login_card, bg=COLOR_CARD)
        role_frame.pack(fill="x", pady=5)
        
        ttk.Radiobutton(role_frame, text="Гость", variable=self.role_var, value="Клиент").pack(side="left", padx=(0, 15))
        ttk.Radiobutton(role_frame, text="Администратор", variable=self.role_var, value="Администратор").pack(side="left", padx=15)
        ttk.Radiobutton(role_frame, text="Официант", variable=self.role_var, value="Официант").pack(side="left", padx=15)
        
        btn_frame = tk.Frame(login_card, bg=COLOR_CARD)
        btn_frame.pack(fill="x", pady=(35, 0))
        
        login_btn = tk.Button(btn_frame, text="Войти в систему", bg=COLOR_ACCENT, fg="#FFFFFF", 
                              font=("Segoe UI", 12, "bold"), activebackground="#1A45D9", 
                              activeforeground="#FFFFFF", width=22, bd=0, relief="flat",
                              command=self.handle_login)
        login_btn.pack(side="right")
        
        tk.Label(btn_frame, text="Создать аккаунт", bg=COLOR_CARD, fg=COLOR_ACCENT, 
                 font=("Segoe UI", 10, "underline"), cursor="hand2").pack(side="left", pady=10)

    def handle_login(self):
        self.current_user = self.username_entry.get().strip()
        self.current_role = self.role_var.get()
        
        if not self.current_user:
            messagebox.showwarning("Внимание", "Пожалуйста, введите Ваше имя.")
            return
            
        if self.current_role == "Клиент":
            self.show_client_screen()
        else:
            self.show_admin_screen()

  
    def show_client_screen(self):
        self.clear_screen()
    
        header = tk.Frame(self, bg=COLOR_CARD, bd=0, relief="flat", pady=10)
        header.pack(fill="x")
        tk.Label(header, text=f"Личный кабинет: {self.current_user}", bg=COLOR_CARD, fg=COLOR_TEXT_MAIN, font=("Segoe UI", 12)).pack(side="left", padx=20)
        tk.Button(header, text="Выйти", bg=COLOR_DANGER, fg="#FFFFFF", font=("Segoe UI", 10), bd=0, padx=15, command=self.show_login_screen).pack(side="right", padx=20)
        
   
        tk.Label(self, text="Ваше новое бронирование", bg=COLOR_BG, fg=COLOR_ACCENT, font=("Segoe UI", 20, "bold")).pack(anchor="w", padx=40, pady=30)
        
        content_frame = tk.Frame(self, bg=COLOR_BG)
        content_frame.pack(fill="both", expand=True, padx=40)
        
        form_card = tk.Frame(content_frame, bg=COLOR_CARD, padx=30, pady=30, bd=1, relief="solid", width=400)
        form_card.config(highlightbackground=COLOR_BORDER, highlightthickness=1)

        form_card.pack(side="left", fill="y")
        
        def create_input(parent, label_text, default_val):
            frame = tk.Frame(parent, bg=COLOR_CARD)
            frame.pack(fill="x", pady=10)
            ttk.Label(frame, text=label_text, style="Card.TLabel").pack(anchor="w")
            entry = tk.Entry(frame, bg="#FFFFFF", fg=COLOR_TEXT_MAIN, bd=1, relief="solid", font=("Segoe UI", 11))
            entry.insert(0, default_val)
            entry.pack(fill="x", ipady=5, pady=(5, 0))
            return entry

        date_entry = create_input(form_card, "Дата (ДД.ММ.ГГГГ)", "17.06.2026")
        time_entry = create_input(form_card, "Время", "19:00")
        guests_entry = create_input(form_card, "Количество гостей", "4")
        
        def submit_booking():
            new_id = len(self.bookings) + 1
            new_booking = {
                "id": new_id,
                "name": self.current_user,
                "date": date_entry.get(),
                "time": time_entry.get(),
                "guests": guests_entry.get(),
                "status": "Ожидает"
            }
            self.bookings.append(new_booking)
            messagebox.showinfo("Готово", f"Бронь #{new_id} успешно отправлена и ожидает подтверждения.")
            self.show_client_screen() 
            
        tk.Button(form_card, text="Забронировать столик", bg=COLOR_ACCENT, fg="#FFFFFF", 
                  font=("Segoe UI", 12, "bold"), bd=0, pady=10, command=submit_booking).pack(fill="x", pady=(30, 0))
        list_frame = tk.Frame(content_frame, bg=COLOR_BG, padx=20)
        list_frame.pack(side="left", fill="both", expand=True)
        tk.Label(list_frame, text="Мои активные брони", bg=COLOR_BG, fg=COLOR_TEXT_SEC, font=("Segoe UI", 12)).pack(anchor="w", pady=(0, 10))
        
        for b in self.bookings:
            if b["name"] == self.current_user:
                txt = f"• {b['date']} в {b['time']} ({b['guests']} чел.) — Статус: {b['status']}"
                tk.Label(list_frame, text=txt, bg=COLOR_BG, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 11)).pack(anchor="w", pady=4)

    def show_admin_screen(self):
        self.clear_screen()
        header = tk.Frame(self, bg=COLOR_CARD, bd=0, relief="flat", pady=10)
        header.pack(fill="x")
        tk.Label(header, text=f"Панель Управления ({self.current_role}): {self.current_user}", bg=COLOR_CARD, fg=COLOR_TEXT_MAIN, font=("Segoe UI", 12)).pack(side="left", padx=20)
        tk.Button(header, text="Выйти", bg=COLOR_DANGER, fg="#FFFFFF", font=("Segoe UI", 10), bd=0, padx=15, command=self.show_login_screen).pack(side="right", padx=20)
        tk.Label(self, text="Список всех бронирований", bg=COLOR_BG, fg=COLOR_ACCENT, font=("Segoe UI", 20, "bold")).pack(anchor="w", padx=40, pady=30)
        table_card = tk.Frame(self, bg=COLOR_CARD, padx=20, pady=20, bd=1, relief="solid")
        table_card.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        
        self.style.configure("Treeview", background="#FFFFFF", foreground=COLOR_TEXT_MAIN, rowheight=30, fieldbackground="#FFFFFF", font=("Segoe UI", 10))
        self.style.map("Treeview", background=[('selected', COLOR_ACCENT)], foreground=[('selected', '#FFFFFF')])
        self.style.configure("Treeview.Heading", background=COLOR_BG, foreground=COLOR_TEXT_SEC, font=("Segoe UI", 10, "bold"))
        
        columns = ("id", "name", "date", "time", "guests", "status")
        tree = ttk.Treeview(table_card, columns=columns, show="headings", height=12)
        
        tree.heading("id", text="ID")
        tree.heading("name", text="Клиент")
        tree.heading("date", text="Дата")
        tree.heading("time", text="Время")
        tree.heading("guests", text="Мест")
        tree.heading("status", text="Статус")
        
        tree.column("id", width=40, anchor="center")
        tree.column("name", width=280)
        tree.column("date", width=100, anchor="center")
        tree.column("time", width=80, anchor="center")
        tree.column("guests", width=60, anchor="center")
        tree.column("status", width=120, anchor="center")
        
        for b in self.bookings:
            tree.insert("", "end", values=(b["id"], b["name"], b["date"], b["time"], b["guests"], b["status"]))
            
        tree.pack(fill="both", expand=True)
        
        def approve_booking():
            selected = tree.selection()
            if selected:
                item_values = tree.item(selected, "values")
                booking_id = int(item_values[0])
                for b in self.bookings:
                    if b["id"] == booking_id:
                        b["status"] = "Подтверждено"
                
                tree.set(selected, "status", "Подтверждено")
                messagebox.showinfo("Система", "Бронь успешно подтверждена.")
            else:
                messagebox.showwarning("Внимание", "Выберите бронь из списка.")

        admin_btn_frame = tk.Frame(table_card, bg=COLOR_CARD)
        admin_btn_frame.pack(fill="x", pady=(20, 0))
        
        tk.Button(admin_btn_frame, text="Подтвердить выбранную бронь", bg=COLOR_ACCENT, fg="#FFFFFF", 
                  font=("Segoe UI", 11, "bold"), bd=0, padx=20, pady=8, command=approve_booking).pack(side="right")


if __name__ == "__main__":
    app = ModernRestaurantApp()
    app.mainloop()