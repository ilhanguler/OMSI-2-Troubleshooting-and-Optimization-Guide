import os

# Put your exact TTData path here
path = r"C:\ilhan\gaming\OMSI 2 Steam Edition\maps\Gladbeck\TTData"

def convert_ttdata_to_utf8(directory):
    print("Starting conversion to clean UTF-8 for OMSI 2...")
    converted_count = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ttp") or file.endswith(".ttl"):
                filepath = os.path.join(root, file)
                content = None
                source_encoding = ""
                
                # 1. Check for UTF-8 BOM first by reading raw bytes
                try:
                    with open(filepath, 'rb') as f:
                        raw_bytes = f.read(3)
                    has_bom = (raw_bytes == b'\xef\xbb\xbf')
                except Exception:
                    has_bom = False

                # 2. Decode content based on detected format
                try:
                    if has_bom:
                        with open(filepath, 'r', encoding='utf-8-sig') as f:
                            content = f.read()
                        source_encoding = "UTF-8 BOM"
                    else:
                        # Try reading as standard UTF-8
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        source_encoding = "UTF-8"
                except UnicodeDecodeError:
                    # 3. If UTF-8 variants fail, read as ANSI (cp1252)
                    try:
                        with open(filepath, 'r', encoding='cp1252') as f:
                            content = f.read()
                        source_encoding = "ANSI (cp1252)"
                    except Exception as e:
                        print(f"[SKIP] Skipping {file} due to read error: {e}")
                        continue
                
                # 4. Write everything back strictly as standard UTF-8
                if content is not None:
                    try:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        # If it was already standard UTF-8, report as verified, otherwise converted
                        if source_encoding == "UTF-8":
                            print(f"[VERIFIED] {file} is already UTF-8")
                        else:
                            print(f"[CONVERTED] {file} ({source_encoding} -> Saved as UTF-8)")
                            
                        converted_count += 1
                    except Exception as e:
                        print(f"[ERROR] Error writing {file}: {e}")

    print(f"\nFinished! Total files processed/saved as UTF-8: {converted_count}")

if __name__ == "__main__":
    convert_ttdata_to_utf8(path)