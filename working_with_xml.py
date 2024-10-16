import xml.etree.ElementTree as ET
from xml.dom import minidom


def create_products_xml():
    """Создает XML-файл с продуктами."""
    # Создаем корневой элемент
    root = ET.Element("products")

    # Создаем первый продукт
    product1 = ET.SubElement(root, "product")
    name1 = ET.SubElement(product1, "name")
    name1.text = "Молоко"
    price1 = ET.SubElement(product1, "price")
    price1.text = "25"
    quantity1 = ET.SubElement(product1, "quantity")
    quantity1.text = "30"

    # Создаем второй продукт
    product2 = ET.SubElement(root, "product")
    name2 = ET.SubElement(product2, "name")
    name2.text = "Хліб"
    price2 = ET.SubElement(product2, "price")
    price2.text = "10"
    quantity2 = ET.SubElement(product2, "quantity")
    quantity2.text = "100"

    # Создаем дерево XML
    tree = ET.ElementTree(root)

    # Записываем в временный файл
    with open("products_temp.xml", "wb") as fh:
        tree.write(fh, encoding='utf-8', xml_declaration=True)

    # Форматируем XML для удобочитаемости
    with open("products_temp.xml", "r", encoding='utf-8') as fh:
        xml_str = fh.read()

    # Используем minidom для форматирования
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")

    # Записываем отформатированный XML в финальный файл
    with open("products.xml", "w", encoding='utf-8') as fh:
        fh.write(pretty_xml)


# Создаем файл с продуктами
create_products_xml()
