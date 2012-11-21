import xml.etree.cElementTree as ET
import os
import imageAdministrator

class XmlAdministrator():
    """
    imports and exports the parameters used in imageAdministrator from and to
    a xml file
    """

    def __init__(self,xmlFileName):
        self.xmlFileName = xmlFileName

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
        
