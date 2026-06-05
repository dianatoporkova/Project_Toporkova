import tkinter as tk
from tkinter import ttk, messagebox

def submit():
    messagebox.showinfo("Сообщение", "Готово")

def clear():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("")
    music_var.set(0)
    video_var.set(0)
    draw_var.set(0)
    combo_country.set("")
    combo_city.set("")
    text_about.delete("1.0", tk.END)
    entry_result.delete(0, tk.END)

root = tk.Tk()
root.title("Форма регистрации пользователя")
root.geometry("650x600")

tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 16)).pack(pady=10)

main_frame = tk.Frame(root, bd=2, relief="solid", padx=15, pady=15)
main_frame.pack(padx=20, pady=10, fill="both", expand=True)

for i in range(10):
    main_frame.rowconfigure(i, pad=8)
main_frame.columnconfigure(1, weight=1)

label_width = 18

tk.Label(main_frame, text="Ваше имя:", width=label_width, anchor="w").grid(row=0, column=0)
entry_name = tk.Entry(main_frame)
entry_name.grid(row=0, column=1, sticky="ew")

tk.Label(main_frame, text="Пароль:", width=label_width, anchor="w").grid(row=1, column=0)
entry_password = tk.Entry(main_frame, show="*")
entry_password.grid(row=1, column=1, sticky="ew")

tk.Label(main_frame, text="Возраст:", width=label_width, anchor="w").grid(row=2, column=0)
entry_age = tk.Entry(main_frame)
entry_age.grid(row=2, column=1, sticky="ew")

tk.Label(main_frame, text="Пол:", width=label_width, anchor="w").grid(row=3, column=0)
gender_var = tk.StringVar()
frame_gender = tk.Frame(main_frame)
frame_gender.grid(row=3, column=1, sticky="w")

tk.Radiobutton(frame_gender, text="Мужской", variable=gender_var, value="Мужской").pack(side="left", padx=10)
tk.Radiobutton(frame_gender, text="Женский", variable=gender_var, value="Женский").pack(side="left", padx=10)

tk.Label(main_frame, text="Ваши увлечения:", width=label_width, anchor="w").grid(row=4, column=0)
frame_hobby = tk.Frame(main_frame)
frame_hobby.grid(row=4, column=1, sticky="w")

music_var = tk.IntVar()
video_var = tk.IntVar()
draw_var = tk.IntVar()

tk.Checkbutton(frame_hobby, text="Музыка", variable=music_var).pack(side="left", padx=10)
tk.Checkbutton(frame_hobby, text="Видео", variable=video_var).pack(side="left", padx=10)
tk.Checkbutton(frame_hobby, text="Рисование", variable=draw_var).pack(side="left", padx=10)

countries = [
    "Россия", "Казахстан", "Беларусь", "Украина", "Германия", "Франция",
    "Италия", "Испания", "США", "Канада", "Китай", "Япония",
    "Индия", "Бразилия", "Турция", "ОАЭ", "Австралия"
]

tk.Label(main_frame, text="Ваша страна:", width=label_width, anchor="w").grid(row=5, column=0)
combo_country = ttk.Combobox(main_frame, values=countries)
combo_country.grid(row=5, column=1, sticky="ew")

cities = [
    "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
    "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону",
    "Уфа", "Красноярск", "Воронеж", "Пермь", "Волгоград"
]

tk.Label(main_frame, text="Ваш город:", width=label_width, anchor="w").grid(row=6, column=0)
combo_city = ttk.Combobox(main_frame, values=cities)
combo_city.grid(row=6, column=1, sticky="ew")

tk.Label(main_frame, text="Кратко о себе:", width=label_width, anchor="nw").grid(row=7, column=0)

text_about = tk.Text(main_frame, height=4, fg="gray")
text_about.grid(row=7, column=1, sticky="ew")

placeholder = "Краткая информация о ваших увлечениях"

def add_placeholder():
    text_about.insert("1.0", placeholder)
    text_about.config(fg="gray")

def remove_placeholder(event):
    if text_about.get("1.0", "end-1c") == placeholder:
        text_about.delete("1.0", tk.END)
        text_about.config(fg="black")

def restore_placeholder(event):
    if text_about.get("1.0", "end-1c") == "":
        add_placeholder()

text_about.bind("<FocusIn>", remove_placeholder)
text_about.bind("<FocusOut>", restore_placeholder)

add_placeholder()

tk.Label(
    main_frame,
    text="Решите пример, запишите результат в поле ниже:",
    anchor="w"
).grid(row=8, column=0, columnspan=2, sticky="w")

entry_result = tk.Entry(main_frame)
entry_result.grid(row=9, column=1, sticky="w")

frame_buttons = tk.Frame(main_frame)
frame_buttons.grid(row=10, column=1, sticky="e", pady=10)

tk.Button(frame_buttons, text="Отменить ввод", command=clear).pack(side="left", padx=5)
tk.Button(frame_buttons, text="Данные подтверждаю", command=submit).pack(side="left")

root.mainloop()