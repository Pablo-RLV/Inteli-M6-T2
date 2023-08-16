import os
import sqlite3
from PIL import Image

# Connect to the database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS imagens (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, imagem BLOB)')

# Path to the images folder
folder = 'output'

# Loop through the images folder
for archive in os.listdir(folder):
    # Open the image and convert it to binary
    with Image.open(os.path.join(folder, archive)) as imagem:
        dados_binarios = imagem.tobytes()
    
    # Insert the image into the database
    cursor.execute('INSERT INTO imagens (nome, imagem) VALUES (?, ?)', (archive, sqlite3.Binary(dados_binarios)))

# Save the changes
connection.commit()

# Close the connection
connection.close()