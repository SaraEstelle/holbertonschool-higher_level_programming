def generate_invitations(template, attendees):

    # 1- vérifier les types
    if not isinstance(template, str):
        print("Invalid template type. Expected a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid attendees type. Expected a list. ")
        return

    # Vérifier qye chaque élément est un dictionnaire
    for person in attendees:
        if not isinstance(person, dict):
            print("Invalid attendees type. Expected at list of dictionaries.")
            return

    # 2- vérifier su vide :
    if template.strip() == "":
        print("Template is empty, no output files generated.")

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 3. Boucle sur chaque personne
    index = 1

    for person in attendees :

        # copier le template

        result = template

        # 4- Remplacer les valeurs
        name = person.get("name") or "N/A"
        title = person.get("event_title") or "N/A"
        date = person.get("event_date") or "N/A"
        location = person.get("event_location") or "N/A"

        result = result.replace("{name}", str(name))
        result = result.replace("{event_title}", str(title))
        result = result.replace("{event_date}", str(date))
        result = result.replace("{event_location}", str(location))

        # 5. Créer fichier
        filename = f"output_{index}.txt"

        with open(filename, "w") as f:
            f.write(result)

        index += 1
