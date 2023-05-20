TEST_FOLDER = test
TEST_APP = test.py
APP = main.py
PYTHON = python
REQUIREMENTS = requirements.txt
PIP = pip
BUILD_FOLDER = build
EXE_FOLDER = dist
INSTALL = install -r


all: setup app

run: $(APP)
	$(PYTHON) $<

app: main.py
	pyinstaller -F -w $(APP)

setup: $(REQUIREMENTS)
	$(PIP) $(INSTALL) $<
	
test: $(TEST_FOLDER)/$(TEST_APP)
	pytest $<

rm: $(BUILD_FOLDER) $(EXE_FOLDER)
	rm -d -r $^
