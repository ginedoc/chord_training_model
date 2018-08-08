import glob

fw = open('../filelist.txt', 'w')

for f in glob.glob('../midi/*.mid'):
	fw.write(f)
	fw.write('\n')
fw.close()
