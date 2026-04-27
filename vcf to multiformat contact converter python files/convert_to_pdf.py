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

def convert():
    contacts = parse_vcf('../contacts2064.vcf')
    from fpdf import FPDF
    pdf = FPDF(format=(76.2, 101.6))
    pdf.set_margins(5, 5, 5)
    pdf.set_auto_page_break(auto=True, margin=5)
    pdf.add_page()
    for contact in contacts:
        pdf.set_font("helvetica", style="B", size=10)
        name = contact['name'].encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(0, 5, txt=name, ln=1)
        pdf.set_font("helvetica", size=10)
        for num in contact['numbers']:
            clean_num = num.replace('-', '').replace(' ', '')
            pdf.cell(0, 5, txt=clean_num, ln=1)
        pdf.ln(5)
    for _ in range(100):
        pdf.add_page()
    pdf.output('../contacts output/phonebook.pdf')

if __name__ == '__main__': convert()
