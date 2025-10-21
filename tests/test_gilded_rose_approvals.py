import io
import sys

from approvaltests import verify
from texttest_fixture import main
from approvaltests.reporters import PythonNativeReporter

def test_gilded_rose_approvals():
    orig_sysout = sys.stdout
    try:
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        sys.argv = ["texttest_fixture.py", 30]
        main()
        answer = fake_stdout.getvalue()
    finally:
        sys.stdout = orig_sysout

    verify(answer, reporter=PythonNativeReporter())

if __name__ == "__main__":
    test_gilded_rose_approvals()
