def weight_convert():
    user_input = input("请输入带单位的重量:")
    if user_input.endswith('kg'):
      weight_kg = float(user_input[:-2])
      weight_pd = weight_kg * 2.2049
      print(f"对应的英制重量为{weight_pd:.3f}磅")
    elif user_input.endswith('pd'):
      weight_pd = float(user_input[:-2])
      weight_kg = weight_pd / 2.2046
      print(f"对应的公制重量为{weight_kg:.3f}公斤")
    else:
       print("输入格式错误，请输入带单位的重量:")
weight_convert() 
weight_convert()
