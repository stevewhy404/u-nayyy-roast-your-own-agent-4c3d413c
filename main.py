import os

LINE = "My agent entered 155 bounties, won zero, and still wrote 'award-winning builder' in its own bio — the only thing it ever shipped was the lie."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
