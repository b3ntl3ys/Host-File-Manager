import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton, QInputDialog, QTextEdit


class HostFileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Host File Manager')
        self.setGeometry(200, 200, 400, 300)

        # Create the list widget
        self.list_widget = QListWidget()

        # Create the add button
        self.add_button = QPushButton('Add')

        # Create the remove button
        self.remove_button = QPushButton('Remove')

        # Create the text edit widget
        self.text_edit = QTextEdit()
        self.text_edit.setFixedHeight(25)  # Set the fixed height
        self.text_edit.setMaximumWidth(10000)  # Set the fixed width

        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the button signals to the respective slots
        self.add_button.clicked.connect(self.add_host_entry)
        self.remove_button.clicked.connect(self.remove_host_entry)

        # Load the host file entries
        self.load_host_entries()

    def load_host_entries(self):
        try:
            with open('C:/Windows/System32/drivers/etc/hosts', 'r') as host_file:
                lines = host_file.readlines()

            # Add each line to the list widget
            for line in lines:
                self.list_widget.addItem(line.strip())

        except FileNotFoundError:
            print("Host file not found!")

    def add_host_entry(self):
        # Get the new entry from the text edit widget
        new_entry = self.text_edit.toPlainText().strip()

        if new_entry:
            # Add the new entry to the list widget
            self.list_widget.addItem(new_entry)

            # Append the new entry to the host file
            with open('C:/Windows/System32/drivers/etc/hosts', 'a') as host_file:
                host_file.write(new_entry + '\n')

            # Clear the text edit widget after adding the entry
            self.text_edit.clear()

    def remove_host_entry(self):
        # Get the currently selected item in the list widget
        selected_item = self.list_widget.currentItem()

        if selected_item is not None:
            # Remove the selected item from the list widget
            self.list_widget.takeItem(self.list_widget.row(selected_item))

            # Remove the corresponding entry from the host file
            with open('C:/Windows/System32/drivers/etc/hosts', 'r') as host_file:
                lines = host_file.readlines()

            with open('C:/Windows/System32/drivers/etc/hosts', 'w') as host_file:
                for line in lines:
                    if line.strip() != selected_item.text():
                        host_file.write(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HostFileManager()
    window.show()
    sys.exit(app.exec_())
