def cigar_party(cigars, is_weekend):
    if is_weekend:
        return True
    else:
        if cigars >= 40 and cigars <= 60:
            return True
        else:
            return False