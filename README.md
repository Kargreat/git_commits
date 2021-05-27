# git_commits
## Algorithm
* Read user inputs for:
    * GitHub Username
    * GitHub Personal Access Token
    * Last n commits (parameterizing commit count)
* Connects to GitHub, and retrieves the events in a descending orer (default)
* For events type 'PushEvent' which tracks commit, store the dates
* Do a function call to write the list to a csv
* In separate function calculate the mean time

## Python Packages
PyGitHub (Python Github package, GitHub Python SDK)
    
## Hot to Run
* built on python=3.6
* install the requirements: pip install -r requirements.txt
* command to execute (from project root): python3.6 __main__.py

## Notes
1. All files are at the same level for this assignment - one child level from the project list

