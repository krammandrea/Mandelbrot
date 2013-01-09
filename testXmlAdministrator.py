import xmlAdministrator
#TODO why are the filenames too similar?
#TODO

if __name__ =='__main__':
    """
    test cases for the xmlAdministrator.change_images_with() function
    """
    #initalize imageAdministrator colorAlg
    currentSet = xmlAdministrator.XmlAdministrator("parameterSets.xml")

    #testcases
    #test every input variable for invalid input and new input 
    #test valid input
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = ['000000','333333','666666','999999','CCCCCC'],
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = str(20),
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    #test out of bound input
    currentSet.recalculate_images_with( newWidth = str(0),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400000000000),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(0),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(40000000000000),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = str(0),
                                        newColors = str(['000000']),
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = str(10000000000000),
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "nonExistantFile.xml")
    #test invalid input
    currentSet.recalculate_images_with( newWidth = "invalid",
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = "invalid",
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = "invalid",
                                        newColors = None,
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = "invalid",
                                        xmlFileName = "parameterSets.xml")
    currentSet.recalculate_images_with( newWidth = str(400),
                                        newHeight = str(400),
                                        newIteration = None,
                                        newColors = None,
                                        xmlFileName = "invalid")
