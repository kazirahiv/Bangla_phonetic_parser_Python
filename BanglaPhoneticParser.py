from string import *


class BanglaPhoneticParser:
    __shoroborno = {}
    __kar = {}
    __byanjonBorno = {}
    __juktoBorno = {}
    __oneChar = ["A", "W", "w", "F", "E", "V", "N", "a", "i", "I",
                 "u", "U", "e", "o", "O", "k", "g", "c", "j", "T", "D", "t", "d",
                 "n", "p", "f", "b", "v", "m", "z", "r", "l", "S", "s", "h", "R",
                 "y", "Y", ":", "q", "Q", "P", "G", "H", "J", "K", "L", "C", "V",
                 "B", "M", "Z", "^", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    __twoChar = ["rr", "ng", "Tw", "Tm", "Ty", "DD", "Dy", "NT",
                 "nc", "jj", "jy", "jr", "jw", "cy", "gg", "kt", "hh", "HH", "SH",
                 "tT", "hl", "hr", "hy", "hm", "hw", "sp", "sn", "st", "sT", "hn",
                 "hN", "sl", "sr", "sy", "sm", "sw", "sf", "Sl", "Sr", "Sy", "Sm",
                 "Sw", "Sn", "St", "sk", "lg", "lk", "zy", "ml", "Sc", "ll", "ly",
                 "lm", "lv", "lw", "lb", "lp", "lD", "lT", "bl", "br", "by", "bb",
                 "bd", "bj", "fl", "mr", "my", "mm", "mv", "mw", "mb", "mf", "mp",
                 "mn", "vl", "vr", "vy", "nw", "nn", "fr", "ps", "pl", "pr", "py",
                 "pp", "pn", "pt", "pT", "ns", "ny", "nm", "dr", "dy", "dm", "dv",
                 "dw", "nd", "nt", "nD", "nT", "Ny", "Nm", "Nw", "Nn", "dd", "dg",
                 "tr", "ty", "tm", "tw", "tn", "tt", "TT", "nj", "ee", "oo", "OI",
                 "OU", "kh", "gh", "Ng", "ch", "jh", "NG", "Th", "Dh", "th", "dh",
                 "ph", "bh", "sh", "Sh", "Rh", "kk", "kT", "kw", "km", "ky", "kr",
                 "kl", "kx", "ks", "gN", "dn", "gn", "gw", "gm", "gy", "gr", "gl",
                 "cc", "Kh", "Gh", "Ch", "Jh", "Ph", "Bh", "cr", "ND", "Dr", "Cr"]
    __threeChar = ["spr", "NTh", "Dhr", "NDh", "NDy", "Dhy", "NGc",
                   "jjh", "jjw", "ghn", "ktr", "kTr", "nTr", "ngo", "sth", "sty",
                   "stw", "skh", "sTr", "skr", "skl", "sph", "ShT", "Shk", "shl",
                   "shr", "shy", "shm", "shw", "shn", "sht", "Shm", "Shw", "Shf",
                   "Shp", "ShN", "rrg", "rrk", "Sch", "shc", "lbh", "ldh", "bdh",
                   "phl", "mvr", "mbh", "mph", "mpr", "mth", "bhl", "bhr", "bhy",
                   "ndh", "ndr", "ndw", "phr", "dbh", "ddh", "ddw", "ndy", "nth",
                   "ntr", "nty", "ntw", "nTh", "dhr", "dhy", "dhm", "dhw", "dhn",
                   "dgh", "thr", "thy", "thw", "tmy", "tth", "ttw", "NGj", "nch",
                   "kkh", "kxw", "kxN", "kxm", "kxy", "khy", "khr", "gdh", "gny",
                   "ghy", "ghr", "Ngk", "nk", "nky", "Ngg", "Ngm", "cch", "nDr",
                   "NDr", "dvr", "chr", "gru", "grU", "lTr"]
    __fourChar = ["hrri", "sthy", "Shkr", "Shph", "Shpr", "ShTh", "ShTr",
                  "ShTy", "rrkhy", "rrky", "rrkh", "shch", "mbhr", "ndhr", "ndhy",
                  "NGch", "kkhw", "kkhN", "kkhm", "kkhy", "Ngky", "Ngkx", "Ngkh",
                  "Nggy", "Nggh", "cchw", "cchr", "dbhr"]
    __fiveChar = ["ShThy", "Ngkkh", "Ngghy", "Ngghr"]

    def __init__(self):
        self.__shoroborno = {"rri": "ঋ", "ee": "ঈ", "oo": "উ", "OI": "ঐ", "OU": "ঔ",
                             "o": "অ", "i": "ই", "I": "ঈ", "u": "উ", "U": "ঊ", "e": "এ",
                             "E": "এ", "O": "ও", "a": "আ", "A": "আ"
                             }
        self.__kar = {"rri": "ৃ", "ee": "ী", "oo": "ু", "OI": "ৈ", "OU": "ৌ", "i": "ি", "I": "ী", "u": "ু",
                      "U": "ূ", "e": "ে", "E": "ে", "O": "ো", "a": "া", "A": "া"}
        self.__byanjonBorno = {"F": "ফ", "SH": "ষ", "V": "ভ", "tT": "ৎ", "0": "০", "1": "১", "2": "২", "3": "৩",
                               "4": "৪", "5": "৫", "6": "৬", "7": "৭", "8": "৮", "9": "৯", "k": "ক", "hh": "্",
                               "HH": "্", "kh": "খ", "Kh": "খ", "g": "গ", "gh": "ঘ", "Gh": "ঘ", "Ng": "ঙ", "c": "চ",
                               "ch": "ছ", "Ch": "ছ", "j": "জ", "jh": "ঝ", "Jh": "ঝ", "NG": "ঞ", "T": "ট",
                               "Th": "ঠ", "D": "ড", "Dh": "ঢ", "N": "ণ", "t": "ত", "th": "থ", "d": "দ", "dh": "ধ",
                               "n": "ন", "p": "প", "ph": "ফ", "Ph": "ফ", "f": "ফ", "b": "ব", "bh": "ভ",
                               "Bh": "ভ", "v": "ভ", "m": "ম", "z": "য", "r": "র", "l": "ল", "sh": "শ",
                               "S": "শ", "Sh": "ষ", "s": "স", "h": "হ", "R": "ড়", "Rh": "ঢ়", "y": "য়",
                               "Y": "য়", "ng": "ং", ":": "ঃ", "q": "ক", "Q": "ক", "P": "প", "G": "গ",
                               "H": "হ", "J": "জ", "K": "ক", "L": "ল", "C": "চ", "B": "ব", "M": "ম", "Z": "্য",
                               "^": "ঁ",
                               "w": "ও", "W": "ও"}
        self.__juktoBorno = {"spr": "স্প্র‌", "rr": "র্", "kk": "ক্ক", "ngo": "ঙ্গ", "kT": "ক্ট",
                             "kt": "ক্ত", "ktr": "ক্ত্র", "kTr": "ক্ট্র", "kw": "ক্ব", "km": "ক্ম",
                             "ky": "ক্য", "kZ": "ক্য", "kr": "ক্র", "kl": "ক্ল", "kkh": "ক্ষ", "kx": "ক্ষ",
                             "kkhw": "ক্ষ্ব", "kxw": "ক্ষ্ব", "kkhN": "ক্ষ্ণ", "kxN": "ক্ষ্ণ", "kkhm": "ক্ষ্ম",
                             "kxm": "ক্ষ্ম", "kkhy": "ক্ষ্য", "kxy": "ক্ষ্য", "kkhZ": "ক্ষ্য", "kxZ": "ক্ষ্য",
                             "ks": "ক্স",
                             "khy": "খ্য", "khZ": "খ্য", "khr": "খ্র", "gN": "গ্ণ", "gdh": "গ্ধ", "gn": "গ্ন",
                             "gny": "গ্ন্য",
                             "gnZ": "গ্ন্য", "gw": "গ্ব", "gm": "গ্ম", "gy": "গ্য", "gZ": "গ্য", "gr": "গ্র",
                             "gl": "গ্ল",
                             "ghn": "ঘ্ন", "ghy": "ঘ্য", "ghZ": "ঘ্য", "ghr": "ঘ্র", "Ngk": "ঙ্ক", "nk": "ঙ্ক",
                             "nky": "ঙ্ক্য",
                             "Ngky": "ঙ্ক্য", "nkZ": "ঙ্ক্য", "NgkZ": "ঙ্ক্য", "Ngkkh": "ঙ্ক্ষ", "Ngkx": "ঙ্ক্ষ",
                             "Ngkh": "ঙ্খ",
                             "Ngg": "ঙ্গ", "Nggy": "ঙ্গ্য", "NggZ": "ঙ্গ্য", "Ngm": "ঙ্ম", "Nggh": "ঙ্ঘ",
                             "Ngghy": "ঙ্ঘ্য", "NgghZ": "ঙ্ঘ্য",
                             "Ngghr": "ঙ্ঘ্র", "cc": "চ্চ", "cch": "চ্ছ", "cchw": "চ্ছ্ব", "cchr": "চ্ছ্র",
                             "cNG": "চ্ঞ", "cy": "চ্য",
                             "cZ": "চ্য", "jj": "জ্জ", "jjw": "জ্জ্ব", "jjh": "জ্ঝ", "gg": "জ্ঞ", "jNG": "জ্ঞ",
                             "jw": "জ্ব", "jy": "জ্য",
                             "jZ": "জ্য", "jr": "জ্র", "nc": "ঞ্চ", "NGc": "ঞ্চ", "Tw": "ট্ব", "Tm": "ট্ম", "Ty": "ট্য",
                             "TZ": "ট্য", "Tr": "ট্র",
                             "DD": "ড্ড", "Dy": "ড্য", "Dz": "ড্য", "Dr": "ড্র", "Dhy": "ঢ্য", "DhZ": "ঢ্য",
                             "Dhr": "ঢ্র", "NT": "ণ্ট",
                             "NTh": "ণ্ঠ", "ND": "ণ্ড", "NDy": "ণ্ড্য", "NDZ": "ণ্ড্য", "NDr": "ণ্ড্র", "NDh": "ণ্ঢ",
                             "nch": "ঞ্ছ", "NGch": "ঞ্ছ",
                             "nj": "ঞ্জ", "NGj": "ঞ্জ", "TT": "ট্ট", "tt": "ত্ত", "ttw": "ত্ত্ব", "tth": "ত্থ",
                             "tn": "ত্ন", "tw": "ত্ব", "tm": "ত্ম",
                             "tmy": "ত্ম্য", "tmZ": "ত্ম্য", "ty": "ত্য", "tZ": "ত্য", "tr": "ত্র", "thw": "থ্ব",
                             "thy": "থ্য", "thZ": "থ্য", "thr": "থ্র",
                             "dg": "দ্গ", "dgh": "দ্ঘ", "dd": "দ্দ", "Nn": "ণ্ন", "Nw": "ণ্ব", "Nm": "ণ্ম", "Ny": "ণ্য",
                             "NZ": "ণ্য", "dhn": "ধ্ন",
                             "dhw": "ধ্ব", "dhm": "ধ্ম", "dhy": "ধ্য", "dhZ": "ধ্য", "dhr": "ধ্র", "nT": "ন্ট",
                             "nTr": "ন্ট্র", "nTh": "ন্ঠ", "nD": "ন্ড",
                             "nt": "ন্ত", "ntw": "ন্ত্ব", "nty": "ন্ত্য", "ntZ": "ন্ত্য", "ntr": "ন্ত্র", "nth": "ন্থ",
                             "nd": "ন্দ", "ndy": "ন্দ্য", "ndZ": "ন্দ্য",
                             "ddw": "দ্দ্ব", "ddh": "দ্ধ", "dw": "দ্ব", "dv": "দ্ভ", "dbh": "দ্ভ", "dm": "দ্ম",
                             "dy": "দ্য", "dZ": "দ্য", "dr": "দ্র", "nm": "ন্ম",
                             "ny": "ন্য", "nZ": "ন্য", "ns": "ন্স", "pT": "প্ট", "pt": "প্ত", "pn": "প্ন", "pp": "প্প",
                             "py": "প্য", "pZ": "প্য", "pr": "প্র",
                             "pl": "প্ল", "ps": "প্স", "fr": "ফ্র", "phr": "ফ্র", "ndw": "ন্দ্ব", "ndr": "ন্দ্র",
                             "ndh": "ন্ধ", "ndhy": "ন্ধ্য", "ndhZ": "ন্ধ্য",
                             "ndhr": "ন্ধ্র", "nn": "ন্ন", "nw": "ন্ব", "vy": "ভ্য", "vZ": "ভ্য", "bhy": "ভ্য",
                             "bhZ": "ভ্য", "vr": "ভ্র", "bhr": "ভ্র",
                             "vl": "ভ্ল", "bhl": "ভ্ল", "mth": "ম্থ", "mn": "ম্ন", "mp": "ম্প", "mpr": "ম্প্র",
                             "mf": "ম্ফ", "mph": "ম্ফ", "mb": "ম্ব",
                             "mw": "ম্ব", "mv": "ম্ভ", "mbh": "ম্ভ", "mvr": "ম্ভ্র", "mbhr": "ম্ভ্র", "mm": "ম্ম",
                             "my": "ম্য", "mZ": "ম্য", "mr": "ম্র", "fl": "ফ্ল",
                             "phl": "ফ্ল", "bj": "ব্জ", "bd": "ব্দ", "bdh": "ব্ধ", "bb": "ব্ব", "by": "ব্য",
                             "bZ": "ব্য", "rZ": "র‍্য", "br": "ব্র", "bl": "ব্ল",
                             "lT": "ল্ট", "lD": "ল্ড", "ldh": "ল্ধ", "lp": "ল্প", "lb": "ল্ব", "lw": "ল্ব", "lv": "ল্ভ",
                             "lbh": "ল্ভ", "lm": "ল্ম", "ly": "ল্য",
                             "lZ": "ল্য", "ll": "ল্ল", "shc": "শ্চ", "Sc": "শ্চ", "shch": "শ্ছ", "Sch": "শ্ছ",
                             "ml": "ম্ল", "zy": "য্য", "zZ": "য্য",
                             "rrk": "র্ক", "rrkh": "র্খ", "rrg": "র্গ", "rrky": "র্ক্য", "rrkZ": "র্ক্য",
                             "rrkhy": "র্খ্য", "rrkhZ": "র্খ্য", "lk": "ল্ক", "lg": "ল্গ",
                             "ShTy": "ষ্ট্য", "ShTZ": "ষ্ট্য", "ShTr": "ষ্ট্র", "ShTh": "ষ্ঠ", "ShThy": "ষ্ঠ্য",
                             "ShThZ": "ষ্ঠ্য", "ShN": "ষ্ণ", "Shp": "ষ্প",
                             "Shpr": "ষ্প্র", "Shph": "ষ্ফ", "Shf": "ষ্ফ", "Shw": "ষ্ব", "Shm": "ষ্ম", "sk": "স্ক",
                             "sht": "শ্ত", "St": "শ্ত", "shn": "শ্ন",
                             "Sn": "শ্ন", "shw": "শ্ব", "Sw": "শ্ব", "shm": "শ্ম", "Sm": "শ্ম", "shy": "শ্য",
                             "shZ": "শ্য", "Sy": "শ্য", "SZ": "শ্য", "shr": "শ্র",
                             "Sr": "শ্র", "shl": "শ্ল", "Sl": "শ্ল", "Shk": "ষ্ক", "Shkr": "ষ্ক্র", "ShT": "ষ্ট",
                             "sf": "স্ফ", "sph": "স্ফ", "sw": "স্ব", "sm": "স্ম",
                             "sy": "স্য", "sZ": "স্য", "sr": "স্র", "sl": "স্ল", "skl": "স্ক্ল", "hN": "হ্ণ",
                             "hn": "হ্ন", "skr": "স্ক্র", "sT": "স্ট", "sTr": "স্ট্র",
                             "skh": "স্খ", "st": "স্ত", "stw": "স্ত্ব", "sty": "স্ত্য", "stZ": "স্ত্য", "sth": "স্থ",
                             "sthy": "স্থ্য", "sthZ": "স্থ্য", "sn": "স্ন",
                             "sp": "স্প", "hw": "হ্ব", "hm": "হ্ম", "hy": "হ্য", "hZ": "হ্য", "hr": "হ্র", "hl": "হ্ল",
                             "hrri": "হৃ", "gru": "গ্রু",
                             "grU": "গ্রূ", "lTr": "ল্ট্র", "cr": "চ্র", "Cr": "চ্র", "nDr": "ন্ড্র", "dvr": "দ্ভ্র",
                             "chr": "ছ্র", "dbhr": "দ্ভ্র"}

    def change(self, txt, ch, nch):
        return txt.replace(ch, nch)

    def changeShoroborno(self, txt, ch):
        sx = ""
        sx += txt
        if (ch.lower() == "a"):
            asx = ""
            for i in range(0, len(txt)):
                if (i == 0):
                    if ("" + txt[i].lower() == "a"):
                        asx += "আ"
                    else:
                        asx += txt[i]
                else:
                    if (("" + txt[i].lower() == "a") and (("" + txt[i - 1] in self.__shoroborno.values()) or
                                                              ("" + txt[i - 1] in self.__shoroborno.keys()) or
                                                              ("" + txt[i - 1] in self.__kar.keys()) or
                                                              ("" + txt[i - 1] in self.__kar.values()))):
                        if (("" + txt[i - 1] == "আ") or ("" + txt[i - 1] == "া") or ("" + txt[i - 1] == "a") or (
                                "" + txt[i - 1] == "A")):
                            asx += "আ"
                        else:
                            asx += "য়া"
                    elif (("" + txt[i].lower() == "a") and (("" + txt[i - 1] in self.__byanjonBorno.values()) or
                                                                ("" + txt[i - 1] in self.__byanjonBorno.keys()) or (
                            "" + txt[i - 1] in self.__juktoBorno.keys())
                                                            or ("" + txt[i - 1] in self.__juktoBorno.values()))):
                        asx += "া"
                    else:
                        asx += "" + txt[i]
            return asx
        else:
            ofe = sx.find(ch, 0)
            ofs = 0
            while ofs < len(txt) and (ofe != -1):
                ofe = sx.find(ch, ofs)
                # print(ofe)
                if (ofe == -1):
                    break
                else:
                    if (ofe == 0):
                        # print(sx)
                        sx = sx.replace(sx[ofe:ofe + len(ch)], self.__shoroborno[ch])
                    else:
                        if (ch == "o" and (("" + txt[ofe - 1] in self.__shoroborno.values()) or (
                                "" + txt[ofe - 1] in self.__shoroborno.keys())
                                           or ("" + txt[ofe - 1] in self.__kar.keys()) or (
                                "" + txt[ofe - 1] in self.__kar.values()))):
                            sx = sx.replace(sx[ofe:ofe + 1], "ও")
                        elif (("" + txt[ofe - 1] in self.__shoroborno.values()) or (
                                "" + txt[ofe - 1] in self.__shoroborno.keys())
                              or ("" + txt[ofe - 1] in self.__kar.keys()) or (
                                "" + txt[ofe - 1] in self.__kar.values()) or
                                  ("" + txt[ofe - 1] == "o")):
                            sx = sx.replace(sx[ofe:ofe + len(ch)], self.__shoroborno[ch])
                        else:
                            if ("" + txt[ofe] != "o"):
                                sx = sx.replace(sx[ofe:ofe + len(ch)], self.__kar[ch])
                ofs = ofe + 1
        return sx

    def changeX(self, txt, ch):
        s = ""
        sx = ""
        for i in range(0, len(txt)):
            if (i == 0):
                if ("" + txt[i].lower() == "x"):
                    sx += "এক্স"
                else:
                    sx += txt[i]
            else:
                if ("" + txt[i].lower() == "x"):
                    if (self.isAlphabet(txt[i - 1])):
                        sx += "ক্স"
                    else:
                        sx += "এক্স"
                else:
                    sx += txt[i]
        return sx

    def isAlphabet(self, code):
        return code.isalpha()

    def convert(self, textToConvert):
        textToConvert = textToConvert. \
            replace("A", "a"). \
            replace("B", "b"). \
            replace("C", "c"). \
            replace("E", "e"). \
            replace("F", "f"). \
            replace("G", "g"). \
            replace("H", "h"). \
            replace("J", "j"). \
            replace("K", "k"). \
            replace("L", "l"). \
            replace("M", "m"). \
            replace("P", "p"). \
            replace("Q", "q"). \
            replace("V", "v"). \
            replace("Y", "y"). \
            replace("X", "x")

        s = textToConvert
        s = self.changeX(s, "x")
        for aFiveChar in self.__fiveChar:
            s = self.change(s, aFiveChar, self.__juktoBorno[aFiveChar])
        for aFourChar in self.__fourChar:
            s = self.change(s, aFourChar, self.__juktoBorno[aFourChar])
        for aThreeChar in self.__threeChar:
            s = self.change(s, aThreeChar, self.__juktoBorno[aThreeChar])
        s = self.changeShoroborno(s, "rri")
        for aTwoChar in self.__twoChar:
            if (aTwoChar in self.__shoroborno.keys()):
                s = self.changeShoroborno(s, aTwoChar)
            elif (aTwoChar in self.__byanjonBorno.keys()):
                s = self.change(s, aTwoChar, self.__byanjonBorno[aTwoChar])
            elif (aTwoChar in self.__juktoBorno.keys()):
                s = self.change(s, aTwoChar, self.__juktoBorno[aTwoChar])
        for aOneChar in self.__oneChar:
            if (aOneChar in self.__shoroborno.keys()):
                s = self.changeShoroborno(s, aOneChar)
            elif (aOneChar in self.__byanjonBorno.keys()):
                s = self.change(s, aOneChar, self.__byanjonBorno[aOneChar])
        s = self.change(s, "o", "")

        return s

    @staticmethod
    def parse(englishTextToParse):
        tempParser = BanglaPhoneticParser()
        separatedWord = englishTextToParse.split(" ")
        convertedText = ""
        for i in range(0, len(separatedWord)):
            convertedText = convertedText + tempParser.convert(separatedWord[i]) + " ";
        # convertedText = convertedText + tempParser.convert(separatedWord[i])
        return convertedText


# letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
# 'z'] letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
# 'U','V', 'W', 'X', 'Y', 'Z'] for ch in letter: print(BanglaPhoneticParser.parse(ch))

while True:
    str = input()
    print(BanglaPhoneticParser.parse(str))
