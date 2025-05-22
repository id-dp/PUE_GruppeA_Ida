from PIL import Image 
# open the json file and load the data
import json
import os

# Example usage
FILE_PATH = 'data\person_db.json'    # Replace with the actual path to your JSON file


def load_user_data(file_path):
    """
    Load user data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: User data loaded from the JSON file.
    """

    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def get_all_names(user_data):
    """
    A function that uses the list of dictionaries to extract all names in the list
    """
    
    user_names = []
    # Loop through the list
    for person_dict in user_data:
        # add first name to user_names
        user_names.append(person_dict["lastname"] + ", " + person_dict["firstname"])
        
    return sorted(user_names)

def get_image(person_name):
    # Laden eines Bilds
    image = Image.open(get_image_path(person_name))
    return image

def get_image_path(current_user):
    """
    current user looks like this: Heyer Yannic
    """
    firstname = current_user.split(", ")[1]
    lastname = current_user.split(", ")[0]

    for person_dict in load_user_data(FILE_PATH):
        if person_dict["firstname"] == firstname and person_dict["lastname"] == lastname:
            path_to_image = person_dict["picture_path"]
            return path_to_image



if __name__ == "__main__":
    user_data = load_user_data('FILE_PATH')
    print(user_data)
    name_list = get_all_names(user_data)
    print(name_list[0])