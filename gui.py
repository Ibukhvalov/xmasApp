import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("800x600")

        # Загрузка изображений
        self.load_images()

        # Главное окно с кнопками
        #self.main_frame = tk.Frame(root)
        #self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.first_page()


    def load_images(self):
        """Загрузка и изменение размера изображений."""
        self.back_image = Image.open("back.png")  # Замените на путь к вашему изображению
        self.back_image = self.back_image.resize((50, 30), Image.LANCZOS)
        self.back_photo = ImageTk.PhotoImage(self.back_image)

        self.santa_image = Image.open("santa.png")  # Замените на путь к вашему изображению
        self.santa_image = self.santa_image.resize((500, 500), Image.LANCZOS)
        self.santa_photo = ImageTk.PhotoImage(self.santa_image)

        self.child_image = Image.open("child.png")  # Замените на путь к вашему изображению
        self.child_image = self.child_image.resize((600, 300), Image.LANCZOS)
        self.child_photo = ImageTk.PhotoImage(self.child_image)

        self.newYear_image = Image.open("newYear.png")  # Замените на путь к вашему изображению
        self.newYear_image = self.newYear_image.resize((500, 400), Image.LANCZOS)
        self.newYear_photo = ImageTk.PhotoImage(self.newYear_image)

        self.bag_image = Image.open("bag.png")  # Замените на путь к вашему изображению
        self.bag_image = self.bag_image.resize((110, 110), Image.LANCZOS)
        self.bag_photo = ImageTk.PhotoImage(self.bag_image)

        self.deer_image = Image.open("deer.png")  # Замените на путь к вашему изображению
        self.deer_image = self.deer_image.resize((200, 300), Image.LANCZOS)
        self.deer_photo = ImageTk.PhotoImage(self.deer_image)

    def first_page(self):
        self.clear_frame()

        self.newYear_label = tk.Label(self.root, image=self.newYear_photo)
        self.newYear_label.place(x=150, y=150)

        self.register_button = tk.Button(self.root, text="Зарегистрироваться", command=self.open_registration)
        self.register_button.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Войти", command=self.open_login)
        self.login_button.pack(pady=10)

        self.bag_button = tk.Button(self.root, image=self.bag_photo, command=self.open_login_for_santas, borderwidth=0,
                                    highlightthickness=0, bg=self.root.cget("bg"))
        self.bag_button.place(x=578, y=440)

    def open_registration(self):
        self.clear_frame()

        self.registration_frame = tk.Frame(self.root)
        self.registration_frame.pack(padx=20, pady=20)

        tk.Label(self.registration_frame, text="Логин:").grid(row=0, column=0)
        self.reg_login_entry = tk.Entry(self.registration_frame)
        self.reg_login_entry.grid(row=0, column=1)

        tk.Label(self.registration_frame, text="Пароль:").grid(row=1, column=0)
        self.reg_password_entry = tk.Entry(self.registration_frame, show='*')
        self.reg_password_entry.grid(row=1, column=1)

        tk.Label(self.registration_frame, text="Повторите пароль:").grid(row=2, column=0)
        self.reg_password_confirm_entry = tk.Entry(self.registration_frame, show='*')
        self.reg_password_confirm_entry.grid(row=2, column=1)

        self.register_submit_button = tk.Button(self.registration_frame, text="Зарегистрироваться", command=self.register)
        self.register_submit_button.grid(row=3, columnspan=2, pady=10)

        self.deer_label = tk.Label(self.root, image=self.deer_photo)
        self.deer_label.place(x=570, y=250)

        self.back_button = tk.Button(self.root, image=self.back_photo, command=self.first_page)
        self.back_button.place(relx=0.0, rely=0.0, anchor='nw')

    def open_login(self):
        self.clear_frame()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        tk.Label(self.login_frame, text="Логин:").grid(row=0, column=0)
        self.login_entry = tk.Entry(self.login_frame)
        self.login_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Пароль:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        self.login_submit_button = tk.Button(self.login_frame, text="Войти", command=self.login)
        self.login_submit_button.grid(row=2, columnspan=2, pady=10)

        self.child_label = tk.Label(self.root, image=self.child_photo)
        self.child_label.pack(pady=50)

        self.back_button = tk.Button(self.root, image=self.back_photo, command=self.first_page)
        self.back_button.place(relx=0.0, rely=0.0, anchor='nw')

    def open_login_for_santas(self):
        self.clear_frame()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        tk.Label(self.login_frame, text="Логин:").grid(row=0, column=0)
        self.login_entry = tk.Entry(self.login_frame)
        self.login_entry.grid(row=0, column=1)

        tk.Label(self.login_frame, text="Пароль:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        self.login_submit_button = tk.Button(self.login_frame, text="Войти", command=self.login)
        self.login_submit_button.grid(row=2, columnspan=2, pady=10)

        # Создание метки для отображения изображения
        self.santa_label = tk.Label(self.root, image=self.santa_photo)
        self.santa_label.pack(pady=10)  # Используем pack для метки с изображением

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        login = self.reg_login_entry.get()
        password = self.reg_password_entry.get()
        password_confirm = self.reg_password_confirm_entry.get()

        if password != password_confirm:
            messagebox.showerror("Ошибка", "Пароли не совпадают!")
        else:
            # Здесь можно добавить логику для сохранения данных
            messagebox.showinfo("Успех", "Регистрация успешна!")
            self.open_login()

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        # Здесь можно добавить логику для проверки логина и пароля
        messagebox.showinfo("Успех", "Вы вошли в систему!")
        self.clear_frame()
        self.main_frame.pack(padx=20, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
