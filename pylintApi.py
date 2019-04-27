from pylint.lint import Run
import getpass
import requests
import json
import re
import os
import shutil

#1. Replicate repository at server.
def getFileNames(user_name, repository, path, old_dir):
    URL = 'https://api.github.com/repos/{}/{}/contents/{}'.format(user_name, repository, path)
    response = requests.get(URL)
    responseJson = response.json()

    # Create a repository dir.
    currentPath = os.path.abspath(os.path.dirname(__file__))
    currentPath = currentPath + '/downloaded_data/'
    old_dir = old_dir
    if os.path.exists(currentPath) and old_dir:
        shutil.rmtree(currentPath

    if old_dir:
        try:
            os.mkdir(currentPath)
        except OSError as err:
            return "Creation of the directory {} failed with message: {}".format(currentPath, err)
        else:
            print ("Successfully created the directory {} ".format(currentPath))
            old_dir = False

    for branches in responseJson
        if(branches.get('type') == 'file'):
            if re.findall("py$", branches.get('name')):
                print(branches.get('path'))

                filePath = currentPath + branches.get('path')
                if not os.path.exists(os.path.dirname(filePath)):
                    try:
                        os.makedirs(os.path.dirname(filePath))
                    except OSError as exc:
                        print('Error while replicating files from github.')

                fileDownloadPath = branches.get('download_url')
                file_response = requests.get(fileDownloadPath)
                file_content = file_response.text

                with open(filePath, "w") as f:
                    f.write(file_content)

        elif(branches.get('type') == 'dir'):
            getFileNames(user_name, repository, branches.get('path'), old_dir)


    return 'Complete !!!'


#Check valid URL
def checkValidUrl(URL):
    # URL = "https://api.github.com/repos/ayushjain10/MockRepo"
    r = requests.get(URL)
    fileJson = r.json()
    for keys in fileJson:
        #print(keys)
        if (keys == 'id'):
            return True
    return False

# Method to run the PyLint code which displayes C/R/E/W in a single code file
#   C -> Convention
#   R -> Refactor
#   E -> Error
#   W -> Warning
def runCREWFile(filename):
    os.system('cat file.txt > ""')
    os.system('pylint '+filename+' > file.txt')

# Check runCREWFile function.
# runCREWFile("MockRepo/isprime.py")

# Method to run the PyLint code which displayes C/R/E/W in all code files in a repo
#   C -> Convention
#   R -> Refactor
#   E -> Error
#   W -> Warning
def runCREWRepo(repo):
    os.system('cat file.txt > ""')
    os.system('pylint '+repo+'/*.py > file.txt')

# Check runCREWRepo function.
# runCREWRepo("MockRepo")

def getWarningCount(filename):
    file = open(filename, "r")
    count = 0
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "W" in output:
                count += 1
    return count

# Check getWarningCount function.
# getWarningCount("file.txt")

def getErrorCount(filename):
    file = open(filename, "r")
    count = 0
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "E" in output:
                count += 1
    return count

# Check getErrorCount function.
# getErrorCount("file.txt")


def getConventionCount(filename):
    file = open(filename, "r")
    count = 0
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "C" in output:
                count += 1
    return count

# Check getConventionCount function.
# getConventionCount("file.txt")

def getRefactorCount(filename):
    file = open(filename, "r")
    count = 0
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "R" in output:
                count += 1
    return count

# Check getRefactorCount function.
# getRefactorCount("file.txt")

def getConventionDict(filename):
    file = open(filename, "r")
    count = 0
    output_dict = dict()
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "C" in output:
                if output in output_dict:
                    output_dict[output] += 1
                else:
                    output_dict[output] = 1
    return output_dict

#Check getConventionDict function
# getConventionDict("file.txt")

def getRefactorDict(filename):
    file = open(filename, "r")
    count = 0
    output_dict = dict()
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "R" in output:
                if output in output_dict:
                    output_dict[output] += 1
                else:
                    output_dict[output] = 1
    return output_dict

#Check getRefactorDict function
# getRefactorDict("file.txt")

def getErrorDict(filename):
    file = open(filename, "r")
    count = 0
    output_dict = dict()
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "E" in output:
                if output in output_dict:
                    output_dict[output] += 1
                else:
                    output_dict[output] = 1
    return output_dict

#Check getErrorDict function
# getErrorDict("file.txt")

def getWarningDict(filename):
    file = open(filename, "r")
    count = 0
    output_dict = dict()
    for line in file:
        if re.findall(": [CREW]", line):
            output = line.split(":")[3]
            if "W" in output:
                if output in output_dict:
                    output_dict[output] += 1
                else:
                    output_dict[output] = 1
    return output_dict

#Check getWarningDict function
# getWarningDict("file.txt")

def runDupFile(filename):
    os.system('cat file2.txt > ""')
    os.system('pylint --disable=all --enable=duplicate-code --reports=yes repository_dir/'+filename+' > file2.txt')

def runDupRepo(duplicate_info_file, f_path):
    # os.system('cat {} > ""'.format(duplicate_info_file))
    open(duplicate_info_file, 'a').close()
    print('debug 0')
    # Run(['--disable=all', '--enable=duplicate-code', '--reports=yes', f_path])
    # os.system('pylint --disable=all --enable=duplicate-code --reports=yes {} > {}'.format(f_path, duplicate_info_file))
    print('debug 1')
    with open(duplicate_info_file, 'w') as f:
        f.write(output)
        print('debug 2')
    print('debug 3')

#Test runDupFile()
# runDupFile("factorial.py")

#Test runDupRepo()
# runDupRepo()

def getCodePercentage(filename):
    file = open(filename, "r")
    for line in file:
        if "|code      |" in line:
            output = line.split('|')
            return output[3]

# getCodePercentage("file2.txt")

def getDocStringPercentage(filename):
    file = open(filename, "r")
    for line in file:
        if "|docstring |" in line:
            output = line.split('|')
            return output[3]

# getDocStringPercentage("file2.txt")

def getCommentPercentage(filename):
    file = open(filename, "r")
    for line in file:
        if "|comment   |" in line:
            output = line.split('|')
            return output[3]

# getCommentPercentage("file2.txt")

def getEmptyPercentage(filename):
    file = open(filename, "r")
    for line in file:
        if "|empty     |" in line:
            output = line.split('|')
            return output[3]

# getEmptyPercentage("file2.txt")

def getNumberDuplication(filename):
    file = open(filename, "r")
    for line in file:
            output = line.split('|')
            return output[2]

def getPercentDuplication(filename):
    file = open(filename, "r")
    for line in file:
            output = line.split('|')
            return output[2]

def doCodeCoverageFile(filename):
    os.system('cat file3.txt > ""')
    os.system('pip install coverage')
    os.system('coverage run '+filename)
    os.system('coverage report -m > file3.txt')

def doCodeCoverageRepo():
    files = getFileNames("https://api.github.com/repos/ayushjain10/MockRepo")
    file_string = ""
    os.system('cat file3.txt > ""')
    os.system('pip install coverage')
    for file in files:
        os.system('coverage run MockRepo/'+file)
        file_string = file_string+" MockRepo/"+file
    os.system('coverage report -m '+file_string+'> file3.txt')

# doCodeCoverageRepo()

def getTotalCodeCoverage(filename):
    file = open(filename, "r")
    coverage_list = []
    for line in file:
        if "%" in line:
            print(line)
            p = re.compile("[0-9]?[0-9]%")
            m = p.match(line)
            #m = re.match("0%", line)
            print(m)
            #coverage_list.append(m.group(1))
    print(coverage_list)

# if __name__ == '__main__':
#     user_name = 'abhishekpareek29'
#     token = "ad11b20c651bf7b342f12275fdc181fb5ef96905"
#     repository = 'csc510_mock_repo'
#     path = ''
#     getFileNames(user_name, repository, path, True)
