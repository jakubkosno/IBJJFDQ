# How to use this script
1. Install python (https://www.python.org/downloads/) and git (https://git-scm.com/install/windows).
2. In order to setup an environment for using this project open terminal of your choice (e.g. previously installed git) and type the following commands.
`git clone https://github.com/jakubkosno/IBJJFDQ.git`
`cd IBJJFDQ`
`pip install -r requirements.txt`
3. Run the script using the following command.
`python dq.py`
4. Cooperate. The script will ask for an url of a tournament you're interested in. Paste its addres into a terminal. Example url is https://www.bjjcompsystem.com/tournaments/3045/categories. Scanning all brackets requires sending a significant number of network requests, which takes time. Once all disualified athletes are found their names can be found in file dq_results.txt.<br>Please note that for now the script doesn't automatically search for both genders, therefore in order to get all disqualified athletes from a given tournament you need to run it twice with two different urls. 


