import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QGridLayout, QPushButton, QWidget ,setWindowIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 1. Buat widget utama sebagai container
    main_window = QWidget()
    main_window.setWindowTitle("Aplikasi PySide6")
    main_window.resize(400, 200)

    
    # 2. Buat layout dan pasang ke main_window
    grid = QGridLayout(main_window)

    w = QLabel("This is a placeholder text")
    w.setAlignment(Qt.AlignCenter)
    grid.addWidget(w, 0, 0)
    
    b = QPushButton("Click me")
    grid.addWidget(b, 1, 0)
    
    # 3. Terapkan style (Pastikan file style.qss ada)
    try:
        with open("style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("File style.qss tidak ditemukan.")
        
    main_window.show()
    sys.exit(app.exec())