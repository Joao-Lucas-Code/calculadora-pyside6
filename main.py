import sys 

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow 
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from styles import setupTheme

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define um icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon) # WINDOWS
    app.setWindowIcon(icon) # MAC

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(buttonsGrid)

    # Executa Tudo
    window.adjustFixedSize()
    window.show()
    app.exec()