     if dataset["comment"].iloc[i] != "": 
            if dataset["rating"].iloc[i] == 1 : 
                Palabras_Positivas.append(dataset["comment"].iloc[i])
            if dataset["rating"].iloc[i] == 0: 
                Palabras_Negativas.append(dataset["comment"].iloc[i])