def meeting(s):
    names_list = s.upper().split(";")
    names_for_sorting = sorted([[name.split(":")[1], name.split(":")[0]] for name in names_list])
    result = ''.join([f"({surname}, {name})" for (surname, name) in names_for_sorting])
    return result



s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
meeting(s)