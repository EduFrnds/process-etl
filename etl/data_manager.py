import csv
import logging
import os


class DataManager:
    def __init__(self, file_path):
        self.file_path = '../data'
        self.path = file_path

    def save_to_csv(self, data, filename, headers):
        """Save data to CSV file"""
        file_path = f"{self.path}/{filename}.csv"
        with open(file_path, 'wt', newline='', encoding='utf-8') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def delete_files(directory_path):
        """Delete all files in the specified directory."""
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            logging.info('Todos os arquivos foram excluídos do diretório.')
        except Exception as e:
            logging.error(f"Erro ao excluir arquivos: {e}")
