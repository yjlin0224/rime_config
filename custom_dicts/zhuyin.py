from datetime import date
from typing import Callable, Optional

import yaml

initial_pronunciations = {
    "ㄅ": "bo",
    "ㄆ": "po",
    "ㄇ": "mo",
    "ㄈ": "fo",
    #
    "ㄉ": "de",
    "ㄊ": "te",
    "ㄋ": "ne",
    "ㄌ": "le",
    #
    "ㄍ": "ge",
    "ㄎ": "ke",
    "ㄏ": "he",
    #
    "ㄐ": "ji",
    "ㄑ": "qi",
    "ㄒ": "xi",
    #
    "ㄓ": "zhi",
    "ㄔ": "chi",
    "ㄕ": "shi",
    "ㄖ": "ri",
    #
    "ㄗ": "zi",
    "ㄘ": "ci",
    "ㄙ": "si",
}

final_pronunciations = {
    "ㄚ": "a",
    "ㄛ": "o",
    "ㄜ": "e",
    "ㄝ": "e",  # ê
    #
    "ㄞ": "ai",
    "ㄟ": "ei",
    "ㄠ": "ao",
    "ㄡ": "ou",
    #
    "ㄢ": "an",
    "ㄣ": "en",
    "ㄤ": "ang",
    "ㄥ": "eng",
    #
    "ㄦ": "er",
    #
    "ㄧ": "yi",
    "ㄨ": "wu",
    "ㄩ": "yu",
    #
    "ㄧㄚ": "ya",
    "ㄧㄛ": "yo",
    "ㄧㄝ": "ye",
    #
    "ㄧㄞ": "yai",
    "ㄧㄟ": "yei",  # not exist in Mandarin
    "ㄧㄠ": "yao",
    "ㄧㄡ": "you",
    #
    "ㄧㄢ": "yan",
    "ㄧㄣ": "yin",
    "ㄧㄤ": "yang",
    "ㄧㄥ": "ying",
    #
    "ㄧㄦ": "yer",  # not exist in Mandarin
    #
    "ㄨㄚ": "wa",
    "ㄨㄛ": "wo",
    "ㄨㄝ": "we",  # not exist in Mandarin
    #
    "ㄨㄞ": "wai",
    "ㄨㄟ": "wei",
    "ㄨㄠ": "wao",  # not exist in Mandarin
    "ㄨㄡ": "wou",  # not exist in Mandarin
    #
    "ㄨㄢ": "wan",
    "ㄨㄣ": "wen",
    "ㄨㄤ": "wang",
    "ㄨㄥ": "weng",
    #
    "ㄨㄦ": "wer",  # not exist in Mandarin
    #
    "ㄩㄝ": "yue",
    "ㄩㄢ": "yuan",
    "ㄩㄣ": "yun",
    "ㄩㄥ": "yong",
}

initials = {
    "ㄅ": "b",
    "ㄆ": "p",
    "ㄇ": "m",
    "ㄈ": "f",
    #
    "ㄉ": "d",
    "ㄊ": "t",
    "ㄋ": "n",
    "ㄌ": "l",
    #
    "ㄍ": "g",
    "ㄎ": "k",
    "ㄏ": "h",
    #
    "ㄐ": "j",
    "ㄑ": "q",
    "ㄒ": "x",
    #
    "ㄓ": "zh",
    "ㄔ": "ch",
    "ㄕ": "sh",
    "ㄖ": "r",
    #
    "ㄗ": "z",
    "ㄘ": "c",
    "ㄙ": "s",
}


def cond(
    initials: list[str], t_final: Optional[str], f_final: Optional[str]
) -> Callable[[str], Optional[str]]:
    return lambda x: t_final if x in initials else f_final


finals: dict[str, str | Callable[[str], Optional[str]]] = {
    "ㄚ": "a",
    "ㄛ": "o",
    "ㄜ": "e",
    #
    "ㄞ": "ai",
    "ㄟ": "ei",
    "ㄠ": "ao",
    "ㄡ": "ou",
    #
    "ㄢ": "an",
    "ㄣ": "en",
    "ㄤ": "ang",
    "ㄥ": "eng",
    #
    "ㄦ": "er",  # not exist in Mandarin
    #
    "ㄧ": "i",
    "ㄨ": "u",
    "ㄩ": "v",
    #
    "ㄧㄚ": "ia",
    "ㄧㄛ": "io",
    "ㄧㄝ": "ie",
    #
    "ㄧㄞ": "iai",
    "ㄧㄟ": "iei",  # not exist in Mandarin
    "ㄧㄠ": "iao",
    "ㄧㄡ": "iu",
    #
    "ㄧㄢ": "ian",
    "ㄧㄣ": "in",
    "ㄧㄤ": "iang",
    "ㄧㄥ": "ing",
    #
    "ㄧㄦ": "ier",  # not exist in Mandarin
    #
    "ㄨㄚ": "ua",
    "ㄨㄛ": "uo",
    "ㄨㄝ": cond(["j", "q", "x"], None, "ue"),  # not exist in Mandarin
    #
    "ㄨㄞ": "uai",
    "ㄨㄟ": "ui",
    "ㄨㄠ": "uao",  # not exist in Mandarin
    "ㄨㄡ": "uou",  # not exist in Mandarin
    #
    "ㄨㄢ": cond(["j", "q", "x"], None, "uan"),
    "ㄨㄣ": cond(["j", "q", "x"], None, "un"),
    "ㄨㄤ": "uang",
    "ㄨㄥ": "ong",
    #
    "ㄨㄦ": "uer",  # not exist in Mandarin
    #
    "ㄩㄝ": cond(["j", "q", "x"], "ue", "ve"),
    "ㄩㄢ": cond(["j", "q", "x"], "uan", "van"),
    "ㄩㄣ": cond(["j", "q", "x"], "un", "vn"),
    "ㄩㄥ": "iong",
}


def main():
    zhuyin_pinyin_table: dict[str, str] = {
        **initial_pronunciations,
        **final_pronunciations,
        # **initials,
    }
    for initial_zy, initial_py in initials.items():
        for final_zy, final_py in finals.items():
            if isinstance(final_py, str):
                zhuyin_pinyin_table[initial_zy + final_zy] = initial_py + final_py
            else:
                if (py := final_py(initial_py)) is not None:
                    zhuyin_pinyin_table[initial_zy + final_zy] = initial_py + py

    header: dict[str, str | bool] = {
        "name": "zhuyin",
        "version": date.today().isoformat(),
    }

    with open("zhuyin.dict.yaml", "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(header, f, allow_unicode=True, sort_keys=False)
        f.write("...\n")
        for zy, py in zhuyin_pinyin_table.items():
            f.write(f"{zy}\t{py}\t{65536 if len(zy) == 1 else 4096}\n")


if __name__ == "__main__":
    main()
