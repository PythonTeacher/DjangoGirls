# manage.py 사이트 관리를 도와주는 파일로
# 다른 설치 작업 없이, 컴퓨터에서 웹 서버를 시작할 수 있습니다.

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoGirls.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
