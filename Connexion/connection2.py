import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QVBoxLayout, QScrollArea
)
import oracledb as db

class DatabaseConnectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Connexion à la base Oracle et affichage des données")
        self.resize(600, 400)

        # Layout principal
        self.main_layout = QVBoxLayout(self)

        # Formulaire pour les informations de connexion
        self.form_layout = QGridLayout()
        self.form_layout.addWidget(QLabel("Nom d'utilisateur:"), 0, 0)
        self.username_input = QLineEdit()
        self.form_layout.addWidget(self.username_input, 0, 1)

        self.form_layout.addWidget(QLabel("Mot de passe:"), 1, 0)
        self.password_input = QLineEdit()

        self.form_layout.addWidget(self.password_input, 1, 1)

        self.form_layout.addWidget(QLabel("Hôte:"), 2, 0)
        self.host_input = QLineEdit("localhost")
        self.form_layout.addWidget(self.host_input, 2, 1)

        self.form_layout.addWidget(QLabel("Port:"), 3, 0)
        self.port_input = QLineEdit("1521")
        self.form_layout.addWidget(self.port_input, 3, 1)

        self.form_layout.addWidget(QLabel("Nom du service:"), 4, 0)
        self.service_name_input = QLineEdit("freepdb1")
        self.form_layout.addWidget(self.service_name_input, 4, 1)

        # Bouton de connexion
        self.connect_button = QPushButton("Se connecter")
        self.connect_button.clicked.connect(self.connect_to_database)
        self.form_layout.addWidget(self.connect_button, 5, 0, 1, 2)

        # Ajouter le formulaire au layout principal
        self.main_layout.addLayout(self.form_layout)

        # Scroll area pour afficher les résultats
        self.scroll_area = QScrollArea()
        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QGridLayout()
        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)

        self.setLayout(self.main_layout)

    def connect_to_database(self):
        # Récupérer les valeurs saisies
        username = self.username_input.text()
        password = self.password_input.text()
        host = self.host_input.text()
        port = self.port_input.text()
        service_name = self.service_name_input.text()

        try:
            # Création du DSN et connexion
            dsn = db.makedsn(host, port, service_name=service_name)
            connection = db.connect(user=username, password=password, dsn=dsn)

            # Exécuter une requête (remplacez par une table existante)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM hr.employees FETCH FIRST 10 ROWS ONLY")  # Exemple avec hr.employees
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Noms des colonnes

            # Afficher les données dans le QGridLayout
            self.display_data(columns, data)

            # Fermer la connexion
            cursor.close()
            connection.close()
        except db.DatabaseError as e:
            error, = e.args
            QMessageBox.critical(self, "Erreur", f"Erreur de connexion : {error}")

    def display_data(self, columns, data):
        # Effacer les données précédentes
        for i in reversed(range(self.scroll_area_layout.count())):
            widget = self.scroll_area_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Afficher les noms des colonnes
        for col_index, col_name in enumerate(columns):
            self.scroll_area_layout.addWidget(QLabel(f"<b>{col_name}</b>"), 0, col_index)

        # Afficher les lignes
        for row_index, row in enumerate(data, start=1):
            for col_index, cell in enumerate(row):
                self.scroll_area_layout.addWidget(QLabel(str(cell)), row_index, col_index)

# Application principale
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseConnectionApp()
    window.show()
    sys.exit(app.exec())
