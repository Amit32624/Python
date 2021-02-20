#
# Simple bulk pretty-printing tool for Python assignments. Assumes base 
# submission directory contains individual student submissions as .py files.
# File names must conform to Canvas export format as specified in regular
# expression below. 
#
# Kieran Herley, February 2021
#

import sys
import re
import os, os.path
import datetime
import subprocess

# Specify path to submission directory.
SUBPATH = "./a99"

# Specify assignment and module parameters.
MODULE = "CS6507"
SEMESTER = "Sem 2"
YEAR = "2020-2021"
INSTRUCTOR = "KTH"
ASSIGNMENT = "Python Print Tool"
EXPECTED_NAME = "a99"
EXPECTED_EXTN = ".py"

# Specify a2ps  configuration parameters.
NUP_FACTOR = 2           # Use 1 for one page per sheet, 2 for two per.
LINENUMBER_SKIP = 5      # Use 5 for every 5th line numbered.
TAB_FACTOR = 4           # Use 4 for 4 spaces for tab.
LINES_PER_PAGE = 70      # Specify number of lines in single 1up page under a2ps.

# Specify header and footer parameters.
WATERMARK = MODULE       
LEFT_TITLE = MODULE      
RIGHT_TITLE = ASSIGNMENT
DATE = datetime.date.today().strftime("%d/%m/%y")
FOOTER = DATE
LEFT_FOOTER = "%s, %s" % (SEMESTER, YEAR)
RIGHT_FOOTER = INSTRUCTOR

# Specify a2ps command template.
PRINT_TEMPLATE = """a2ps\
        -%d\
        --pretty-print=%%s\
        --highlight-level='heavy'\
        --no-header\
        --chars-per-line=79\
        --truncate-lines='yes'\
        --prologue=fixed\
        --line-numbers=%d\
        --tabsize=%d\
        --underlay='%s'\
        --center-title='%%%%s'\
        --left-title='%s'\
        --right-title='%s'\
        --footer='%s'\
        --left-footer='%s'\
        --right-footer='%s'\
        '%%%%s'
        """ % (
          NUP_FACTOR,
          LINENUMBER_SKIP,
          TAB_FACTOR,
          WATERMARK,
          LEFT_TITLE,
          RIGHT_TITLE,
          FOOTER,
          LEFT_FOOTER,
          RIGHT_FOOTER
       )

# Particularize template for Python code.
CODE_TEMPLATE = PRINT_TEMPLATE % "python"

# Canvas submission names have format:
#     murphyjohnpatrick_12345_67891_thenameofthefile.xyz
# Late submissions are tagged "_LATE" and ressubmissions are tagged
# thenameofthefile-2.xyz etc.
CANVAS_HANDLE_RE = re.compile(
    r"(?P<stname>[a-z]+)(_LATE)?_\d+_\d+_(?P<stfilename>(\w|[_\-. ()])+)")

def pretty_print_code(pyfilepath,  student_name, student_id = "???"):
    """ Pretty-print the Python file at path 'pyfilepath', incorporating 
    'student_name' and 'student_id' (if provided).
    """
    printcmd = CODE_TEMPLATE % (
        "%s (%s)" % (student_name, student_id), pyfilepath)
    sp = subprocess.Popen(printcmd, shell=True)
    sp.wait()
  

def print_one(filepath):
    """ Print the file at path 'filepath'. Files with wrong extention or
    broken format are skipped; those with unexpected names are flagged.
    """
  
    fullfilename = os.path.basename(filepath)
    fname, fext  = os.path.splitext(filepath)

    if fext != EXPECTED_EXTN:
        print("Unexpected file extn '%s' for file '%s'-- file skipped." % (fext, fullfilename))
        return

    if not fname.endswith(EXPECTED_NAME):
        print("Unexpected file name '%s' for file '%s'." % (fname, fullfilename))
 
    m = CANVAS_HANDLE_RE.match(fullfilename)
    if m is None:
        print("Unexpected file name format for file '%s'." % fullfilename)
        return

    stname, subname = m.group("stname"), m.group("stfilename")
    print("Printing %s  . . . " % (stname), end = "")
    pyfilepath = os.path.join(SUBPATH, fullfilename)
    pretty_print_code(pyfilepath, stname)     
    print("Done!")
    
    return True
         
if __name__ == "__main__":
    all_files = os.listdir(SUBPATH)
    for afile in all_files:
        print_one(afile)

        break
        
        
