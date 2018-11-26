#!user/bin/python3.7


import sys
import xml.sax.saxutils

def main():
    maxwidth, format = process_options()
    if maxwidth is not None:
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "while"
                else:
                    color = "lightyellow"
                    print_line(line, color, maxwidth, format)
                    count += 1
            except EOFError:
                break
        print_end()




def process_options():
    maxwidth_arg = "maxwidth="
    format_argv = "format="
    maxwidth = 100
    format = ".0f"
    for argv in sys.argv[1:]:
        if argv in ["-h", "--help"]:
            print("""\
            usage:
            csv2html.py [maxwidth=int] [format=str]<infile.csv>outFile.html
            maxwidth is an options integer; if specified, it sets the maximum number of characters hat can be output for string fields, otherwise a default of {0} characters is used.
             format is the format to use for numbers; if not specified it defaults to {1}.""".format(maxwidth, format))
            return None, None
        elif argv.startswith(maxwidth_arg):
            try:
                maxwidth = int(argv[len(maxwidth_arg):])
            except ValueError:
                pass
        elif arg.startswith(format_argv):
            format = argv[len(format_argv):]
            return maxwidth, format




def print_start():
    print("<table border ='1'>")



def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0]'>".format(color))
    numberFormat = "<td align='right'>{{0:{0}}}</td>".format(format)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(numberFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
            else:
                field = "{0} ...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
                print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
                if field:
                    continue
                if quote is None and c == ",":
                    fields.append(field)
                    field = ""
                else:
                    field += c
                    if field:
                        fields.append(field)
                        return fields


def print_end():
    print("</table>")




main()




