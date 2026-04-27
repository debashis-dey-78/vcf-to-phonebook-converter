# VCF to Multi-Format Phonebook Converter
## Project Documentation & Specifications

### 1. Project Overview
The **VCF to Phonebook Converter** is a specialized utility designed to parse raw `.vcf` (vCard) contact backups from a mobile device and convert them into beautifully formatted, printable, physical-pocket-sized phonebooks. 

### 2. Application Specifications
#### Core Formatting Requirements:
- **Dimensions:** Formatted precisely for 3" x 4" physical pages (ideal for fitting perfectly into a standard pant pocket).
- **Typography:** Contact names are strictly displayed in **Bold**, while phone numbers are in a normal font.
- **Layout:** No spaces exist between the contact's name and their number. A single line break separates each complete contact block.
- **Data Sanitization:** Hyphens and spaces are automatically stripped from phone numbers for maximum space efficiency.
- **Sorting:** All contacts are automatically alphabetized from A to Z prior to rendering.

#### Supported Output Formats:
The core conversion engine was expanded to output the phonebook into 10 distinct formats to fit any possible user need:
1. **PDF (`.pdf`)** - Exact 3" x 4" formatting locked for printing.
2. **Word (`.docx`)** - Exact 3" x 4" formatting, editable.
3. **HTML (`.html`)** - Web-viewable, uses CSS `@page` rules for 3"x4" print rendering.
4. **Excel (`.xlsx`)** & **CSV (`.csv`)** - Spreadsheet formats for digital organization.
5. **Markdown (`.md`)** & **Rich Text Format (`.rtf`)** - For note-taking apps and universal word processors.
6. **JSON (`.json`)** & **XML (`.xml`)** - For database integration and developers.
7. **Text (`.txt`)** - Raw, lightweight text output.

#### Special Features:
- **Blank Pages:** The PDF and Word document generators automatically inject **100 blank pages** at the end of the contact list. This allows the user to have extra space in their physical pocketbook to manually hand-write new contacts in the future.
- **Desktop Application:** The entire suite of scripts was unified into a user-friendly, Tkinter-based Windows Desktop GUI (`app.py`).
- **Standalone Executable:** The desktop application was compiled into a single portable `.exe` file using `PyInstaller`, requiring no installation or Python environment to run.

---

### 3. Development Process & Phases

**Phase 1: Initial Parsing & Text Output**
- Developed the initial `convert.py` script to parse `contacts2064.vcf`.
- Extracted `FN` (Full Name) and `TEL` (Telephone) fields.
- Implemented `quopri` decoding to handle Quoted-Printable strings in the vCard file.
- Generated a basic `.txt` file to establish the baseline extraction logic.

**Phase 2: HTML & 3"x4" Print Formatting**
- Transitioned from `.txt` to `.html` to allow for styling.
- Injected inline CSS using `@page { size: 3in 4in; }` to force physical print dimensions.
- Updated python logic to strip hyphens and spaces from numbers, and alphabetize the contact list.

**Phase 3: Multi-Format Expansion**
- Expanded the project scope to build dedicated conversion scripts for 10 different formats.
- Installed `openpyxl` for Excel generation and `fpdf2` for native, margin-controlled PDF generation.
- Installed `python-docx` to generate Word documents with precise `Inches(3)` x `Inches(4)` page sizes and custom margins.

**Phase 4: Blank Page Injection**
- Modified the `.docx` and `.pdf` scripts to append 100 extra blank pages (`pdf.add_page()` and `doc.add_page_break()`) to the end of the generated documents.

**Phase 5: UI & Desktop App Compilation**
- Built `app.py`, integrating all 10 format engines into a single Tkinter application.
- Added file browsing, output directory selection, and format toggling checkboxes.
- Used `PyInstaller` (`--onefile --windowed`) to compile `app.py` into a standalone Windows executable (`Phonebook Converter.exe`).

**Phase 6: File Reorganization & Path Correction**
- Cleaned up the workspace directory by creating a `contacts output` folder for the generated files.
- Moved all raw Python source code (`.py` files) into a dedicated `vcf to multiformat contact converter python files` folder.
- Wrote an automated string-replacement script to update all hardcoded file paths inside the Python files, changing `contacts2064.vcf` to `../contacts2064.vcf` to ensure backward compatibility with the new folder structure.
