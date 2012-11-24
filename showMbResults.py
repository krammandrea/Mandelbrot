import xml.etree.ElementTree as ET
import imageAdministrator,argparse,

#default size in pixel for a square thumbnail image
THUMBNAILSIZE = 200; 


if __name__ =='__main__':
"""
generate more readable html out of the parameterSets saved as xml, with the option
of generating thumbnails, masterImages and large scale images
"""
#initalize imageAdministrator colorAlg
    #?
    parser = argparse.ArgumentParser()
    parser.add_argument("xmlFileName", type = file,
                    help ="show the accumulated parameters in a html overview")
    parser.add_argument("-t","--showThumbnails", action = 'store_true',
                    help ="add 200x200 thumbnails of the generated images")
    parser.add_argument("-m","--showMasterImage", action = 'store_true',
                    help ="add a master image showing all the sections")
    parser.add_argument("-s","--changePixelSizeTo",nargs = 2,type=int,
                    help="generate all the sections in the pixel size given, takes two arguments width and height")
    parser.add_argument("-i","--changeIterationsTo",type=int,
                    help ="change the number of iterations")
    parser.add_argument("-c","--useColorScheme")
    args = parser.parse_args()
    print args

#write html file outline
#format xml to html table
#start new folder in same directory to save all the newly generated pictures and 
#html there, as well as an xml-file with the new parameters

#option --showThumbnails
#multiImageAdministrator.regenerate_image_with(THUMBNAILSIZE,THUMBNAILSIZE,None,None,filename)
#add images to the html table

#option --showMasterImage
#multiImageAdministrator.generate_master_image(filename)
#takes colorscheme and iteration of the first image on file
#add to html

#option --changePixelSize
#multiImageAdministrator.regenerate_image_with(givenWidth,givenHeight,None,None,filename)
#change pxSize to desired size and generate new images

#option --changeIterations
#multiImageAdministrator.regenerate_image_with(None,None,newIteration,None,filename)
#change number of iterations and generate new images

#generate a html page showing the parameters in the given file as well as the 
#generated images and save everything(xml, thumbnails, masterimage, large images,html) in a folder
#name: xmlFile+ThumbNail+Number
