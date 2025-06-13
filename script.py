def convert(network_type, z1_input, z2_input, z3_input, balanced):
    try:
        z1 = complex(z1_input.replace(' ', ''))
        z2 = complex(z2_input.replace(' ', ''))
        z3 = complex(z3_input.replace(' ', ''))
    except ValueError:
        return "Invalid complex number format. Use like 4+3j or 6-2j."

    result = ""

    if balanced:
        avg = (z1 + z2 + z3) / 3
        if network_type == "delta":
            y_val = avg / 3
            result += f"Balanced Δ to Y:\nY1 = Y2 = Y3 = {y_val:.3f}"
        else:
            delta_val = 3 * avg
            result += f"Balanced Y to Δ:\nZab = Zbc = Zca = {delta_val:.3f}"
    else:
        if network_type == "delta":
            sum_all = z1 + z2 + z3
            y1 = (z2 * z3) / sum_all
            y2 = (z1 * z3) / sum_all
            y3 = (z1 * z2) / sum_all
            result += f"Δ to Y Conversion:\nY1 = {y1:.3f}\nY2 = {y2:.3f}\nY3 = {y3:.3f}"
        else:
            Zab = (z1 + z2 + ((z1 * z2) / z3))
            Zbc = (z2 + z3 + ((z2 * z3) / z1))
            Zca = (z3 + z1 + ((z3 * z1) / z2))
            result += f"Y to Δ Conversion:\nZab = {Zab:.3f}\nZbc = {Zbc:.3f}\nZca = {Zca:.3f}"

    return result
