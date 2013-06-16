run:
	twistd -n twsrs

cov:
	coverage run --branch --source talkback  `which trial` tests
	coverage report
	coverage html

.PHONY: run cov
