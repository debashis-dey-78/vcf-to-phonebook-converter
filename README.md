# 📖 VCF to Multi-Format Phonebook Converter

A powerful Windows Desktop Application designed to seamlessly convert raw `.vcf` (vCard) contact backups into beautifully formatted, printable, pocket-sized phonebooks.

## 📥 Download the App
**[⬇️ Download Phonebook Converter.exe](https://github.com/debashis-dey-78/vcf-to-phonebook-converter/raw/main/dist/Phonebook%20Converter.exe)**

*Note: This is a standalone portable Windows executable. No complicated installation is required! Just download it and double-click to run.*

---

## ✨ Key Features

- **10 Export Formats Supported:** Export your contacts into PDF, Word (.docx), Excel (.xlsx), CSV, HTML, Markdown (.md), JSON, XML, RTF, or plain Text.
- **Physical Print Ready:** Formatted perfectly to fit a 3" x 4" physical pocketbook size.
- **Clean Typography:** Renders contact names in bold, automatically strips dashes/spaces from numbers for maximum space efficiency, and inserts uniform line breaks.
- **Auto-Sorting:** Automatically alphabetizes your entire contact list from A to Z.
- **Extra Blank Pages:** Automatically injects 100 blank pages at the end of PDF and Word document exports so you have room to handwrite new contacts in the future.
- **Privacy First:** 100% offline. Your private phone numbers are processed entirely locally on your machine and are never uploaded to any cloud server.

---

## 🛠️ How to Use

1. **Open the App:** Double-click the downloaded `Phonebook Converter.exe`.
2. **Select VCF:** Click **Browse** to select your `.vcf` mobile contact backup file.
3. **Select Destination:** Choose the output folder where you want your new phonebooks to be saved.
4. **Choose Formats:** Check the boxes for the file formats you wish to generate.
5. **Convert:** Click **Convert Contacts**. Your generated phonebooks will instantly appear in the chosen output folder!

---

## ⚙️ System Requirements & Setup

### For Standard Users (Recommended)
**No installation or prerequisites are required!** 
Because the app is bundled as a standalone executable, you only need:
- **OS:** Windows 10 or Windows 11
- **Setup:** None. Simply download the `.exe` from the link above and double-click it to run.

### For Developers (Running from Source)
If you prefer to run the raw Python scripts instead of using the `.exe`, or if you are on macOS/Linux, you must meet the following prerequisites:
- **Python:** Python 3.8 or newer installed on your system.

**Developer Setup Process:**
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/debashis-dey-78/vcf-to-phonebook-converter.git
   ```
2. Navigate into the script directory:
   ```bash
   cd "vcf-to-phonebook-converter/vcf to multiformat contact converter python files"
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main GUI application:
   ```bash
   python app.py
   ```

---

For full technical specifications and development history, please see the [App Documentation](App_Documentation.md).
