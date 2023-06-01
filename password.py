import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox

def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    try:
        length = int(length_entry.get())
    except:
        length = 10
    use_special_chars = special_chars_var.get()
    password = generate_password(length, use_special_chars)
    password_label.config(text="Generated Password:\n" + password)
    copy_button.config(state=tk.NORMAL)  # Включаем кнопку "Copy password"

def copy_button_click():
    password = password_label.cget("text")[19:]  # Получаем сгенерированный пароль из метки
    window.clipboard_clear()  # Очищаем буфер обмена
    window.clipboard_append(password)  # Копируем пароль в буфер обмена
    messagebox.showinfo("Copied", "Password copied to clipboard!")  # Отображаем сообщение о скопированном пароле

def toggle_language():
    global current_language
    if current_language == "ENG":
        current_language = "RU"
        lang_button.config(text="RU")
        length_label.config(text="Длина пароля:")
        generate_button.config(text="Сгенерировать пароль")
        special_chars_checkbox.config(text="Использовать разные символы")
        password_label.config(text="Сгенерированный пароль:\n")
    else:
        current_language = "ENG"
        lang_button.config(text="ENG")
        length_label.config(text="Password Length:")
        generate_button.config(text="Generate Password")
        special_chars_checkbox.config(text="Include Special Characters")
        password_label.config(text="Generated Password:\n")

# Создание главного окна
window = tk.Tk()
window.title("Password Generator")

# Получение размера экрана
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Вычисление координат для размещения окна в центре экрана
window_width = 300
window_height = 160
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Установка положения окна
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Создание виджетов
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window, justify="center")
length_entry.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(window, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_button_click)
generate_button.pack()

password_label = tk.Label(window, text="Generated Password:\n")
password_label.pack()

copy_button = tk.Button(window, text="Copy Password", state=tk.DISABLED, command=copy_button_click)
copy_button.pack()


# Добавление кнопки для переключения языка
current_language = "ENG"  # Изначально установлен английский язык
lang_button = tk.Button(window, text="ENG", command=toggle_language)
lang_button.place(x=10, y=10)  # Установка позиции кнопки в левом верхнем углу

# Запуск главного цикла окна
window.mainloop()
