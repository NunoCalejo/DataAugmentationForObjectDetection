def Save_Label(filename, labels):

    number2item = {1:'button', 2:'input_text', 3:'radio', 4:'select'}
    
    import xml.etree.ElementTree as xml
    #XML file
    
    root = xml.Element("annotation")
    
    folder = xml.Element("folder")
    root.append(folder)
    folder.text = "images"
    
    imgfile = xml.Element("filename")
    root.append(imgfile)
    imgfile.text = filename + '.png'
    
    size = xml.Element("size")
    root.append(size)
    width = xml.SubElement(size, "width")
    width.text = str(500)
    height = xml.SubElement(size, "height")
    height.text = str(500)
    
    for label in labels:
        objectelement = xml.Element("object")
        root.append(objectelement)
        
        name = xml.SubElement(objectelement, "name")
        name.text = str(number2item[label[4]])
        
        bndbox = xml.SubElement(objectelement, "bndbox")
        xmin = xml.SubElement(bndbox, "xmin")
        xmin.text = str(label[0])
        ymin = xml.SubElement(bndbox, "ymin")
        ymin.text = str(label[1])
        xmax = xml.SubElement(bndbox, "xmax")
        xmax.text = str(label[2])
        ymax = xml.SubElement(bndbox, "ymax")
        ymax.text = str(label[3])
    
    tree = xml.ElementTree(root)
    with open('./Train_annotations_aug/xml/' + filename + '.xml', "wb") as fh:
        tree.write(fh)
    
    #txt file
    # Open for 'w'riting 
    file_name = './Train_annotations_aug/txt/' + filename +  '.txt'
    f = open(file_name, 'w')
    for label in labels:
        item_label = str(number2item[label[4]]) + ' ' + str(label[0]) + ' ' + str(label[1]) + ' ' + str(label[2]) + ' ' + str(label[3]) + "\n" 
        f.write(item_label)
    f.close()