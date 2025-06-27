def convert(network_type, z1_input, z2_input, z3_input, balanced):
    try:
        z1 = complex(z1_input.replace(' ', ''))
        z2 = complex(z2_input.replace(' ', ''))
        z3 = complex(z3_input.replace(' ', ''))
    except ValueError:
        return "Invalid complex number format. Use like 4+3j or 6-2j."

    result = ""

    if balanced:
        if network_type == "delta": # convert to wye
            y_val = z1/3
            result += f"Balanced Δ to Y:\nY1 = Y2 = Y3 = {y_val:.3f}"
        else:
            delta_val = 3 * z1
            result += f"Balanced Y to Δ:\nZab = Zbc = Zca = {delta_val:.3f}"
    else:
        if network_type == "delta": # convertto wye
            y1 = (z2 * z3) / (z1 + z2 + z3)
            y2 = (z1 * z3) / (z1 + z2 + z3)
            y3 = (z1 * z2) / (z1 + z2 + z3)
            result += f"Δ to Y Conversion:\nY1 = {y1:.3f}\nY2 = {y2:.3f}\nY3 = {y3:.3f}"
        else: # netwrok is wye type, convert to delta
            Zab = (z1*z2 + z2*z3 + z3*z1)/z1
            Zbc = (z1*z2 + z2*z3 + z3*z1)/z2
            Zca = (z1*z2 + z2*z3 + z3*z1)/z3
            result += f"Y to Δ Conversion:\nZab = {Zab:.3f}\nZbc = {Zbc:.3f}\nZca = {Zca:.3f}"

    return result
