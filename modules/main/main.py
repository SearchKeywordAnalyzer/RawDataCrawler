import modules.search.parser as parser
from modules.repository.SchKwdAnz import SchKwdAnz

result = parser.get_result(top20_list=parser.get_top20_list())
print(result)
schKwdAnz = SchKwdAnz()
schKwdAnz.insert_one(result)
