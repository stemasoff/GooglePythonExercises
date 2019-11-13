**Part A**

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Suggested milestones for incremental development:

 -Extract the year and print it

 -Extract the names and rank numbers and just print them

 -Get the names data into a dict and print it

 -Build the [year, 'name rank', ... ] list and print it

 -Fix main() to use the extract_names list

**Part B**

Suppose instead of printing the text to standard out, we want to write files containing the text.
If the flag --summaryfile is present, do the following:
for each input file 'foo.html',
instead of printing to standard output, write a new file 'foo.html.summary' 
that contains the summary text for that file.

Once the --summaryfile feature is working, run the program on all the 
files using * like this: "./babynames.py --summaryfile baby*.html".
This generates all the summaries in one step.
(The standard behavior of the shell is that it expands the "baby*.html"
pattern into the list of matching filenames, and then the shell runs babynames.py,
passing in all those filenames in the sys.argv list.)