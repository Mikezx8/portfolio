def to_text_unicode(s):
    r = ""
    i = 0
    while i < len(s):
        c = s[i]
        o = ord(c)

        # drop emoji selector
        if o == 0xFE0F:
            i += 1
            continue

        # force text selector
        if i + 1 < len(s) and ord(s[i + 1]) == 0xFE0F:
            r += c + "\uFE0E"
            i += 2
            continue

        r += c
        i += 1

    # hard replacements (UI-safe)
    r = (
        r.replace("✅", "✓")
         .replace("❌", "✗")
         .replace("✔", "✓")
         .replace("✖", "✗")
         .replace("⭐", "★")
         .replace("➡", "→")
         .replace("⬅", "←")
         .replace("⬆", "↑")
         .replace("⬇", "↓")
    )

    return r

print(to_text_unicode("⚙️ Settings ✅ ❌ ⭐ ➡️ 💻 📚 🎨 🗑️"))
