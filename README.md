bosun_python
============

Implementation of the Bosun API in Python


###Example Code
```
from bosun import bosun_client
bosun = bosun_client()
bosun.debug = True
tags = {"tag1": "value1","tag2": "value2"}
result = bosun.write_data("test.testvalue1",42,tags)
print result
```
