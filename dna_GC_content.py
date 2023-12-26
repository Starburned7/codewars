def gc_content(seq):
    base_dict = {base: seq.count(base) for base in set(seq)}
    if seq:
        gc = base_dict.get('G', 0) + base_dict.get('C', 0)
        return round((gc/ len(seq) * 100),2)
    else:
        return 0


gc_content("AAATTTCCCGGG")