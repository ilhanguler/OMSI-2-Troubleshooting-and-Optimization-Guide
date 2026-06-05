import os

# Put your exact TTData path here
path = r"C:\ilhan\gaming\OMSI 2 Steam Edition\maps\Gladbeck\TTData"

def check_ttdata_encodings(directory):
    print("Checking OMSI 2 file encodings...")
    print("-" * 60)
    
    counts = {"UTF-8": 0, "UTF-8 BOM": 0, "ANSI (cp1252)": 0, "UNKNOWN": 0}
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ttp") or file.endswith(".ttl"):
                filepath = os.path.join(root, file)
                detected_encoding = "UNKNOWN"
                
                # 1. Check for UTF-8 BOM first by reading raw bytes
                try:
                    with open(filepath, 'rb') as f:
                        raw_bytes = f.read(3)
                    has_bom = (raw_bytes == b'\xef\xbb\xbf')
                except Exception:
                    has_bom = False

                # 2. Test decodings without modifying the file
                if has_bom:
                    detected_encoding = "UTF-8 BOM"
                else:
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            f.read()
                        detected_encoding = "UTF-8"
                    except UnicodeDecodeError:
                        try:
                            with open(filepath, 'r', encoding='cp1252') as f:
                                f.read()
                            detected_encoding = "ANSI (cp1252)"
                        except Exception:
                            detected_encoding = "UNKNOWN"

                counts[detected_encoding] += 1
                print(f"[{detected_encoding}] {file}")

    print("-" * 60)
    print("SUMMARY OF FILES:")
    for enc, count in counts.items():
        print(f"  {enc}: {count}")

if __name__ == "__main__":
    check_ttdata_encodings(path)