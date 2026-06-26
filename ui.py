import tkinter as tk
import os
import hashlib
import ctypes  # <-- Ajouté pour désactiver la réduction
from PIL import Image, ImageTk


class PuzzleGame:
    W, H = 650, 520

    RIDDLES = [
        {
            "text": (
                "حاجيتك و ماجيتك على الميم\n"
                "الميم توضى او صلى\n"
                "او مشا و ما ولى\n\n"
                "شنو هو؟"
            ),

            "accepted": [
                "998ee7c0c9672efa3707daeed501a93054eb2dbe887b57ed47ddeb4d28ef2a7b",  # ميت
                "ddf08a658cc66c819054760f323fc915e5724b83ae21b389be5cdd083924f8ca",  # الميت
                "b5a2baeab4bf956d9d75a9a9569bd068b8c33141d09f55f312232b8e46d5ebea",  # myt
                "3fedfdcd165747f00456904bc4526e608fa54b735ccf8dfb21dcd806796b6506",  # myit
                "07529c7e359f6f144df582c753e60366c027638a2fd25ac63c42f599c8096b35",  # myet
                "d82ee7dc26ecc9921e1f68abe452b8415255b068c78245b5e7e23d2fab4b6dd5",  # miyt
                "f6e37861c11b59cacc9ecc24a583256d44ee726ae92813151ef33af511289eb5",  # miyit
                "196ea6f41a20849887ba597461bb189749769a53466765faced6935bbaad8e13",  # miyet
                "de245bf16a55947c5257fa068baae63386cca744f1d9c9a3819dcf7f36b337ff",  # meit
                "d9b57c13afd71fc54635542fb9bd6f2228092215786ff860efc7d6cd0893ed82",  # meyit
                "29464ad9f605ea3698cd27aeb40b5734d8d2d9146d5db19a39545d1a71a50320",  # meyet
                "dd0b801f050d5c7f84c81bc3788d0380ccdb94c2190676479209919a99ab9673",  # mait
                "a5e7e358a94916f12c9ce5c59686ad4271cf7e2c6b1a2144ae032ae99e867aea",  # mayit
                "4879009d9beb6e4d80267c65d8835e85fd66cf9001504bc4cde0eb99617f0a29"   # mayet
            ]
        },
        {
            "text": (
                "حاجيتك او ماجيتك على الباء\n"
                "البا مَيعشي وليداتو،\n"
                "حتى يحرق جنيباتو؟\n\n"
                "شنو هو؟"
            ),

            "accepted": [
                "3562d899829c0b97fc39d53f6fcf3e428ef7574e0ee02e2227877f100ad246fb",  # براد
                "f7a618a89b5b21e37e946427dbde683576fe4e354adbc6f8968ce33a0a9aaa15",  # البراد
                "bc6df839c8b161195b35502d44db492f582ab3e7c8b32acdf87f979b3d914162",  # berad
                "322f965a2919f46725dece842eb487fc569656d59bf3e1d35cc33cf8a9dcdfec",  # brad
                "d8f24cc00b3df9393cc26da5dcaf76329cd19e0a4c0021418afc7cd3e69b38e0",  # bred
                "e2d60d239a066ead12c711d19fc1d7b5ee50c1966412cabbd89c0129fad1bc51",  # birad
                "e2d60d239a066ead12c711d19fc1d7b5ee50c1966412cabbd89c0129fad1bc51",  # birad
                "7fd31607e012d44ab6b9f5ceca5a8cc69e77b01e3c4e4ac134f17a15efc28ac7",  # bered
                "63e9589364d9fe57b7886e685985eea468ca64b84a4f3b42ea802c2479cbb37b",  # bared
                "13973854e8f312749056d53a0a024100d0f510caff3313ca43a36484785d7b1d",  # barad
                "52bf92049182fd2a04d1b4198e450a60d88355649a85da212019c10d8ad290d7",  # braad
                "db460b3ddf4370589e95c842b1c88da3066dbdd121cdd84e5c20de44a6815809",  # brade
                "b8d629205e3e12b296231ccc18c7b7863f4b34f646422df3b6a58152a68d7ab0",  # berrada
                "f722b68c9ff8d95919bba0e5af5ebe9633fade0e9241a449c4f743f6c44c5145",  # lberad
                "fa772ee616bbf6b6a588132d112f3b94b260cc254e260172482c2403e63fd1fe",  # lbrad
            ]
        },
        {
            "text": (
                "حاجيتك أو ما جيتك على الطاء\n"
                "الطا طولها طوال\n"
                "ومعندها خيال \n"
                "أو تديك فين ما بغيتي\n\n"
                "شنو هي؟"
            ),
            
            "accepted": [
                "c32f69eeffc5a460142456637200c46b36f062b707fdb5a96db789e3e96373ec",  # طريق
                "4452951be4d4e5a8937ed85c70f4a439930c9753d5d710ca6e7a677771a8137b",  # الطريق
                "88e586bab89ddff842b77b06da49bc1b7b9adb1f05034a19a91834d93b1a129d",  # tarik
                "260f43c2851ddb8e2db85667b615c5f966d83e98afccdd86e271ab89b8877bad",  # tariq
                "4f3688f7637169645d85a38019cfc546308f4b9fc345d1b689a8cc13474c4b49",  # tari9
                "cd2410785fb16799ba63a657f46561aac2ab07557e646a877bd1cab73c8aa980",  # triq
                "c6dd6a824ee4884b6e5687cd8089b5eeaf5c0171648ea0589cbd8a6ca956c7f0",  # tri9
                "aefd23327f9d3302efab5077134d1df0e0ad198ae4168842f1ee41ae21d95030",  # trik
                "1994d77b7cf4860a616b25003579fbb20cbe24899deb22868fb4f857746cf7e1",  # trek
                "7ea9100c00b285855ea992d2511aa345649e6d2f46d5eaf1d0aab0abce99d740",  # treq
                "4d3b96ad12e9c090a48d323a0fc8b52996ecf2844af77ed8104b6e329d00270d",  # tre9
                "e6031d9cc1679ffb6a909f2e96b9f17dcf768547332141eee312e564fff5e1ba",  # tareq
                "d4b4ba57f3e1defb1ea656f5806a1648cdf3641822e61e9430d47f4421c4f8df",  # tare9
                "b982db561969906549b464c71f64de017e07b0bcd98a5d5e2773a3fd6800ec9a",  # taryq
                "c8c4334b7b3fc8978f26f713b31aecaa9635a0eca4673d23ca171e567a42fe13",  # tary9
                "3d0b2a936f427b92a450048383c3a356f17010ea4f8a2f48a2884412354db935",  # ltriq
                "adfa44765c7223d4189ed0ed63afb51b43d6568cfe1ae510f4608e3ed12471f0",  # ltariq
                "c5e59e0826715d4b689bf1395a014211864df3a2b34e62963ab62923f26e1771",  # ltari9
            ]
        }
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("Enigmaverse")
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)
        self._center()

        self.screen = "locked"
        self.submitting = False
        self.current_riddle = 0

        self.btns = []
        self.bg_photo = None
        self._logo_photo = None
        self.entry = None
        self.feedback_job = None

        self.cv = tk.Canvas(root, width=self.W, height=self.H,
                            highlightthickness=0)
        self.cv.pack()

        self._init_bg()
        self._disable_minimize()  # <-- Appel pour désactiver la réduction

        self.cv.bind("<Motion>", self._motion)
        self.cv.bind("<Button-1>", self._click)
        self.root.bind("<Return>", self._enter_key)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        self._welcome()

    # ── Window ──────────────────────────────────────────
    def _center(self):
        x = (self.root.winfo_screenwidth() - self.W) // 2
        y = (self.root.winfo_screenheight() - self.H) // 2
        self.root.geometry(f"{self.W}x{self.H}+{x}+{y}")

    def _disable_minimize(self):
        """Désactive le bouton réduire (et agrandir) de la fenêtre sous Windows"""
        try:
            self.root.update_idletasks()
            hwnd = int(self.root.winfo_id())
            
            # GWL_STYLE = -16
            style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
            
            # Retirer WS_MINIMIZEBOX (0x00020000) et WS_MAXIMIZEBOX (0x00010000)
            style &= ~0x00020000
            style &= ~0x00010000
            
            ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)
            
            # Forcer la mise à jour de la fenêtre pour appliquer le changement visuel
            self.root.attributes("-topmost", True)
            self.root.update()
        except Exception:
            # Si pas sur Windows (ex: Linux/Mac), ça ne crashera pas
            pass

    def _on_close(self):
        if self.screen in ["victory"]:
            if self.feedback_job:
                self.root.after_cancel(self.feedback_job)
            self._remove_entry()

            self.cv.delete("ui")
            self._txt(
                self.W / 2, self.H / 2,
                "Good luck 🔐",
                "#f5d060",
                ("Arial", 24, "bold"),
                tag="ui",
                shadow=True
            )

            self.root.after(900, self.root.destroy)
        else:
            if self.screen == "riddle":
                self._feedback("يجب حل اللغز أولاً!", "#ff5555")

    # ── Background ──────────────────────────────────────
    def _init_bg(self):
        path = os.path.join(os.getcwd(), "img1.jpeg")
        if not os.path.exists(path):
            path = os.path.join(os.getcwd(), "img2.jpg")

        if os.path.exists(path):
            try:
                im = Image.open(path)
                im = im.resize((self.W, self.H), Image.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(im)
                self.cv.create_image(0, 0, image=self.bg_photo, anchor="nw", tags="bg")
                self.cv.create_rectangle(0, 0, self.W, self.H, fill="#000000", stipple="gray50", outline="", tags="bg")
                return
            except Exception:
                pass

        c1, c2 = (10, 10, 28), (24, 22, 56)
        for i in range(self.H):
            t = i / self.H
            r = int(c1[0] + (c2[0] - c1[0]) * t)
            g = int(c1[1] + (c2[1] - c1[1]) * t)
            b = int(c1[2] + (c2[2] - c1[2]) * t)
            self.cv.create_line(0, i, self.W, i, fill=f"#{r:02x}{g:02x}{b:02x}", tags="bg")

    # ── Logo Loader ─────────────────────────────────────
    def _load_logo(self, max_h=110):
        path = os.path.join(os.getcwd(), "enigmaverse.png")
        if os.path.exists(path):
            try:
                im = Image.open(path)
                ratio = max_h / im.height
                new_w = int(im.width * ratio)
                im = im.resize((new_w, max_h), Image.LANCZOS)
                self._logo_photo = ImageTk.PhotoImage(im)
                return True
            except Exception:
                pass
        return False

    # ── Rounded rect ───────────────────────────────────
    def _rrect(self, x0, y0, x1, y1, r, **kw):
        pts = [x0 + r, y0, x1 - r, y0, x1, y0, x1, y0 + r, x1, y1 - r, x1, y1, x1 - r, y1,
               x0 + r, y1, x0, y1, x0, y1 - r, x0, y0 + r, x0, y0]
        return self.cv.create_polygon(pts, smooth=True, **kw)

    def _txt(self, x, y, text, fill, font, tag="ui", shadow=True, justify="center"):
        if shadow:
            self.cv.create_text(x + 1, y + 2, text=text, fill="#000000", font=font, tags=tag, justify=justify)
        self.cv.create_text(x, y, text=text, fill=fill, font=font, tags=tag, justify=justify)

    # ── Clear UI ────────────────────────────────────────
    def _clear_ui(self):
        self.cv.delete("ui")
        self.cv.delete("feedback")
        self.cv.delete("copy_feedback")
        self.btns.clear()
        self.submitting = False
        self._remove_entry()

        if self.feedback_job:
            self.root.after_cancel(self.feedback_job)
            self.feedback_job = None

    # ── Buttons ─────────────────────────────────────────
    def _add_btn(self, cx, cy, w, h, text, cmd, style="primary"):
        if style == "primary":
            bg, hv, fg = "#e8b923", "#f5d060", "#0c0c1d"
        elif style == "copy":
            bg, hv, fg = "#2563eb", "#3b82f6", "#ffffff"
        else:
            bg, hv, fg = "#1e1e3c", "#2e2e5c", "#d0d0e8"

        btn = {"cx": cx, "cy": cy, "w": w, "h": h, "text": text, "cmd": cmd,
               "bg": bg, "hv": hv, "fg": fg, "rid": None, "tid": None, "hov": False}
        self._draw_btn(btn)
        self.btns.append(btn)

    def _draw_btn(self, b):
        x0, y0 = b["cx"] - b["w"] / 2, b["cy"] - b["h"] / 2
        x1, y1 = b["cx"] + b["w"] / 2, b["cy"] + b["h"] / 2
        r = min(b["w"], b["h"]) / 2
        color = b["hv"] if b["hov"] else b["bg"]

        if b["rid"]: self.cv.delete(b["rid"])
        if b["tid"]: self.cv.delete(b["tid"])

        self._rrect(x0 + 2, y0 + 3, x1 + 2, y1 + 3, r, fill="#050510", outline="", tags="ui")
        b["rid"] = self._rrect(x0, y0, x1, y1, r, fill=color, outline="#333344", width=1, tags="ui")

        fs = 16 if b["w"] >= 140 else 14
        b["tid"] = self.cv.create_text(b["cx"], b["cy"], text=b["text"], fill=b["fg"], font=("Arial", fs, "bold"), tags="ui")

    def _motion(self, e):
        for b in self.btns:
            hit = (abs(e.x - b["cx"]) <= b["w"] / 2 and abs(e.y - b["cy"]) <= b["h"] / 2)
            if hit != b["hov"]:
                b["hov"] = hit
                self._draw_btn(b)
        self.cv.config(cursor="hand2" if any(b["hov"] for b in self.btns) else "")

    def _click(self, e):
        for b in self.btns:
            if (abs(e.x - b["cx"]) <= b["w"] / 2 and abs(e.y - b["cy"]) <= b["h"] / 2):
                b["cmd"]()
                return

    def _enter_key(self, _):
        if self.screen == "riddle" and self.entry and not self.submitting:
            self._submit()

    # ── Entry ───────────────────────────────────────────
    def _make_entry(self, cx, cy, w=320, h=48):
        self._remove_entry()
        frame = tk.Frame(self.root, bg="#4a4a7a", highlightbackground="#e8b923", highlightthickness=1)
        self.entry = tk.Entry(frame, font=("Arial", 16), bg="#12122a", fg="#ffffff",
                              insertbackground="#e8b923", relief="flat", justify="center", highlightthickness=0)
        self.entry.pack(padx=4, pady=4, fill="both", expand=True)
        frame.place(x=cx - w / 2, y=cy - h / 2, width=w, height=h)
        self._entry_frame = frame
        self.entry.focus_set()

    def _remove_entry(self):
        if self.entry:
            self.entry.destroy()
            self.entry = None
        if hasattr(self, "_entry_frame") and self._entry_frame:
            self._entry_frame.destroy()
            self._entry_frame = None

    # ── Screens ─────────────────────────────────────────
    def _welcome(self):
        self._clear_ui()
        self.screen = "welcome"
        self.current_riddle = 0

        if self._load_logo():
            self.cv.create_image(self.W / 2, 95, image=self._logo_photo, anchor="center", tags="ui")

        self._rrect(self.W / 2 - 240, 170, self.W / 2 + 240, 280, 24, fill="#0f0f25", outline="#2a2530", width=1, tags="ui")
        self._txt(self.W / 2, 210, "مرحبا بكم في حاجيتك او ماجيتك", "#ffffff", ("Arial", 20, "bold"), shadow=True)
        self._txt(self.W / 2, 255, "3 ألغاز تنتظرك", "#8888bb", ("Arial", 13), shadow=False)

        self._add_btn(self.W / 2, 350, 220, 54, "ابدأ التحدي", self._start, "primary")

    def _start(self):
        self._riddle()

    def _riddle(self):
        self._clear_ui()
        self.screen = "riddle"

        riddle = self.RIDDLES[self.current_riddle]
        progress = f"الغز {self.current_riddle + 1} / {len(self.RIDDLES)}"

        # Barre de progression
        bar_w = 300
        bar_h = 8
        bar_x0 = self.W / 2 - bar_w / 2
        bar_y = 42
        self._rrect(bar_x0, bar_y, bar_x0 + bar_w, bar_y + bar_h, 4,
                    fill="#1a1a3a", outline="#2a2a5a", width=1, tags="ui")
        fill_w = bar_w * (self.current_riddle / len(self.RIDDLES))
        if fill_w > 0:
            self._rrect(bar_x0, bar_y, bar_x0 + fill_w, bar_y + bar_h, 4,
                        fill="#4ade80", outline="", tags="ui")
        self._txt(self.W / 2, 28, progress, "#8888bb", ("Arial", 12), shadow=False)

        # Panel énigme
        self._rrect(self.W / 2 - 270, 60, self.W / 2 + 270, 250, 22,
                    fill="#0f0f25", outline="#3a3a6a", width=1, tags="ui")
        self._txt(self.W / 2, 155, riddle["text"], "#ffffff", ("Arial", 16, "bold"), justify="center")

        self._make_entry(self.W / 2, 305)

        self._add_btn(self.W / 2 - 85, 370, 150, 48, "أجب", self._submit, "primary")
        self._add_btn(self.W / 2 + 85, 370, 150, 48, "مسح", self._reset, "secondary")

    def _submit(self):
        if not self.entry or self.submitting:
            return

        # 1. Nettoyer la saisie (comme avant)
        ans = self.entry.get().strip().lower().replace(" ", "").replace("ال", "")
        
        # 2. Convertir en hash SHA-256
        hashed_ans = hashlib.sha256(ans.encode('utf-8')).hexdigest()
        
        riddle = self.RIDDLES[self.current_riddle]

        # 3. Vérifier si le hash est dans la liste des accepts
        if hashed_ans in riddle["accepted"]:
            self.submitting = True

            self.current_riddle += 1

            if self.current_riddle >= len(self.RIDDLES):
                self._victory()
            else:
                self._next_riddle_anim()
            return

        self._feedback("إجابة خاطئة، حاول مرة أخرى!", "#ff5555")

    def _next_riddle_anim(self):
        self._remove_entry()
        self.cv.delete("ui")
        self.cv.delete("feedback")

        self._txt(self.W / 2, self.H / 2 - 20, "صحيح ✅", "#4ade80", ("Arial", 32, "bold"))
        self._txt(self.W / 2, self.H / 2 + 30, "الغز التالي...", "#8888bb", ("Arial", 16), shadow=False)

        self.submitting = False
        self.root.after(1200, self._riddle)

    def _reset(self):
        if self.entry and not self.submitting:
            self.entry.delete(0, tk.END)
            self.entry.focus_set()
            self.cv.delete("feedback")

    def _feedback(self, text, color):
        self.cv.delete("feedback")
        self._rrect(self.W / 2 - 160, 425, self.W / 2 + 160, 460, 14, fill="#0f0f25", outline="", tags="feedback")
        self._txt(self.W / 2, 442, text, color, ("Arial", 13, "bold"), tag="feedback", shadow=False)

    def _victory(self):
        self._clear_ui()
        self.screen = "victory"

        # Full progress bar (completed)
        bar_w = 300
        bar_h = 8
        bar_x0 = self.W / 2 - bar_w / 2
        bar_y = 42
        self._rrect(bar_x0, bar_y, bar_x0 + bar_w, bar_y + bar_h, 4,
                    fill="#4ade80", outline="", tags="ui")
        self._txt(self.W / 2, 28, f"الغز {len(self.RIDDLES)} / {len(self.RIDDLES)}",
                "#8888bb", ("Arial", 12), shadow=False)

        # Trophy / celebration header
        self._txt(self.W / 2, 105, "🎉", "#f5d060", ("Arial", 48), shadow=False)
        self._txt(self.W / 2, 168, "CONGRATULATIONS!", "#f5d060", ("Arial", 22, "bold"), shadow=True)
        self._txt(self.W / 2, 205, "لقد حللت جميع الألغاز!", "#4ade80", ("Arial", 14), shadow=False)

        # Info panel
        self._rrect(self.W / 2 - 250, 230, self.W / 2 + 250, 360, 22,
                    fill="#0f0f25", outline="#3a3a6a", width=1, tags="ui")
        self._txt(self.W / 2, 265,
                "The real password can be found in the book:",
                "#8888bb", ("Arial", 12), shadow=False)
        self._txt(self.W / 2, 310, "للرجال فقط",
                "#ffd700", ("Arial", 24, "bold"), shadow=True)
        self._txt(self.W / 2, 348, "Good luck 🔐",
                "#8888bb", ("Arial", 12), shadow=False)

        # Exit button
        self._add_btn(self.W / 2, 430, 180, 50, "Exit", self.root.destroy, "primary")

if __name__ == "__main__":
    root = tk.Tk()
    PuzzleGame(root)
    root.mainloop()