from pathlib import Path
import datetime

today = datetime.date.today()

base_dir = Path("raporty_dzienne")

file_path = base_dir / today.strftime("%Y-%m-%d") / "raport.txt"

file_path.parent.mkdir(parents=True, exist_ok=True)

file_path.write_text("To jest treść raportu.", encoding="utf-8")

content = file_path.read_text(encoding="utf-8")
print("Zawartość pliku:")
print(content)

print("\nInformacje o pliku:")
print("Pełna ścieżka:", file_path.resolve())
print("Nazwa pliku:", file_path.name)
print("Folder nadrzędny:", file_path.parent)
