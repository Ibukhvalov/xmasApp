import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("800x600")

        # Главное окно с кнопками
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.pack(padx=20, pady=20)

        self.santa_image = Image.open("santa.png")  # Замените на путь к вашему изображению
        self.santa_image = self.santa_image.resize((500, 500), Image.LANCZOS)  # Изменение размера изображения
        self.santa_photo = ImageTk.PhotoImage(self.santa_image)

        # Вставка изображения колпака
        self.santaHat_image = Image.open("santaHat.png")  # Замените на путь к вашему изображению
        self.santaHat_image = self.santaHat_image.resize((30, 30), Image.LANCZOS)  # Изменение размера изображения
        self.santaHat_photo = ImageTk.PhotoImage(self.santaHat_image)
        self.santaHat_button = tk.Button(self.main_frame, image=self.santaHat_photo, command=self.open_login_for_santas)
        self.santaHat_button.place(relx=1.0, rely=1.0, anchor='se')

        self.register_button = tk.Button(self.main_frame, text="Зарегистрироваться", command=self.open_registration)
        self.register_button.pack(pady=10)

        self.login_button = tk.Button(self.main_frame, text="Войти", command=self.open_login)
        self.login_button.pack(pady=10)

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

        self.register_submit_button = tk.Button(self.registration_frame, text="Зарегистрироваться",
                                                command=self.register)
        self.register_submit_button.grid(row=3, columnspan=2, pady=10)

        tk.Label(self.registration_frame, text="Уже есть аккаунт?").grid(row=5, column=0)
        tk.Label(self.registration_frame, text="Тогда:").grid(row=6, column=0)
        self.register_login_button = tk.Button(self.registration_frame, text="Войти",
                                                command=self.open_login)
        self.register_login_button.grid(row=6, columnspan=2, pady=10)

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
