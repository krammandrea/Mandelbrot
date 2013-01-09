import xml.etree.cElementTree as ET
import os
import imageAdministrator

class XmlAdministrator():
    """
    manages multiple images imported from xml file
    imports and exports the parameters used in imageAdministrator from and to
    a xml file
    """

    def __init__(self,xmlFileName):
        self.xmlFileName = xmlFileName

    def recalculate_images_with(self,newWidth,newHeight,newIteration,newColors,xmlFileName):
        """
        generate new images with different parameters than given in the 
        original xmlFile, making those uniform over all the images
        All the new files are saved in a new directory
        """
        imageAdmin = imageAdministrator.ImageAdministrator()
        #check validity of the new parameters and if invalid return
        #using short circuit evaluation to avoid calling is..Valid when
        #expression is None, expression False and X, X won't be evaluated
        if(not(newWidth==None) and not imageAdmin.isSizeInputValid(newWidth)):
            print "the given width is not valid"
            return
        if(not(newHeight==None)and not imageAdmin.isSizeInputValid(newHeight)):
            print "the given height is not valid"
            return
        if(not(newIteration==None)and not imageAdmin.isIterationInputValid(newIteration)):
            print "the given number of iterations is not valid"
            return
        if(not(newColors==None)and not imageAdmin.isColorInputValid(newColors)):
            print "the given colorscheme is not valid"
            return

        #load rotate over all the images on file
        try:
            xmlFile = open (xmlFileName,'r')
            tree = ET.parse(xmlFileName)
            root = tree.getroot()
        except Exception as exceptionMessage:
            print "error loading xml structure from xml file"
            print exceptionMessage 
            return
        #start new xml file containing the modyfied parameters
        newRoot = ET.Element('parameterSetList')
        newTree = ET.ElementTree(newRoot)
        dirAdded = False
        

        for parameterSet in root.findall('parameterSet'):
        #using root.iter() here causes the loop to run indefinitely, not reproducable using python in the shell
            if (imageAdmin.load_parameters_from_xml(parameterSet)):
                #change the parameter where a new value is given 
                if (newWidth != None and newHeight != None):
                    imageAdmin.change_imagesize(int(newWidth),int(newHeight))
                if (newIteration != None):
                    imageAdmin.change_maxiteration(int(newIteration))
                if (newColors !=None):
                    imageAdmin.change_colorscheme(newColors)

            else:
                print "Parameters imported from "+xmlFileName+" are invalid."
                #go try the next set of parameters on file

            #generate imagename, hashfct(borders,size,color,res)
            newImageName = str(newWidth)+"x"+str(newHeight)+"i"+str(newIteration)+"cs"+imageAdmin.generate_checksum()

            #and use first set of parameters to name new directory and xml file
            if (dirAdded == False):
                try:
                    if (os.path.isdir(newImageName)):
                        print "using already existing "+newImageName+" directory."
                    else:
                        os.mkdir(newImageName)

                    newDir = newImageName
                    newXmlFile = os.path.join(newDir,newImageName)+".xml"
                    dirAdded = True
            
                except Exception as exceptionMessage:
                    print "error adding directory "+newImageName
                    print exceptionMessage
                    return

            newImagePath = os.path.join(newDir,newImageName)+".png"
            #generate new image
            imageAdmin.calculate_mandelbrot(newImagePath)

            #add the current set of parameters to the new file
            currentParaSet = ET.SubElement(newRoot, 'parameterSet')
            currentParaSet = imageAdmin.write_parameters_to_xml_tree(currentParaSet)

            #save complete xml File
            newTree.write(newXmlFile)

    def generate_master_image(self,xmlFileName):
        """
        generates a master picture using the given sections, being large 
        enough to show them all and marking every section with a white rectangle 
        """
        #TODO
        #load parameterSets and write all the boundaries into a list
        #calculate the boundaries and add 5% on all sides for visibility
        #masterPicture.calculate_boundaries(xStartList,xEndList,yStartList,yEndList)
        #take colorscheme and iteration of the first image in the file
        #generate imagename, hashfct(borders,size,color,res)
        #generate masterpictue
        #mark every given section with a white line, using drawBorderLines
        #masterPicture.draw_border_lines(xStartList,xEndList,yStartList,yEndList)
        pass

    def write_parameters_to_xml(self,xmlFileName,imageAdministrator):
        """
        check if file already exist, if not create and add root
        """
        xmlFile = open (xmlFileName,'a')
        
        if (os.path.getsize(xmlFileName)==0): #TODO try-catch?
            #is empty
            root = ET.Element('parameterSetList')        
            #wrap in ElementTree instance
            tree = ET.ElementTree(root)
        else:
            tree = ET.parse(xmlFileName)
            root = tree.getroot()

        
        #add the current set of parameters to the file
        currentParaSet = ET.SubElement(root, 'parameterSet')
        currentParaSet = imageAdministrator.write_parameters_to_xml_tree(currentParaSet)

        #save to file
        tree.write(xmlFileName)  
        
    """
        
    #create thumbnails
    for parameterSet in root.iter('parameterSet'):
        #TODO if loading succesful
        if (self.colorAlg.loadParametersFromXml(parameterSet)):
            #overwrite pxsize with thumbnailsize
            #save in file
        else:
            print "Parameters imported from "+xmlFileName+" are invalid."
"""
