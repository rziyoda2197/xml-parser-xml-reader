import xml.etree.ElementTree as ET

def oqish(xml_fayl):
    tree = ET.parse(xml_fayl)
    root = tree.getroot()
    itemlar = root.findall('.//item')
    return itemlar

xml_fayl = 'xml_fayl.xml'  # XML fayliningizni yuklab oling
itemlar = oqish(xml_fayl)
for item in itemlar:
    print(item.tag, item.attrib)
```

```python
import xml.etree.ElementTree as ET

def oqish(xml_fayl):
    tree = ET.parse(xml_fayl)
    root = tree.getroot()
    return root.findall('.//item')

xml_fayl = 'xml_fayl.xml'  # XML fayliningizni yuklab oling
itemlar = oqish(xml_fayl)
for item in itemlar:
    print(item.tag, item.attrib)
