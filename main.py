from utils.messages import INVALID_PATH
from utils.validators import validate_path

print(validate_path(""))
print(validate_path("C:\\Users"))
print(validate_path("C:\\ABCXYZ"))