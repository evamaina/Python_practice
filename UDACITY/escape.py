# User Instructions
# 
# Implement the function escape_html(s), which replaces
# all instances of:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
	for (i,o) in (("$","&amp;"),
				  (">","&gt;"),
    			  ("<","&lt;"),
    			  ('"',"&quote;")):
		s = s.replace(i,o)
	return s
print(escape_html('>'))
print(escape_html('<'))
print(escape_html('"'))
print(escape_html("&"))