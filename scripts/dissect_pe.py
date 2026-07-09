#!/usr/bin/env python3
import sys
import json
import zipfile
from pathlib import Path

# Try to import pefile, if not installed, we will install it in the caller environment
try:
    import pefile
except ImportError:
    print("pefile library is not installed. Please install it first.", file=sys.stderr)
    sys.exit(1)

def dissect(zip_path: Path, output_json: Path):
    print(f"Opening ZIP: {zip_path}")
    with zipfile.ZipFile(zip_path) as zf:
        exe_data = zf.read("core_fix_v2.exe")
    
    print(f"Loaded core_fix_v2.exe ({len(exe_data)} bytes) in memory.")
    pe = pefile.PE(data=exe_data)
    
    pe_info = {}
    
    # File Header
    pe_info["file_header"] = {
        "machine": hex(pe.FILE_HEADER.Machine),
        "number_of_sections": pe.FILE_HEADER.NumberOfSections,
        "time_date_stamp": pe.FILE_HEADER.TimeDateStamp,
        "characteristics": hex(pe.FILE_HEADER.Characteristics)
    }
    
    # Optional Header
    pe_info["optional_header"] = {
        "magic": hex(pe.OPTIONAL_HEADER.Magic),
        "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
        "image_base": hex(pe.OPTIONAL_HEADER.ImageBase),
        "subsystem": pe.OPTIONAL_HEADER.Subsystem
    }
    
    # Sections
    sections = []
    for section in pe.sections:
        name = section.Name.decode('utf-8', errors='ignore').strip('\x00')
        entropy = section.get_entropy()
        sections.append({
            "name": name,
            "virtual_size": hex(section.Misc_VirtualSize),
            "raw_size": hex(section.SizeOfRawData),
            "entropy": round(entropy, 4)
        })
    pe_info["sections"] = sections
        
    # Directories
    directories = []
    for entry in pe.OPTIONAL_HEADER.DATA_DIRECTORY:
        if entry.Size > 0:
            directories.append({
                "name": entry.name,
                "virtual_address": hex(entry.VirtualAddress),
                "size": hex(entry.Size)
            })
    pe_info["directories"] = directories

    # Imports
    imports = {}
    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll_name = entry.dll.decode('utf-8', errors='ignore')
            dll_imports = []
            for imp in entry.imports:
                name = imp.name.decode('utf-8', errors='ignore') if imp.name else f"ordinal {imp.ordinal}"
                address = hex(imp.address)
                dll_imports.append({
                    "name": name,
                    "address": address
                })
            imports[dll_name] = dll_imports
    pe_info["imports"] = imports
                
    # Security Certificate
    security_dir = pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_SECURITY']]
    if security_dir.Size > 0 and security_dir.VirtualAddress > 0:
        cert_data = pe.__data__[security_dir.VirtualAddress : security_dir.VirtualAddress + security_dir.Size]
        printable = "".join(chr(b) if 32 <= b <= 126 else "." for b in cert_data)
        
        cert_excerpts = []
        for word in ["CN", "O", "L", "S", "C", "computrabajo"]:
            idx = printable.find(word)
            if idx != -1:
                cert_excerpts.append({
                    "keyword": word,
                    "offset": idx,
                    "context": printable[max(0, idx-10) : min(len(printable), idx+50)]
                })
        pe_info["security_certificate"] = {
            "offset": hex(security_dir.VirtualAddress),
            "size": hex(security_dir.Size),
            "length": int.from_bytes(cert_data[0:4], 'little'),
            "revision": hex(int.from_bytes(cert_data[4:6], 'little')),
            "cert_type": hex(int.from_bytes(cert_data[6:8], 'little')),
            "excerpts": cert_excerpts
        }
    else:
        pe_info["security_certificate"] = None

    # Write to JSON
    output_json.write_text(json.dumps(pe_info, indent=2), encoding="utf-8")
    print(f"Wrote PE dissection JSON to: {output_json}")

if __name__ == "__main__":
    dissect(Path("quarantine/core_fix_v2.zip"), Path("fixtures/detailed-pe-dissection.public.json"))
