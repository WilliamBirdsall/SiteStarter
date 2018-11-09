import os
import pathlib
import shutil
import sys


def create_sub_dirs(project_dir):
    sub_dirs = ["css", "js", "imgs"]
    for sub_dir in sub_dirs:
        sub_path = pathlib.PurePath(project_dir, sub_dir)
        os.mkdir(sub_path)

def generate_files(project_dir, site_starter_path):
    def create_index_html_file():
        index_template_path = pathlib.PurePath(site_starter_path,"index_template.html")
        index_file_path = pathlib.PurePath(project_dir, "index.html")
        shutil.copyfile(index_template_path, index_file_path)

    def create_css_files():
        css_file_path = pathlib.PurePath(project_dir, "css", "styles.css")
        f = open(css_file_path, "w")
        f.close()

    def create_js_file():
        js_file_path = pathlib.PurePath(project_dir, "js", "main.js")
        f = open(js_file_path, "w")
        f.close()

    create_index_html_file()
    create_css_files()
    create_js_file()

def main():
    if len(sys.argv) <= 1:
        print("Site Starter generates a project file with the specified project name in the cwd.")
        print("Usage: python3 path_to_generate.py <project_name>")
    else:
        cwd = os.getcwd()
        site_starter_path = pathlib.PurePath(sys.argv[0]).parent
        project_dir = pathlib.PurePath(cwd, sys.argv[1])
        os.mkdir(project_dir)
        create_sub_dirs(project_dir)
        generate_files(project_dir, site_starter_path)


if __name__ == '__main__': main()
