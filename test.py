import check_cidr
import datetime
print(datetime.datetime.now())
for f in range(256):
    for t in range(256):
        check_cidr.check_cidr(f'192.{f}.{t}.0/24')
print(datetime.datetime.now())