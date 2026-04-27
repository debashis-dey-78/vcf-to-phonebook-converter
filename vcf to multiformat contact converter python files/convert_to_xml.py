import quopri
def decode_quoted_printable(text):
    try: return quopri.decodestring(text.encode('utf-8')).decode('utf-8')
    except: return text

def parse_vcf(input_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f: lines = f.readlines()
    contacts, current_contact = [], {}
    for line in lines:
        line = line.strip()
        if line == 'BEGIN:VCARD': current_contact = {}
        elif line.startswith('FN:'): current_contact['name'] = line[3:]
        elif line.startswith('FN;'):
            if ':' in line:
                val = line.split(':', 1)[1]
                if 'QUOTED-PRINTABLE' in line: val = decode_quoted_printable(val)
                current_contact['name'] = val
        elif line.startswith('TEL'):
            parts = line.split(':', 1)
            if len(parts) > 1:
                number = parts[1].strip()
                if 'numbers' not in current_contact: current_contact['numbers'] = []
                if number not in current_contact['numbers']: current_contact['numbers'].append(number)
        elif line == 'END:VCARD':
            if 'name' not in current_contact: current_contact['name'] = 'Unknown'
            if 'numbers' in current_contact: contacts.append(current_contact)
    contacts.sort(key=lambda x: x['name'].lower())
    return contacts

import xml.etree.ElementTree as ET
def convert():
    contacts = parse_vcf('../contacts2064.vcf')
    root = ET.Element("Phonebook")
    for contact in contacts:
        c_el = ET.SubElement(root, "Contact")
        n_el = ET.SubElement(c_el, "Name")
        n_el.text = contact['name']
        nums_el = ET.SubElement(c_el, "Numbers")
        for num in contact['numbers']:
            num_el = ET.SubElement(nums_el, "Number")
            num_el.text = num.replace('-', '').replace(' ', '')
    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ", level=0)
    tree.write('../contacts output/phonebook.xml', encoding='utf-8', xml_declaration=True)

if __name__ == '__main__': convert()
