# This is practice work from Automate the boring stuff with python.
# Reading and Writing Files.
# Mad Libs.
# Main task is to write a program that read text files and lets the user add their own text.
# Programm will replace ADJECTIVE, NOUN, ADVERB, or VERB appears in text file to any that will user write.


def main(path, new_file_path):
    # Open and read text file.
    with open(path, 'r') as text_file:
        text = text_file.read()

    # Replacing ADJECTIVE, NOUN, ADVERB, or VERB appears in text.
    repl_d = {}
    for part_of_speach in ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']:
        if part_of_speach in text:
            for _ in range(text.count(part_of_speach)):
                text = text.replace(part_of_speach, input(f'Enter a {part_of_speach.lower()}\n'), 1)

    print(text)
    # Creating a new .txt file where parts of speach replaced to user words.
    with open(new_file_path, 'w') as new_text_file:
        new_text_file.write(text)


main('text.txt', 'new_text.txt')
                                           
                                           
