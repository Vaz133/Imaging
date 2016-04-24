from optparse import OptionParser
import os

## takes common string from filename, directory housing files, and file extension,
## and merges into a single file. Saves merged file into directory python script
## is launched from. 

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", type="string", action="store", help="string that filenames share in common")
parser.add_option("-d", "--directory", dest="directory", type="string", action="store", help="path to directory containing the files")
parser.add_option("-e", "--extension", dest="extension", type="string", action="store", help="file extension e.g. csv, txt")
(options, args) = parser.parse_args()

count = 0
with open(os.getcwd()+"/merged_file_"+options.filename+"."+options.extension, "a") as merged_file:
	for filename in os.listdir(options.directory):
		if options.filename in filename and options.extension in filename:
			with open(options.directory+filename, "r") as current_file:
				## remove header from all files except the first
				if count >= 1:
					data = current_file.readlines()[1:]
				else:
					data = current_file.readlines()
				for line in data:
					merged_file.write(line)
			current_file.close()
			count += 1
merged_file.close()