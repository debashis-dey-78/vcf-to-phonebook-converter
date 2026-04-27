import quopri

def decode_quoted_printable(text):
    try:
        return quopri.decodestring(text.encode('utf-8')).decode('utf-8')
    except:
        return text

def convert_vcf(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    contacts = []
    current_contact = {}
    
    for line in lines:
        line = line.strip()
        if line == 'BEGIN:VCARD':
            current_contact = {}
        elif line.startswith('FN:'):
            current_contact['name'] = line[3:]
        elif line.startswith('FN;'):
            if ':' in line:
                val = line.split(':', 1)[1]
                if 'QUOTED-PRINTABLE' in line:
                    val = decode_quoted_printable(val)
                current_contact['name'] = val
        elif line.startswith('TEL'):
            parts = line.split(':', 1)
            if len(parts) > 1:
                number = parts[1].strip()
                if 'numbers' not in current_contact:
                    current_contact['numbers'] = []
                if number not in current_contact['numbers']:
                    current_contact['numbers'].append(number)
        elif line == 'END:VCARD':
            if 'name' not in current_contact:
                current_contact['name'] = 'Unknown'
            if 'numbers' in current_contact:
                contacts.append(current_contact)

    contacts.sort(key=lambda x: x['name'].lower())

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("<html><head><style>\n")
        f.write("@page { size: 3in 4in; margin: 0.2in; }\n")
        f.write("body { font-family: Arial, sans-serif; font-size: 10pt; line-height: 1.2; }\n")
        f.write(".contact { margin-bottom: 1em; }\n")
        f.write(".name { font-weight: bold; }\n")
        f.write("</style></head><body>\n")
        for contact in contacts:
            f.write("<div class='contact'>\n")
            f.write(f"<div class='name'>{contact['name']}</div>\n")
            for number in contact['numbers']:
                clean_num = number.replace('-', '').replace(' ', '')
                f.write(f"<div>{clean_num}</div>\n")
            f.write("</div>\n")
        f.write("</body></html>\n")

if __name__ == '__main__':
    convert_vcf('../contacts2064.vcf', '../contacts output/phonebook.html')
