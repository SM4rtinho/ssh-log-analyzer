import re
from collections import defaultdict

LOG_FILE = 'sample_auth.log'
FAILED_LOGIN_PATTERN = r"Failed password for(?: invalid user)? (\w+) from ([\d.]+)"

attempts_by_user = defaultdict(int)
attempts_by_ip = defaultdict(int)

with open(LOG_FILE, 'r') as file:
    for line in file:
        match = re.search(FAILED_LOGIN_PATTERN, line)
        if match:
            user, ip = match.groups()
            attempts_by_user[user] += 1
            attempts_by_ip[ip] += 1

with open('report.txt', 'w') as report:
    report.write("SSH Failed Login Report\n\n")
    
    report.write("Attempts by user:\n")
    for user, count in attempts_by_user.items():
        report.write(f"{user}: {count}\n")

    report.write("\nAttempts by IP address:\n")
    for ip, count in attempts_by_ip.items():
        report.write(f"{ip}: {count}\n")

print("Report saved to 'report.txt'")


