import xml.etree.cElementTree as ET
import os
import imageAdministrator

class multiImagesAdministrator():
    """
    manages multiple images imported from xml file
    imports and exports the parameters used in imageAdministrator from and to
    a xml file
    """

    def __init__(self,xmlFileName):
        self.xmlFileName = xmlFileName

    def regenerate_image_with(self,newWidth,newHeight,newIteration,newColors,xmlFile):
        """
        generate new images with different parameters than given in the 
        original xmlFile, making them uniform over all the images
        """
        #check validity of the new parameters
        #load rotate over all the images on file
            #change the parameter where a new value is given 
            #generate new image
            #generate imagename, hashfct(borders,size,color,res)
            #save        
        pass


    def generate_master_image(self,xmlFileName):
        """
        generates a master picture using the given sections, being large 
        enough to show them all and marking every section with a white rectangle 
        """
        #load parameterSets and write all the boundaries into a list
        #calculate the boundaries and add 5% on all sides for visibility
        #masterPicture.calculate_boundaries(xStartList,xEndList,yStartList,yEndList)
        #take colorscheme and iteration of the first image in the file
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
