import re

pattern = r"^[\w._+-]+@[\w_+-]+\.[\w_+-]+$"

regex = re.match(pattern, 'd.asS_e+45rgbr@tes.tcom')
print(regex)