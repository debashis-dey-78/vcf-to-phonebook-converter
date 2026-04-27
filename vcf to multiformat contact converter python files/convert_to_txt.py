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
        for contact in contacts:
            f.write(f"{contact['name']}\n")
            for number in contact['numbers']:
                clean_num = number.replace('-', '').replace(' ', '')
                f.write(f"{clean_num}\n")
            f.write("-----------------\n")

if __name__ == '__main__':
    convert_vcf('../contacts2064.vcf', '../contacts output/phonebook.txt')
