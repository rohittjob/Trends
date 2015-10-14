from os import system, chdir
from os.path import join

if __name__ == '__main__':
	path = join('..','file_hash')
	chdir(path)

	path = join(path, 'integrity_test.py')	
	system('python ' + path)