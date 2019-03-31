import subprocess


def check_work():
    commit_num = subprocess.check_output("git rev-list HEAD --count", shell=True).decode('utf-8').strip()
    commit_num = int(commit_num)

    sha1 = subprocess.check_output("git rev-parse HEAD", shell=True).decode('utf-8').strip()
    work = len(sha1) - len(sha1.lstrip('0'))

    print(f"Number of commits done: {commit_num}")
    print(f"SHA1 hash of latest commit: {sha1}")
    print(f"Difficulty of work done in commit: {work}")
    assert commit_num <= work, "Not enough work done."

def check_text():
    with open('success.txt', 'r') as f:
        lines = f.readlines()
    assert len(lines) == 1, "success.txt must have only 1 line"

    line = lines[0].strip()
    assert len(line) <= 100, "Username must be shorter than 100 characters"

if __name__ == '__main__':
    check_text()
    check_work()


    

    
    
