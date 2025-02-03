# Description: Makefile for running BDD UI tests with Allure report

# Local variables:
ALLURE_RESULTS_DIR = $(shell pwd)/allure-results
ALLURE_REPORT_DIR = $(shell pwd)/allure-report

# Docker variables:
DOCKER_IMAGE = python-ui-test
DOKCER_ALLURE_RESULTS_DIR = $(shell pwd)/docker-allure-results
DOCKER_ALLURE_REPORT_DIR = $(shell pwd)/docker-allure-report


### LOCAL PYTHON RUN: ##########################################
run-level-e2e-tests:
	@echo "Starting to run the tests locally..."
	source .venv/bin/activate && behave --tags=level_e2e --no-skipped \
	|| echo "Tests failed. Proceeding to generate the Allure report."

generate-allure-report:
	@echo "Generating Allure report..."
	allure generate --single-file $(ALLURE_RESULTS_DIR) --clean -o $(ALLURE_REPORT_DIR)

open-local-allure-report:
	@echo "Attempting to open the Allure report in browser. If it does not open automatically, please open '$(ALLURE_REPORT_DIR)/index.html' manually."
	allure open $(ALLURE_REPORT_DIR)

clean-local-reports:
	@echo "Cleaning up the allure reports..."
	rm -rf allure-report/* allure-results/* allure-screen-shots/*

run-local-all: clean-local-reports run-level-e2e-tests generate-allure-report open-local-allure-report


### LOCAL DOCKER RUN: ##########################################
build:
	@echo "Building the Docker image..."
	docker buildx build --platform linux/amd64 -t $(DOCKER_IMAGE) --load --no-cache .

run-tests-and-generate-allure-report:
	@echo "Running the tests and generating Allure report..."
	docker run --rm -it \
		-v $(DOCKER_ALLURE_REPORT_DIR):/app/allure-report \
		-v $(DOKCER_ALLURE_RESULTS_DIR):/app/allure-results $(DOCKER_IMAGE)

# Clean up allure files
clean-docker-reports:
	@echo "Cleaning up the allure reports..."
	rm -rf docker-allure-report/* docker-allure-results/* allure-screenshots allure-results allure-report

open-docker-allure-report:
	@echo "Attempting to open the Allure report in browser. If it does not open automatically, please open '$(DOCKER_ALLURE_REPORT_DIR)/index.html' manually."
	open docker-allure-report/index.html

# Before run:
# Make sure that you have Docker installed and in 'environment.py' set 'headless=True' in browser_chrome method.
run-docker-all: clean-docker-reports build run-tests-and-generate-allure-report open-docker-allure-report
