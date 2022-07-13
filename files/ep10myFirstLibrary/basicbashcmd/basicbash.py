class Bash:
    """
    Basic Bash Command - 
    it is Python's library that teach the basic bash command.
    """
    def __init__(self):
        self.intro = 'Basic Bash Command'
        self.dict = {
            'pwd':'Present working directory',
            'dir':'List directory',
            'cd':'Change directory',
            'mkdir':'Make directory',
            'rm':'Remove',
            'cp':'Copy',
            'mv':'Move',
            'cat':'Show file contents',
            'less':'Show file contents 10 lines a page',
            'head':'Show first 10 lines of file contents',
            'tail':'Show last 10 lines of file contents'
        }
        self.usage = {
'pwd' : '''
pwd
    to print out present working directory
''',
'dir' : '''
dir
    to list directory content(s)
''',
'cd' : '''
cd LOCATION
    to change working directory
cd ..
    to step back upper directory
''',
'mkdir' : '''
mkdir DIRECTORY_NAME
    to create new directory
''',
'rm' : '''
rm FILE_NAME
    to remove file
rm -r DIRECTORY_NAME
    to remove directory
''',
'cp' : '''
cp SOURCE_FILE DESTINATION_FILE
    to copy SOURCE_FILE to DESTINATION_FILE
''',
'mv' : '''
mv SOURCE_FILE DESTINATION_FILE
    to move/rename SOURCE_FILE to DESTINATION_FILE
''',
'cat' : '''
cat FILE_NAME
    to display file content
''',
'less' : '''
less FILE_NAME
    to show 10 lines of file contents page by page
''',
'head' : '''
head FILE_NAME
    to show first 10 lines of file contents
''',
'tail' : '''
tail FILE_NAME
    to show last 10 lines of file contents
'''
        }

    def list(self):
        usage = '''To display command usage type
        cmd('COMMAND')
        ex: cmd('pwd')
        Commands list display below.'''
        print(usage)
        for i in self.dict:
            print(i)
    def desc(self, command='pwd'):
        print('-=0=-')
        print(self.dict[command])

    def cmd(self, command='pwd'):
        print('-=0=-')
        commanded = self.usage[command]
        print(commanded)

if __name__ == '__main__':
    b = Bash()
    b.list()
    b.desc('cd')
    b.cmd('cp')