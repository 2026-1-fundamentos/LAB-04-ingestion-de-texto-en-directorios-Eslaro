# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
   
    import os
    import zipfile

    import pandas as pd

    # Raíz del repositorio: un nivel arriba de homework/
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_zip = os.path.join(root, "files", "input.zip")
    extract_dir = os.path.join(root, "files")
    output_dir = os.path.join(root, "files", "output")

    # Descomprimir el archivo zip de entrada
    with zipfile.ZipFile(input_zip, "r") as z:
        z.extractall(extract_dir)

    # Crear la carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    def build_dataset(split):
        """Construye un DataFrame a partir de los archivos de texto de un split."""
        records = []
        base_path = os.path.join(extract_dir, "input", split)
        for sentiment in ["positive", "negative", "neutral"]:
            folder = os.path.join(base_path, sentiment)
            if not os.path.isdir(folder):
                continue
            for filename in os.listdir(folder):
                if filename.endswith(".txt"):
                    filepath = os.path.join(folder, filename)
                    with open(filepath, "r", encoding="utf-8") as f:
                        phrase = f.read().strip()
                    records.append({"phrase": phrase, "target": sentiment})
        return pd.DataFrame(records, columns=["phrase", "target"])

    # Generar y guardar train_dataset.csv
    train_df = build_dataset("train")
    train_df.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)

    # Generar y guardar test_dataset.csv
    test_df = build_dataset("test")
    test_df.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)
