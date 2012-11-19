import xml.etree.ElementTree as ET
import imageAdministrator,coloralg,argparse


if __name__ =='__main__':
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

#load xmlFile to imageAdministrator

#option --showThumbnails
#change size to 200x200 and generate new images

#option --showMasterImage
#send all to generateMasterImage

#option --changePixelSize
#change pxSize to desired size and generate new images

#option --changeIterations
#change number of iterations and generate new images

#generate a html page showing the parameters in the given file as well as the 
#generated images and save everything(xml, thumbnails, masterimage, large images,html) in a folder
#name: xmlFile+ThumbNail+Number

    """
    self.colorAlg = coloralg.ColorAlg()
    try:
        tree = ET.parse(xmlFileName)
        root = tree.getroot()

    except: 
        #no xml-data in file or file nonexistent
        print "No xml-data in "+xmlFileName
        
    #create thumbnails
    for parameterSet in root.iter('parameterSet'):
        #TODO if loading succesful
        if (self.colorAlg.loadParametersFromXml(parameterSet)):
            #overwrite pxsize with thumbnailsize
            #save in file
        else:
            print "Parameters imported from "+xmlFileName+" are invalid."
"""
