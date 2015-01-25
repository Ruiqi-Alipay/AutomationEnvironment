import subprocess
import sys

def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

def main(argv):
	default_args = ['100', '1', '2188205015274735', 'RANDOM', 'RANDOM']
	for idx, val in enumerate(default_args):
		if idx < len(argv):
			default_args[idx] = argv[idx]

	args = " ".join(default_args)
	for output_line in run_command('java -jar environment\\autotest.jar ' + args):
	    print(output_line)

	raw_input('...')

if __name__ == "__main__":
   main(sys.argv[1:])