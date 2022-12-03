
from csv import DictReader
from jinja2 import Template


# open file in read mode
with open("BOOKS.csv", 'r') as f:
    dict_reader = DictReader(f)

    bookslist = list(dict_reader)
def main():
    template_file=open("HOME.html.jinja2")
    template1=template_file.read()
    template_file.close()
    template = Template(template1)
    content=template.render(bookslist=bookslist)
    myfile=open('index.html','w')
    myfile.write(content)
    myfile.close()


if __name__ == '__main__':
    main()
