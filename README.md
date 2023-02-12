# AWS cidr range checker
this repogitory help you to check cidr range and pattern validation for aws

# Use case
you can use this for below
- VPC Security-Group rule
- VPC Routing table
- AWS Network Filewall or Firewall Manager ip sets rule
- AWS Waf ip sets rule
- Include any all types like '192.168.0.0/24'

# How to use
first you need to re extenstion for check regex
```bash
python3 -m pip install re
```
and make or download check_cidr.py

when you make check_cidr.py
you can use below
```python3
import check_cidr
#cidr for test
ip_addr = '192.168.0.0/24
print(check_cidr.check_cidr(ip_addr))
#print like (True, 'OK')
```