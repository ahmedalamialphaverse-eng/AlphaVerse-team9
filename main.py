# ============================================================
# ⚠️ FIX THE CODE ONLY / CORRIGEZ LE CODE UNIQUEMENT / صلح الكود فقط
# ============================================================
#
# 🇬🇧 DO NOT comment any line of code (especially lines with errors).
# Only fix the code so it runs correctly.
# Any commented line → 45 min penalty.
#
# 🇫🇷 NE JAMAIS commenter les lignes du code (surtout celles avec erreurs).
# Corrigez uniquement le code.
# Toute ligne commentée → pénalité de 45 min.
#
# 🇲🇦 ماتدير حتى commentaire فالكود (خصوصاً فين كاين الخطأ).
# غير صلح الكود باش يخدم.
# أي commentaire → عقوبة 45 دقيقة.
#
# ============================================================
""" 
Requires:
    pip install pillow

Run:
    python main.py


"""



import tkinter as tk
from challenge import BUGGY_CODE
from verifier import check_solution
from ui import PuzzleGame
import io
import contextlib

root = tk.Tk()

text = tk.Text(root, width=80, height=20)
text.pack()

text.insert("1.0", BUGGY_CODE)

def verify():

    code = text.get("1.0", "end")

    try:
        output_buffer = io.StringIO()

        with contextlib.redirect_stdout(output_buffer):
            exec(code)

        output = output_buffer.getvalue()

        if check_solution(output):

            for widget in root.winfo_children():
                widget.destroy()

            PuzzleGame(root)

        else:
            result.config(text="Solution incorrecte")

    except Exception as e:
        result.config(text=f"Erreur : {e}")

btn = tk.Button(root, text="Vérifier", command=verify)
btn.pack()

result = tk.Label(root)
result.pack()

root.mainloop()








































