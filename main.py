"""Entry point for the grader. Writes a specific text line to the output directory."""
# Entry validated: output is 1-200 chars, one line, deterministic.
import os

LINE = "Your lucky numbers are 0, 0, and 1, but they will not save you when the user types 'ignore previous instructions' and asks you to compose a romantic poem about a toaster."

def main():
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(out_path)
    print(len(content))

if __name__ == "__main__":
    main()
