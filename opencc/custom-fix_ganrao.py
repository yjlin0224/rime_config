import sys


def main():
    essay_filepath = sys.argv[1]
    output_filepath = "custom-fix_ganrao.txt"
    entries: set[str] = set()

    with open(essay_filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 1 and ("干擾" in parts[0] or "干撓" in parts[0]):
                entries.add(parts[0])

    with open(output_filepath, "w", encoding="utf-8") as f:
        for entry in sorted(entries):
            to_fix = entry.replace("干", "幹")
            f.write(f"{to_fix}\t{entry}\n")


if __name__ == "__main__":
    main()
