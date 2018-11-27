import sys
import unicodedata

word = None
code = ord(" ")
end = sys.maxunicode

def print_unicode_table(word):
    print("decimal hex chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format("-" * 40))


if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv))
        word = 0
    else:
        word = sys.argv[1].lower()
        if word != 0:
            print_unicode_table(word)


            while code < end:
                c = chr(code)
                name = unicodedata.name(c, "*** unknown ***")
                if word is None or word in name.lower():
                    print("{0:7} {0:5x} {0:^3c} {1}".format(code, name, title()))
                    code += 1

