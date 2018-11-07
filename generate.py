import os
import pathlib


def create_sub_dirs(project_name):
    sub_dirs = ["css", "js", "imgs"]
    for sub_dir_name in sub_dirs:
        os.mkdir(project_name + "/" + sub_dir_name)

def generate_files(project_name):
    def create_index_html_file():
        index_file_path = pathlib.PurePath(project_name, "index.html")
        with open(index_file_path, 'w') as index_file:
            index_file.write('<!DOCTYPE html>\n')
            index_file.write('<html>\n')
            index_file.write('\t<head>\n')
            index_file.write('\t\t<title>My Site</title>\n')
            index_file.write('\t\t<link rel="stylesheet" type="text/css" href="styles.css">\n')
            index_file.write('\t</head>\n')
            index_file.write('\t<body>\n')
            index_file.write('\t</body>\n')
            index_file.write('</html>\n')

    def create_css_files():
        css_file_path = pathlib.PurePath(project_name, "css", "styles.css")
        f = open(css_file_path, "w")
        f.close()

    def create_js_file():
        js_file_path = pathlib.PurePath(project_name, "js", "main.js")
        f = open(js_file_path, "w")
        f.close()

    create_index_html_file()
    create_css_files()
    create_js_file()


if __name__ == '__main__':
    project_name = input("Enter name for new project directory: ")
    os.mkdir(project_name)
    create_sub_dirs(project_name)
    generate_files(project_name)
