# main.py
import customtkinter as ctk
import customtkinter.CTkEntry as CTkEntry
import customtkinter.CTkLabel as CTkLabel

def main():
    ctk.set_appearance_mode("dark")  # opsi: "light", "dark", "system"
    root = ctk.CTk()
    root.title("Demo CustomTkinter")

    entry = CTkEntry(root, placeholder_text="Masukkan nama")
    entry.pack(padx=20, pady=20)

    label = CTkLabel(root, text="Selamat datang!")
    label.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()

# echo "# apk-android-python" >> README.md 
# git init 
# git add README.md 
# git commit -m "first commit" 
# git branch -M main 
# git remote add origin https://github.com/NexdyMC/apk-android-python.git
#  git push -u origin main