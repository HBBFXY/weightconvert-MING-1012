weight_str = input()
num = float(weight_str[:-2])
unit = weight_str[-2:]
if unit == "kg":
    pound = num * 2.2046
    print(f"对应的英制重量为{pound:.3f}磅")
elif unit == "pd":
    kg = num / 2.2049
    print(f"对应的公制重量为{kg:.3f}公斤")
