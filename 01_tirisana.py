from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
MODEL_COLUMNS = ["species", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]


def clean_penguins(raw_data):
    # Atlasām sugu un četrus mērījumus, jo sugu prognozēsim pēc putna ķermeņa uzbūves.
    selected = raw_data[MODEL_COLUMNS]
    # Izmetam rindas ar trūkstošu sugu vai mērījumu, jo katram piemēram vajag gan atbildi, gan visus četrus mērījumus.
    return selected.dropna()


def main():
    # Lasot avota CSV, apzīmējumu NA uztveram kā trūkstošu vērtību, jo tā atzīmēti nezināmie mērījumi.
    raw_data = pd.read_csv(PROJECT_DIR / "dati" / "penguins.csv", na_values="NA")
    clean_data = clean_penguins(raw_data)
    # Saglabājam atlasītos datus atsevišķā failā bez pandas rindas numura, jo tas nav pingvīna mērījums.
    clean_data.to_csv(PROJECT_DIR / "tirs.csv", index=False)

    print(f"Rindas sākumā: {len(raw_data)}")
    print(f"Izmestas rindas ar trūkstošu sugu vai mērījumu: {len(raw_data) - len(clean_data)}")
    print(f"Rindas beigās: {len(clean_data)}")


if __name__ == "__main__":
    main()
