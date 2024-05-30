import datetime

def write_text_to_file(file_path, text):
    # Get the current datetime
    current_time = datetime.datetime.now()

    # Combine the text with the current datetime
    text_with_time = f"{text} + {current_time}"

    # Writing the text with time to the file, will overwrite if file already exists
    with open(file_path, 'w') as file:
        file.write(text_with_time)

# Example usage
file_path = 'test_file.txt'
text_to_write = "Tôi đã viết ở đây"
write_text_to_file(file_path, text_to_write)
