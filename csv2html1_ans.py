#!/usr/bin/env python3.6





import sys
import xml.sax.saxutils

import cvs2html

def print_start():
    print("<table border='1'>")




def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgeen"
            elif count % 2:
                color = "while"
            else:
                color = "lightyellow"
                print_line(line, color, maxwidth)
                count += 1
        except EOFError:
            break
    print_end()






def print_line(line, color, maxwidth):
    print("<tr dgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field =field.title()
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
        if  c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c: # end of quoted string
                quote = None
            else:
                field += c # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
                fields.append(field)
                field = ""
        else:
            field += c # accumulating a field
            if field:
                field.append(field) #adding the last field
                return fields



def print_end():
    print("</table>")

    main()






