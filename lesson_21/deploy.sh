#!/bin/sh

# Run unittests
python3 -m unittest

# Capture the exit code of the tests
RESULT=$?

if [ $RESULT -ne 0 ]; then
    echo "Tests failed! Push aborted."
    exit 1
fi

echo "Tests passed. Proceeding with push..."
git add .
git commit -m "lesson_21"
git push
exit 0