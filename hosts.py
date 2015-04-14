import string
import argparse


HOSTS_PATH = 'c:/windows/system32/drivers/etc/hosts'
COMMENT = '#added by Dower'


def add(name):
    print('Adding %s...' % name)
    with open(HOSTS_PATH, 'a') as fout:
        fout.write('\n127.0.0.1{0}{1} {2}'.format('\t'*4, name, COMMENT))
    
def remove(name):
    print('Removing %s...' % name)
    with open(HOSTS_PATH) as fin:
        data = fin.readlines()
        
    result = ''
    occured = False
    for line in data:
        line = line.strip()
        host, sep, remain = line.partition(' ')
        try:
            host_addr, host_name, comment = line.split(None, 2)
        except ValueError:
            host_addr, host_name = line.split(None, 1)
        if 'comment' in locals():
            print(comment)
            del comment
        if name == host_name:
            occured = True
            continue
        result += line + '\n'
            
    if occured:
        with open(HOSTS_PATH, 'w') as fout:
            fout.write(result)
        print('Host %s was removed.' % name)
    else:
        print('Such host was not found: %s.' % name)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add or remove entry in hosts file')
    parser.add_argument('command', help="the command to perform", choices=['add', 'remove'])
    parser.add_argument("name", type=str, help="name of the alias")
    args = parser.parse_args()
    globals()[args.command](args.name)