def subtraction(vals):
    vals = tuple(vals)
    subtract = vals[0]
    for i in vals[1:]:
        subtract -= i
    return subtract
