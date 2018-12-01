import os
import sys

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines

def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()

if len(sys.argv) < 2:
    print("usage: noblanks.py infile1 [infile2 [... infileN]]")
    sys.exit()

for filename in sys.argv[1:]:
    lines = read_data(filename)
    if lines:
        write_data(lines, os.path.splitext(filename)[0] + ".nb")