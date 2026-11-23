from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


PROJECT_DIR = Path(__file__).resolve().parent
RANDOM_SEED = 42


def print_first_error(test_features, test_species, predictions):
    for (index, actual), predicted in zip(test_species.items(), predictions):
        if actual != predicted:
            # Indekss sākas ar 0, bet CSV pirmajā rindā ir kolonnu nosaukumi.
            print(f"\nKļūdas piemērs no tirs.csv, faila rinda {index + 2}")
            print(test_features.loc[index].to_string())
            print(f"Patiesā suga: {actual} | Prognoze: {predicted}")
            return
    print("Visas testa sugas prognozētas pareizi.")


def main():
    data = pd.read_csv(PROJECT_DIR / "tirs.csv")
    species = data["species"]
    features = data.drop(columns="species")

    train_features, test_features, train_species, test_species = train_test_split(
        features, species, test_size=0.2, stratify=species, random_state=RANDOM_SEED
    )
    model = DecisionTreeClassifier(max_depth=3, random_state=RANDOM_SEED)
    model.fit(train_features, train_species)
    predictions = model.predict(test_features)

    # Bāzes līnija katram testa pingvīnam izvēlas biežāko sugu treniņa datos.
    most_common_species = train_species.value_counts().idxmax()
    baseline_predictions = [most_common_species] * len(test_species)
    baseline_accuracy = accuracy_score(test_species, baseline_predictions)
    model_accuracy = accuracy_score(test_species, predictions)

    print(f"Treniņa rindas: {len(train_species)} | Testa rindas: {len(test_species)}")
    print(f"Modelis: {model_accuracy:.2%} | Bāzes līnija ({most_common_species}): {baseline_accuracy:.2%}")

    importance = pd.Series(model.feature_importances_, index=features.columns)
    print("Divas svarīgākās kolonnas:")
    for name, score in importance.nlargest(2).items():
        print(f"  {name}: {score:.1%}")

    print_first_error(test_features, test_species, predictions)


if __name__ == "__main__":
    main()
