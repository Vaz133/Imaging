from PIL import Image
from optparse import OptionParser
from os import listdir
from scipy import misc

parser = OptionParser()
parser.add_option("-i", "--input_images", dest="images", type="string", action="store", help="string that images share in common")
parser.add_option("-d", "--directory", dest="directory", type="string", action="store", help="directory to search for images")
parser.add_option("-x", "--x_dim", dest="x_dim_final", type="int", action="store", help="final image dimensions x")
parser.add_option("-y", "--y_dim", dest="y_dim_final", type="int", action="store", help="final image dimensions y")
parser.add_option("-e", "--extension", dest="extension", type="string", action="store", help="file extension")
(options, args) = parser.parse_args()

image_list = []
x = 0
y = 0
new_im = Image.new('RGB', (options.x_dim_final, options.y_dim_final))	
for filename in listdir(options.directory):
	if options.images in filename and options.extension in filename:
		im = Image.open(options.directory+filename)	
		new_im.paste(im, (x,y))	
		width, height = im.size
		x += width
		if x >= options.x_dim_final:
			x = 0
			y += height	

new_im.save(options.directory+options.images+options.extension)








